# Lecture 01 — なぜ今、Claude Code を学ぶのか

AI コーディングシリーズ 第 1 回。Claude Code を中心に、Git/GitHub・Issue/PR・MCP・worktree までを扱う 6〜7 回シリーズの入口。

## このディレクトリの中身

```
01-claude-code-intro/
├── lecture.html       ← 本体（ブラウザで開く / AI に読ませる）
├── README.md          ← このファイル
└── _assets/           ← 図・スクショ（必要時）
```

`lecture.html` は隣接する `../shared/` の以下に依存：

- `shared/deck-stage.js` — スライドナビゲーション・スケーリング・印刷を担うエンジン
- `shared/theme.css` — Anthropic 風のクリーム + テラコッタ デザインシステム

## 想定読者と読み方

| 読み手 | 使い方 |
|---|---|
| 人間（ブラウザ） | `lecture.html` を開く。`←` / `→` キー、Space、PgUp/PgDn でナビ。`Cmd/Ctrl + P` で PDF 出力 |
| 人間（対面） | 発表者が前で操作。スライド本体は読み物としても成立 |
| AI（Claude Code/Codex） | ファイルそのものを読ませると、構造化された HTML として理解される。「次のスライドを書いて」「この部分を噛み砕いて」と編集相談ができる |

## 全体構成

全 11 枚。**主張 → 具体理由** の流れで構成、「PC を AI が操作する道具」フレームに統一。

### 設計方針

- **資料は「概要のみ」。** 詳細・具体は受講者が手元の AI（Claude Code 等）に聞く前提
- **HTML で書く。** 人間と AI が一緒に読み、AI が編集もできる "生きた資料"
- **主張先行。** 「誰の話か」を最初に置き、歴史・具体例は補強として後ろに置く
- **PC 操作フレーム。** Claude Code は単なるコーディング道具ではなく「AI が PC を操作する道具」
- 詳しくはルート `../CLAUDE.md` を参照

### スライド一覧

| # | チャプター | 内容 |
|---|---|---|
| 01 | — | Cover — なぜ今、Claude Code を学ぶのか |
| 02 | — | このドキュメントの読み方 |
| 03 | Ch.1 | Claude と Claude Code — 粒度が違う |
| 04 | Ch.2 | どの Claude Code か — CLI 版に絞る |
| 05 | Ch.3 | PC で働く AI — Claude Code の正体 |
| 06 | Ch.4 | 立ち位置の変化 — 「PC を操作する人」から「指示する人」へ |
| 07 | Ch.5 | 何ができるか — 8 領域で MECE に |
| 08 | Ch.6 | 実績 — 普及している、本当に |
| 09 | Ch.7 | 結論 — 数年後、これが標準になる |
| 10 | Coda | 終わりに — 続きは触ってから |
| 11 | AI Buddy | AI Buddy — 一緒に育てる（受講者の AI に GitHub 貢献を提案するプロトコル） |

### 関連

- ルート `../00-about/lecture.html` — このシリーズ全体の **取説・Read.me**（持続可能な運用思想）

数字の出所は Anthropic 公式・Bloomberg・SaaStr・VentureBeat 等の公開報道（2026/4 時点）。後続の回が固まったら数字も更新する。

## シリーズ全体の暫定マップ

| # | テーマ | 主役 |
|---|---|---|
| **01** | AI コーディング進化史 / なぜ Claude Code か | （動機づけ・読み物） |
| 02 | Claude Code 環境構築 + 最初の対話 | Claude Code |
| 03 | Git/GitHub 概念 + AI に commit/push を任せる | + Git/GitHub |
| 04 | Issue → Branch → PR → Merge を AI に任せる | + GitHub Flow |
| 05 | MCP とは / Codex を MCP 経由で呼ぶ | + MCP |
| 06 | worktree でマルチエージェント並列開発 | + 並列実行 |
| 07 | 実プロジェクトでの運用ノウハウ（暫定） | 統合 |

## 関連

- ルート `../00-about/lecture.html` — このシリーズ全体の取説・Read me
