# scripts/

リポジトリ運用のためのユーティリティスクリプト。

---

## `sync_listings.py` — 講義一覧の自動同期

`NN-slug/index.html` を真実源（source of truth）として、以下の自動生成ブロックを同期する：

| ファイル | 同期される場所 |
|---|---|
| `sitemap.xml` | `<!-- listings:auto:start --> ... :end -->` — 講義 URL の `<url>` ブロック |
| `llms.txt` | 同上 — 「## 講義」の箇条書き |
| `index.html`（ルート） | 同上 — `<ul class="map">` の中身 |
| `README.md` | `<!-- listings:auto:lectures-table:start -->` 〜 — 章テーブル |
| `README.md` | `<!-- listings:auto:lectures-urls:start -->` 〜 — 公開 URL 一覧 |

各 `NN-slug/index.html` の `<title>` と `<meta name="description">` と `<section>` 数が抽出元。

### 使い方

```bash
# 変更を書き戻す（ローカル開発で使う）
python3 scripts/sync_listings.py --write

# ずれていないか確認（CI 用、exit 1 で fail）
python3 scripts/sync_listings.py --check
```

### 新しい講義を追加する流れ

1. `_template/` をコピーして `NN-slug/` を作る
2. `<title>` / `<meta name="description">` / スライド本文を書く
3. `python3 scripts/sync_listings.py --write` で 4 ファイルを同期
4. `git add -A && git commit && PR`

PR を上げ忘れても CI の `sync-listings-check.yml` が落とすので発見できる。
main にマージ後は念のため `sync-listings-bot.yml` が再生成する二重防衛。

### 依存

- Python 3.8+（標準ライブラリのみ。`pip install` 不要）
- `git`（lastmod の取得に使用）

### マーカー設計

各ファイルに HTML/XML コメント形式でマーカーを埋める。マーカー間の本文のみ
スクリプトが再生成し、マーカー外は触らない。

```
<!-- listings:auto:start -->
... 自動生成 ...
<!-- listings:auto:end -->
```

同じファイルに 2 か所以上ある場合は名前付きにする：

```
<!-- listings:auto:<name>:start -->
... 自動生成 ...
<!-- listings:auto:<name>:end -->
```
