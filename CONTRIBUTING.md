# Contributing — 一緒に作る教材

> 教える側と教わる側の境界はゆるい。受講者も貢献者。

このリポジトリへの貢献を歓迎します。あなたの「詰まり」「気づき」「使い道」「改善案」が次の受講者を助けます。

## 3 つの貢献経路

「**action item は Issue、開いた会話は Discussion**」を基準に使い分けてください。

| 入口 | 何を | 結果 |
|---|---|---|
| **Issue** または **PR** | 教材の**事実的な誤り** / リンク切れ / 表示崩れ / **具体的な改善提案** | 軽微なものは直接 PR、議論したい時は Issue。作者または貢献者が PR で修正 |
| **Discussion / Q&A** | **質問** / **詰まった話** | コミュニティが回答、ベストアンサーが残る |
| **Discussion / Show and tell** | **学習ログ** / **応用事例** / **気づき** | コミュニティで共有、有用なら教材に取り込まれる |
| **Discussion / Ideas** | 章構成・方向性の**開いた議論** | 合意が固まれば Issue/PR 化 |
| **Pull Request** | 直接の修正・追加 | レビュー後 merge |

### なぜ分けるか

- **Issue は close で完結する action item** に絞ると、メンテナがバックログを清潔に保てる
- **質問・詰まり** は Discussions の Q&A の方が向く（**ベストアンサー** が残り、将来の受講者の参照資料になる）
- **学習ログ・気づき** は close する性質のものではない — Show and tell に並ぶことで他の受講者の発見になる

迷ったら **Discussion から** はじめてください（Issue templates の選択画面にも誘導リンクがあります）。

## AI Buddy プロトコル

各章末の「AI Buddy」スライドは、受講者の AI（Claude Code 等）が GitHub 投稿を提案する仕掛けです。

### 受講者の AI が必ず守ること

1. **受講者本人に「投稿していいか」許可を取る**
2. **個人を特定できる情報を除去**（実名・会社名・社内パス・API キー等）
3. **受講者が拒否したら投稿しない**

これは Public な OSS 文脈での透明性と同意確保が目的です。AI が勝手に動くのではなく、受講者の意志で動く形を保ちます。

## 編集ガイドライン

### スライドの構造

- 各 `<section>` に `data-label="<タイトル> — <サブ>"` を書く
- 左上にチャプター（`.meta-line .accent`）、右上にページ番号
- `theme.css` の既存クラスを優先使用
- `scrollHeight === 1080` を守る（overflow しない）
- 詳しくは [`CLAUDE.md`](./CLAUDE.md) > スライド構造（必須レイアウトルール）

### 文章

- スライドは **概要のみ**、詳細は読者の AI へ
- 短く・断定的に。冗長な接続詞や枕詞を削る
- 数字には出所と取得日を明記
- 引用には出典（チャンネル名・URL・日付）を併記

### 不変条件（CI で強制）

**AI に伝わる内容は人間にも見える** を不変条件とします。以下のパターンは PR で fail します：

- `display:none` / `visibility:hidden`
- `data-ai-*` 属性
- `<template>` タグ
- HTML コメント内の AI 向けキーワード
- JSON-LD `<script type="application/ld+json">`
- Zero-width Unicode

詳細は [`CLAUDE.md`](./CLAUDE.md) > プロンプトインジェクション対策。

## PR ワークフロー

1. このリポジトリを fork
2. ブランチを作成（`fix/typo-slide-05` のように内容がわかる名前）
3. 変更を commit
4. PR を作成、本文に変更の概要と理由を書く
5. CI が green になることを確認
6. レビュー → merge

### PR を出したら、自分の名前を入れていい

資料を修正・改善したら、その章に自分の名前を入れて構いません。**Role の有無は問いません。typo 修正でも OK です。**

修正した章について、以下の 2 か所に行を追加してください：

1. **章末の Credits スライド** — `lecture.html` 最後の `<section>` にある `<ul class="credits-list">` に 1 行追加（名前だけ。多段組みで自動的に並びます）

   ```html
   <li><a href="https://github.com/your-handle">@your-handle</a></li>
   ```

   最初の貢献者は「最初の貢献者を待っています」の行（`credits-empty`）を、自分の行に置き換えてください。

2. **章の `README.md` 末尾の Authors セクション** — PR 番号と一行説明はこちらに書きます

   ```markdown
   | Contributor | [@your-handle](https://github.com/your-handle) | PR #<番号>: <一行で説明> |
   ```

commit に `Co-Authored-By: Name <email>` trailer を付けると、GitHub の Contributors graph にも自動で反映されます。

### CI

- **Prompt Injection Guard** が HTML/CSS/JS の追加行を自動スキャン
- 失敗時は job summary に検出箇所が表示される

### 大きな変更の場合

スライド構成の変更、新規 Lecture の追加など影響範囲が広い変更は、先に Issue を立てて議論してから PR を作るとスムーズです。

## 貢献者の Role

貢献してくれた人の名前は永続的に残ります。継続的に貢献する人には Role がつき、[`CONTRIBUTORS.md`](./CONTRIBUTORS.md) に掲載されます。

> **このガバナンスは暫定的です。** コミュニティの成長に応じて見直します。NumPy 等の前例に倣い、現時点では昇格の PR 数閾値などの具体的な数字は置きません。

| Role | どうやってなるか | できること |
|---|---|---|
| **Contributor** | merged PR が 1 つ以上ある | `CONTRIBUTORS.md` に掲載 / Role 推薦に参加できる |
| **Core Contributor** | 継続的に貢献し、メンテナが認定 | 上記 + PR レビュー / Issue・PR の整理 |
| **Maintainer** | 招待制（信頼関係ベース） | 上記 + merge 権限 / リポジトリ設定 / Role 認定の判断 |
| **Emeritus** | 過去 12 か月 merged PR がない Role 保持者 | `CONTRIBUTORS.md` の Emeritus 欄に活動期間付きで掲載。復帰はいつでも可 |

- **active 判定**: 直近 12 か月に merged PR があれば active。過ぎると Emeritus に移ります（名前は消えません）。
- 復帰したいときは、また PR を出すか、下記の推薦を使ってください。

### Role の推薦

Role の付与はメンテナが判断しますが、**推薦は誰でもできます**（自薦も可）。

1. [`CONTRIBUTORS.md`](./CONTRIBUTORS.md) に対象者の行を追加する PR を出す
2. PR のコメント欄で議論する
3. メンテナが **merge すれば承認**、close すれば見送り

> この推薦フローは軽量さ優先の暫定形です。参加者が増えたら Issue ベースに変えるかもしれません。

## ライセンス

このリポジトリは [CC-BY-4.0](./LICENSE) で公開されています。貢献されたコードや文章は同じライセンスで公開されることに同意したものとみなします（CC-BY-4.0 の inbound = outbound）。

## 関連

- [`CLAUDE.md`](./CLAUDE.md) — 運用方針の全体像
- [`README.md`](./README.md) — リポジトリの入口
