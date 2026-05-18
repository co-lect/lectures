# Lecture 02 — Claude Code 環境構築

AI コーディングシリーズ 第 2 回。プランの選択からインストール・認証・初起動まで、Claude Code を動かすまでの手順を 12 枚で解説。

## このディレクトリの中身

```
02-setup/
├── index.html         ← 本体（ブラウザで開く / AI に読ませる）
└── README.md          ← このファイル
```

`index.html` は隣接する `../shared/` の以下に依存：

- `shared/deck-stage.js` — スライドナビゲーション・スケーリング・印刷を担うエンジン
- `shared/theme.css` — Anthropic 風のクリーム + テラコッタ デザインシステム

## 想定読者と読み方

| 読み手 | 使い方 |
|---|---|
| 人間（ブラウザ） | `index.html` を開く。`←` / `→` キー、Space、PgUp/PgDn でナビ。`Cmd/Ctrl + P` で PDF 出力 |
| 人間（対面） | 発表者が前で操作。スライド本体は読み物としても成立 |
| AI（Claude Code 等） | ファイルそのものを読ませると、構造化された HTML として理解される。「次のスライドを書いて」「この部分を噛み砕いて」と編集相談ができる |

## 全体構成

全 12 枚。**選択 → 手順 → 確認** の流れで構成。

### 設計方針

- **資料は「概要のみ」。** 詳細・具体は受講者が手元の AI に聞く前提
- **公式ドキュメント準拠。** インストールコマンドは `code.claude.com/docs/en/getting-started`（2026/5 時点）に基づく
- **OS 別に明示。** macOS/Linux/WSL・Windows PowerShell・Windows CMD を分けて記載
- 詳しくはルート `../CLAUDE.md` を参照

### スライド一覧

| # | チャプター | 内容 |
|---|---|---|
| 01 | — | Cover — Claude Code 環境構築 |
| 02 | — | このドキュメントの読み方 |
| 03 | Ch.1 | プランの選択 — API / Claude Pro / Claude Max |
| 04 | Ch.2 | インストール方法 — 4つの選択肢 |
| 05 | Ch.3 | Native Install — OS 別のコマンド |
| 06 | Ch.4 | 認証 — アカウントと紐づける |
| 07 | Ch.5 | 初起動 — まず挨拶してみる |
| 08 | Ch.6 | 最初の実践 — ファイルを渡してみる |
| 09 | Ch.7 | 結論 — 動かせた、それが出発点 |
| 10 | Coda | 終わりに — 次は使い方へ |
| 11 | AI Buddy | AI Buddy — セットアップで詰まった場所を共有してください |
| 12 | Credits | Credits — この資料に関わった人 |

## Authors

| 役割 | 名前 | 貢献 |
|---|---|---|
| Initial author | [@Tsubasasa1857](https://github.com/Tsubasasa1857) | 章全体の構成・執筆 |

> このセクションは PR 単位で追加されます。修正・改善した方は、PR でこの表に行を追加してください。Role に関係なく、貢献した資料に名前を入れて OK です。
