#!/usr/bin/env python3
"""build.py — 各章の index.html から「完全版」（単一ファイル）を生成する。

shared/ の CSS・JS と、ローカル画像（qr.svg / _assets/*.png）を HTML に
インライン化し、dist/<章名>.html として 1 ファイルにまとめる。
リポジトリやネット接続なしで開ける、配布・オフライン閲覧用のファイル。

正本は各章の index.html（shared/ 参照版）のまま。dist/ はビルド成果物で
git 管理外。内容や shared/ を変更したら `python build.py` で再生成する。

SEO / 重複コンテンツ対策:
  完全版 HTML には `<link rel="canonical" href="編集用URL">` と
  `<meta name="robots" content="noindex, follow">` を自動挿入する。
  Pages 上で 2 系統の URL（章フォルダ / dist/）が同一コンテンツを返すため、
  検索エンジンには編集用 URL を正本として扱わせる。

既知の制約:
  theme.css は Google Fonts を @import している。完全オフラインでは
  Web フォントが読めず、システムフォントにフォールバックする
  （レイアウトは崩れない）。フォント自体の埋め込みは行わない。

依存: Python 3 標準ライブラリのみ。
使い方: リポジトリ直下で `python build.py`
"""
from __future__ import annotations

import base64
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"

# Pages 上の編集用 URL のベース。完全版 HTML の canonical に使う。
CANONICAL_BASE = "https://co-lect.github.io/lectures"

# 外部 / data URI は埋め込み対象外（そのまま残す）
_SKIP_PREFIXES = ("http://", "https://", "data:", "//")


def find_chapters() -> list[Path]:
    """`NN-...` 形式で index.html を持つ章ディレクトリを返す。"""
    return sorted(p.parent for p in ROOT.glob("[0-9][0-9]-*/index.html"))


def data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    if mime is None:
        mime = "application/octet-stream"
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{b64}"


def inline(html: str, base_dir: Path) -> str:
    """html 内のローカル CSS / JS / 画像参照をインライン化して返す。"""

    def resolve(ref: str) -> Path:
        return (base_dir / ref).resolve()

    def is_local(ref: str) -> bool:
        return not ref.startswith(_SKIP_PREFIXES)

    # 1. <link rel="stylesheet" href="..."> → <style>...</style>
    def css_repl(m: re.Match) -> str:
        href = m.group("href")
        if not is_local(href):
            return m.group(0)
        css = resolve(href).read_text(encoding="utf-8-sig")
        return f"<style>\n{css}\n</style>"

    html = re.sub(
        r'<link\s+rel="stylesheet"\s+href="(?P<href>[^"]+)"\s*/?\s*>',
        css_repl,
        html,
    )

    # 2. <script src="..."> の開始タグだけを差し替え、ソースを流し込む。
    #    元の </script> はそのまま残り、インライン化したスクリプトを閉じる。
    #    （終了タグを正規表現で扱わないことで、script 要素全体をマッチする
    #     脆い正規表現パターンを避ける）
    #    defer 属性は落ちるが、progress-strip.js は readyState を自前で
    #    ガードしており、deck-stage.js は head 配置で問題ない。
    def js_repl(m: re.Match) -> str:
        src = m.group("src")
        if not is_local(src):
            return m.group(0)
        js = resolve(src).read_text(encoding="utf-8-sig")
        # JS 内に "</script" があると HTML パーサが script を誤って閉じる。
        # "<\/script" は JS 上は等価（文字列・正規表現・コメントいずれでも安全）。
        js = js.replace("</script", "<\\/script")
        return f"<script>\n{js}\n"

    html = re.sub(r'<script\s+src="(?P<src>[^"]+)"[^>]*>', js_repl, html)

    # 3. <img ... src="..."> のローカル画像 → data URI
    def img_repl(m: re.Match) -> str:
        src = m.group("src")
        if not is_local(src):
            return m.group(0)
        return m.group(0).replace(f'src="{src}"', f'src="{data_uri(resolve(src))}"')

    html = re.sub(r'<img\b[^>]*\bsrc="(?P<src>[^"]+)"[^>]*>', img_repl, html)

    return html


def inject_seo_meta(html: str, chapter_name: str) -> str:
    """完全版 HTML に canonical と robots=noindex を </head> 直前に注入する。

    編集用 URL（章フォルダ）が正本であることを検索エンジンに伝え、
    完全版 URL（dist/<章名>.html）の重複 indexing を避ける。
    """
    canonical = f"{CANONICAL_BASE}/{chapter_name}/"
    tags = (
        f'<link rel="canonical" href="{canonical}">\n'
        f'<meta name="robots" content="noindex, follow">\n'
    )
    if "</head>" in html:
        return html.replace("</head>", tags + "</head>", 1)
    # </head> が無いケースは想定外。head 解析より、検出して失敗させる方が安全
    raise RuntimeError(f"{chapter_name}: </head> が見つからず canonical を挿入できません")


def main() -> int:
    # Windows の既定コンソール（cp932）でも日本語を出せるようにする
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    chapters = find_chapters()
    if not chapters:
        print("章ディレクトリ（NN-.../index.html）が見つかりません。", file=sys.stderr)
        return 1

    DIST.mkdir(exist_ok=True)
    ok = True
    print(f"完全版をビルド中（{len(chapters)} 章）...\n")

    for ch in chapters:
        html = (ch / "index.html").read_text(encoding="utf-8-sig")
        built = inline(html, ch)
        built = inject_seo_meta(built, ch.name)

        # 未解決のローカル参照（../ や _assets/）が残っていないか検証
        leftover = sorted(set(re.findall(
            r'(?:href|src)="((?:\.\./|\./|_assets/)[^"]*)"', built)))

        out = DIST / f"{ch.name}.html"
        out.write_text(built, encoding="utf-8")
        size_kb = out.stat().st_size / 1024

        if leftover:
            ok = False
            print(f"  [NG] {out.relative_to(ROOT)}  ({size_kb:,.0f} KB)")
            print(f"       未解決のローカル参照: {leftover}")
        else:
            print(f"  [OK] {out.relative_to(ROOT)}  ({size_kb:,.0f} KB)")

    print()
    if not ok:
        print("一部の参照を埋め込めませんでした。上記を確認してください。", file=sys.stderr)
        return 1
    print(f"完了: dist/ に {len(chapters)} ファイルを生成しました。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
