#!/usr/bin/env python3
"""sync_listings.py — keep listing files in sync with NN-slug/index.html.

Discovers lecture directories matching ``NN-slug/`` at the repo root,
extracts metadata (title / meta description / <section> count / git lastmod),
and rewrites the auto-generated blocks (delimited by HTML comment markers)
inside sitemap.xml, llms.txt, index.html, and README.md.

Usage:
  python3 scripts/sync_listings.py --check   # exit 1 if any block drifts
  python3 scripts/sync_listings.py --write   # apply drift back to disk

Marker format:
  <!-- listings:auto:start --> ... <!-- listings:auto:end -->
  <!-- listings:auto:<name>:start --> ... <!-- listings:auto:<name>:end -->

No third-party deps; Python 3.8+ standard library only.
"""
from __future__ import annotations

import argparse
import datetime
import html
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

SITE_BASE = "https://co-lect.github.io/lectures/"
LECTURE_DIR_RE = re.compile(r"^([0-9]{2})-([a-z0-9-]+)$")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL)
META_DESC_RE = re.compile(
    r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']',
    re.DOTALL,
)
SECTION_RE = re.compile(r"<section[\s>]")


def repo_root() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    )
    return Path(out.stdout.strip())


def git_lastmod(rel_path: str, root: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel_path],
            capture_output=True, text=True, check=True, cwd=root,
        )
        date = out.stdout.strip()
        if date:
            return date
    except subprocess.CalledProcessError:
        pass
    return datetime.date.today().isoformat()


@dataclass
class Lecture:
    num: str
    slug: str
    raw_title: str
    desc: str
    slide_count: int
    lastmod: str

    @property
    def dir_name(self) -> str:
        return f"{self.num}-{self.slug}"

    @property
    def url(self) -> str:
        return f"{SITE_BASE}{self.dir_name}/"

    @property
    def topic(self) -> str:
        """Short topic title for listing display.

        Handles two patterns:
          "Lecture 01 — Foo"        → "Foo"
          "Read me — 1 年で..."      → "Read me"
          (anything else)            → full title (after stripping " — Lectures")
        """
        t = re.sub(r"\s+—\s+Lectures$", "", self.raw_title.strip())
        m = re.match(r"^Lecture\s+\d{2}\s+—\s+(.+)$", t)
        if m:
            return m.group(1).strip()
        m = re.match(r"^(.+?)\s+—\s+.+$", t)
        if m:
            return m.group(1).strip()
        return t


def _extract(pattern: re.Pattern, page: str, label: str, path: Path) -> str:
    m = pattern.search(page)
    if not m:
        raise SystemExit(f"ERROR: missing {label} in {path}")
    # HTML entities in the source decode to their characters so that
    # renderers can re-escape per output format without double-encoding.
    return html.unescape(m.group(1).strip())


def discover_lectures(root: Path) -> list[Lecture]:
    lectures: list[Lecture] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        m = LECTURE_DIR_RE.match(child.name)
        if not m:
            continue
        idx = child / "index.html"
        if not idx.exists():
            raise SystemExit(
                f"ERROR: {child.name}/ matches the lecture naming pattern "
                f"but has no index.html"
            )
        page = idx.read_text(encoding="utf-8")
        lectures.append(Lecture(
            num=m.group(1),
            slug=m.group(2),
            raw_title=_extract(TITLE_RE, page, "<title>", idx),
            desc=_extract(META_DESC_RE, page, '<meta name="description">', idx),
            slide_count=len(SECTION_RE.findall(page)),
            lastmod=git_lastmod(f"{child.name}/index.html", root),
        ))
    return lectures


# Pre-flight validation. Reject metadata characters that would break the
# rendered output: newlines collapse listings, "<!-- listings:auto" would
# corrupt our own marker scan, and pipes break markdown tables. Keep this
# strict so we fail fast instead of producing a malformed file.
FORBIDDEN_SUBSTRINGS = ("<!-- listings:auto", "\n", "\r", "|")


def validate_metadata(lectures: list[Lecture]) -> None:
    for lec in lectures:
        for field_name, value in (("<title>", lec.raw_title),
                                  ("<meta description>", lec.desc)):
            for bad in FORBIDDEN_SUBSTRINGS:
                if bad in value:
                    label = repr(bad) if bad.strip() else "newline/CR"
                    raise SystemExit(
                        f"ERROR: {lec.dir_name}/index.html {field_name} "
                        f"contains forbidden substring {label}: {value!r}"
                    )


# --- renderers ---------------------------------------------------------------

def _h(value: str) -> str:
    """Escape for HTML/XML text content and attribute values."""
    return html.escape(value, quote=True)


def render_sitemap(lectures: list[Lecture]) -> str:
    parts = []
    for lec in lectures:
        parts.append(
            "  <url>\n"
            f"    <loc>{_h(lec.url)}</loc>\n"
            f"    <lastmod>{_h(lec.lastmod)}</lastmod>\n"
            "    <changefreq>monthly</changefreq>\n"
            "    <priority>0.8</priority>\n"
            "  </url>"
        )
    return "\n".join(parts)


def render_llms(lectures: list[Lecture]) -> str:
    return "\n".join(
        f"- [{lec.num} {lec.topic}]({lec.url}): {lec.desc}"
        for lec in lectures
    )


def render_index_html(lectures: list[Lecture]) -> str:
    blocks = []
    for lec in lectures:
        blocks.append(
            "    <li>\n"
            f'      <a class="title" href="{_h(lec.dir_name)}/">'
            f"{_h(lec.num)} — {_h(lec.topic)}</a>\n"
            f'      <div class="desc">{_h(lec.desc)}</div>\n'
            "    </li>"
        )
    return "\n".join(blocks)


def render_readme_table(lectures: list[Lecture]) -> str:
    # `|` and newlines are blocked at validate_metadata(); escape angle
    # brackets so values like `<X>` do not get treated as raw HTML by
    # markdown renderers.
    def md(v: str) -> str:
        return v.replace("<", "&lt;").replace(">", "&gt;")

    return "\n".join(
        f"| [`{lec.dir_name}/`](./{lec.dir_name}/index.html) "
        f"| {md(lec.topic)} | {lec.slide_count} 枚 |"
        for lec in lectures
    )


def render_readme_urls(lectures: list[Lecture]) -> str:
    return "\n".join(lec.url for lec in lectures)


RENDERERS = {
    "sitemap": render_sitemap,
    "llms": render_llms,
    "index": render_index_html,
    "readme_table": render_readme_table,
    "readme_urls": render_readme_urls,
}

# (path, marker, renderer_key)
TARGETS: list[tuple[str, str, str]] = [
    ("sitemap.xml", "listings:auto", "sitemap"),
    ("llms.txt", "listings:auto", "llms"),
    ("index.html", "listings:auto", "index"),
    ("README.md", "listings:auto:lectures-table", "readme_table"),
    ("README.md", "listings:auto:lectures-urls", "readme_urls"),
]


# --- marker replace ----------------------------------------------------------

def replace_block(text: str, marker: str, replacement: str) -> tuple[str, bool]:
    """Replace content between marker comments, preserving the end marker's
    leading indentation. Returns (new_text, changed)."""
    start_tag = f"<!-- {marker}:start -->"
    end_tag = f"<!-- {marker}:end -->"
    s = text.find(start_tag)
    if s < 0:
        raise SystemExit(f"ERROR: '{start_tag}' not found")
    after_start = s + len(start_tag)
    e = text.find(end_tag, after_start)
    if e < 0:
        raise SystemExit(f"ERROR: '{end_tag}' not found (after start marker)")
    line_start = text.rfind("\n", 0, e) + 1
    end_indent = text[line_start:e]
    if end_indent.strip():
        end_indent = ""  # not pure whitespace; do not preserve
    current = text[after_start:e]
    new = f"\n{replacement}\n{end_indent}"
    if current == new:
        return text, False
    return text[:after_start] + new + text[e:], True


# --- main --------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true",
                   help="exit 1 if any block drifts")
    g.add_argument("--write", action="store_true",
                   help="write drift back to disk")
    args = ap.parse_args()

    root = repo_root()
    lectures = discover_lectures(root)
    if not lectures:
        print("No lectures discovered.", file=sys.stderr)
        return 2
    validate_metadata(lectures)

    file_text: dict[str, str] = {}
    drifted: list[tuple[str, str]] = []

    for path_str, marker, key in TARGETS:
        path = root / path_str
        if path_str not in file_text:
            file_text[path_str] = path.read_text(encoding="utf-8")
        replacement = RENDERERS[key](lectures)
        new_text, changed = replace_block(file_text[path_str], marker, replacement)
        file_text[path_str] = new_text
        if changed:
            drifted.append((path_str, marker))

    if args.check:
        if not drifted:
            print(f"OK: all listings in sync ({len(lectures)} lectures).")
            return 0
        print(f"Drift detected in {len(drifted)} block(s):", file=sys.stderr)
        for path_str, marker in drifted:
            print(f"  - {path_str} [{marker}]", file=sys.stderr)
        print(
            "\nTo fix:\n  python3 scripts/sync_listings.py --write\n"
            "then commit the result.",
            file=sys.stderr,
        )
        summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary_path:
            with open(summary_path, "a", encoding="utf-8") as f:
                f.write("### Listings out of sync\n\n")
                f.write("The following auto-generated blocks need regeneration:\n\n")
                for path_str, marker in drifted:
                    f.write(f"- `{path_str}` (`{marker}`)\n")
                f.write(
                    "\n**Fix locally:**\n"
                    "```\npython3 scripts/sync_listings.py --write\n```\n"
                    "then commit the result.\n"
                )
        return 1

    # --write
    changed_files = {p for p, _ in drifted}
    for path_str in changed_files:
        (root / path_str).write_text(file_text[path_str], encoding="utf-8")
    if changed_files:
        print(f"Wrote {len(changed_files)} file(s): "
              f"{', '.join(sorted(changed_files))}")
    else:
        print(f"OK: nothing to write ({len(lectures)} lectures, all in sync).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
