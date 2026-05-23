# Lectures — AI と人間が共同編集する教材

> 「飢えた人に魚を与えれば一日食べさせられる。<br>
> 魚の釣り方を教えれば一生食べさせられる。」

このリポジトリは **資料を配布する場所ではなく、教育・知識・技術を持続可能に運用するための実験場** です。スライドは凍結された PDF ではなく、Git で進化する HTML。受講者と AI（Claude Code 等）が一緒に読み、必要なら直接編集して PR を投げる前提で設計しています。

AI コーディング（Claude Code 等）を中心に、散在しがちな情報を 1 か所に集約した **最新の地図** になることを目指しています。

詳細な思想は [`CLAUDE.md`](./CLAUDE.md) を読んでください。

---

## 📖 今すぐ読む — 公開サイト

ブラウザでそのまま読めます。インストール不要。

**▶ <https://co-lect.github.io/lectures/>**

スマホで開くなら、この QR コードから：

<img src="shared/qr.svg" alt="lectures 公開サイトの QR コード" width="150">

---

## 何が読めるか

| 章 | 内容 | スライド |
|---|---|---|
| [`00-about/`](./00-about/index.html) | この資料の歩き方（Read me） | 10 枚 |
| [`01-claude-code-intro/`](./01-claude-code-intro/index.html) | Claude Code 入門 | 13 枚 |
| [`02-setup/`](./02-setup/index.html) | Claude Code 環境構築（プラン選び・インストール・初起動） | 12 枚 |
| [`03-claude-md/`](./03-claude-md/index.html) | `CLAUDE.md` でプロジェクトを記憶させる | 12 枚 |

各章は単体の HTML として完結しているので、ブラウザで開けばそのまま読めます。

---

## 読み進め方（推奨ルート）

「どの順番で・どの深さで読めばいいか分からない」と感じたら、次の 3 ルートから自分に合うものを選んでください。**どのルートも 25〜45 分** で初回通読できます。

### ルート A — はじめての方（30 分）

> 「Claude Code をまだ触ったことがない／聞いたことはあるけど使っていない」

1. [`00-about/`](./00-about/index.html) — **必読**。なぜこの形（HTML × Git × AI）の教材なのか、思想を 9 枚で。ここを飛ばすと以降が宙に浮きます
2. [`01-claude-code-intro/`](./01-claude-code-intro/index.html) — Claude Code とは何か、何ができるか
3. [`02-setup/`](./02-setup/index.html) — 手元にインストールして触ってみる

**ゴール**: Claude Code を自分の PC で動かして、ちょっとした質問を投げられる状態。

### ルート B — Claude Code は触っている方（25 分）

> 「日常的に使っているが、もっと深く使いこなしたい／チームに紹介したい」

1. [`00-about/`](./00-about/index.html) — このリポジトリ自体の運用思想（5 分で目を通す）
2. [`03-claude-md/`](./03-claude-md/index.html) — `CLAUDE.md` の書き方・育て方（実は最も効果がある投資）
3. ルートの [`CLAUDE.md`](./CLAUDE.md) — 本リポジトリで採用している運用ルールの実例

**ゴール**: 自分のリポジトリの `CLAUDE.md` を 1 つ書き直して、AI の挙動を狙い通りに変えられる。

### ルート C — 教材として／作り手として読む方（45 分）

> 「教育担当・社内教材を作る人・カンファレンス登壇者など、"作り方" 自体に興味がある」

1. [`00-about/`](./00-about/index.html) — 設計思想（必読）
2. [`CONTRIBUTING.md`](./CONTRIBUTING.md) — Issue / Discussion / PR の使い分け
3. [`CLAUDE.md`](./CLAUDE.md) — このリポジトリの運用方針全体
4. 任意の章を 1 つ選んで [`shared/`](./shared/) の HTML スライドエンジンを覗く

**ゴール**: 自前で同じ形式の教材を立ち上げる土台ができる。

### 読み方のスタイル（3 パターン）

ルートを選んだら、次は **どう読むか**。3 パターンあります。

#### パターン 1 — スライドだけを見る

ブラウザで `index.html` を開いて、矢印キー（`→` / `Space`）で読み進める。最短ルート。

- **向くとき**: 25 分以内でざっと全体像を掴みたい / 講義・勉強会で投影する
- **限界**: スライドは骨格と主張しか持っていない。詳細が気になっても、その場では深掘りできない

#### パターン 2 — Claude Code に読ませて、対話で読む

各章の URL（例: `https://co-lect.github.io/lectures/00-about/`）またはローカルの `index.html` パスを Claude Code に渡し、要約させる・疑問を投げる・自分の文脈に置き換えてもらう。

- **向くとき**: 視覚的なスライドより自分の課題に引き寄せて深く理解したい / 通勤中などスライド画面を見られない状況
- **限界**: スライドの "見せ方" や図表が伝える情報は、AI のテキスト要約では落ちる

#### パターン 3 — 両方（**おすすめ**）

スライドを開きつつ、隣で Claude Code を起動。**章の URL を最初に AI に渡しておき**、スライドを進めながら気になったところで質問・改善提案・自分の現場での具体例を聞く。

- **何がいいか**:
  - 図やレイアウトはスライドで（視覚情報を落とさない）
  - 詳細・自分への応用は AI で（骨格に肉付けする）
  - 読みながら出た疑問・改善案は、そのまま AI Buddy（各章末尾）経由で Discussions / Issue / PR に流せる
- **最初の一声**（コピペ用）:
  > 「これから https://co-lect.github.io/lectures/00-about/ を読みます。読み終わったら、私が詰まった点や改善提案を一緒に整理して、Issue / Discussion / PR のどれにするか提案してください。」

この 3 パターン目が **資料が読まれて終わらず、次の受講者の役に立つループ** を作る、本リポジトリの想定運用です。

### どのルートでも共通の前提

- **「読む」だけで終わらせない** — 隣に Claude Code（または Codex 等）を置いて、気になった用語はその場で深掘りしてください。スライドは骨格と主張だけしか持っていません（[`00-about/`](./00-about/index.html) の解決策 02 参照）
- **詰まったら Issue / Discussion へ** — 「ここわからない」は Discussions / Q&A、「ここ直してほしい」は Issue。詳しくは [`CONTRIBUTING.md`](./CONTRIBUTING.md)

---

## どう読むか

### 方法 1: 公開サイト（GitHub Pages）

```
https://co-lect.github.io/lectures/00-about/
https://co-lect.github.io/lectures/01-claude-code-intro/
```

### 方法 2: クローンしてローカルで開く

```bash
git clone https://github.com/co-lect/lectures
cd lectures
# ブラウザで 00-about/index.html を開く
```

### 操作

| キー | 動作 |
|---|---|
| `→` / `Space` | 次のスライド |
| `←` | 前のスライド |
| `R` | 最初に戻る |
| `F` | フルスクリーン |
| `S` | スピーカーノート（あれば） |

---

## 完全版（1 ファイル）を入手する

各章を 1 つの HTML にまとめた「完全版」が用意されています。`shared/` の CSS・JS と画像をすべて埋め込むので、**リポジトリもネット接続もなしで開けます**。メール添付・USB 配布・オフライン閲覧に。

### 方法 1: ダウンロードする（推奨）

CI が自動更新する常に最新版を Pages から取得できます。

```
https://co-lect.github.io/lectures/dist/00-about.html
https://co-lect.github.io/lectures/dist/01-claude-code-intro.html
https://co-lect.github.io/lectures/dist/02-setup.html
https://co-lect.github.io/lectures/dist/03-claude-md.html
```

ブラウザで開いて右クリック →「名前を付けて保存」で `.html` 1 ファイルが手元に残ります。

### 方法 2: 自分でビルドする

```bash
python build.py
```

`dist/00-about.html` などが生成されます（`dist/` は git 管理外のビルド成果物）。依存は Python 3 標準ライブラリのみ。

### 注意

- `dist/` は **ビルドの度に上書きされる**。直接編集しないこと
- 配布前は **必ず `python build.py` を実行**するか、Pages の最新版を取得する
- `dist/` は git 管理外（`.gitignore` 設定済み）。`git add -f` で強制追加しないこと

> Web フォント（Google Fonts）だけは埋め込みません。完全オフラインではシステムフォントにフォールバックします（レイアウトは崩れません）。

---

## 一緒に作る — 貢献の入口

このリポジトリは **教える側と教わる側の境界をゆるくする** ことを意図しています。受講者も貢献者です。

| 入口 | 何を |
|---|---|
| **Issue** | 詰まった点、誤りの指摘、改善提案 |
| **Discussion** | 学習ログ、応用事例、質問 |
| **Pull Request** | 直接の修正・追加 |

### AI Buddy

各章の末尾には **AI Buddy** スライドがあります。受講者の AI（Claude Code 等）にそのスライドを渡すと、AI が「詰まった点を Issue にしますか？」「気づきを Discussion にしますか？」と提案してくれます。

**必ず受講者本人の同意を取り、個人情報を匿名化する** ことを AI に求めるプロトコルなので、無断投稿は起きません。

詳しくは各章末スライド、または [`CLAUDE.md`](./CLAUDE.md) を参照してください。

### 貢献者の名前は残る

PR で資料を直した人の名前は、その章の Credits スライド・章の `README.md`・GitHub の履歴に永続的に残ります。継続的に貢献する人には Role（Contributor / Core Contributor / Maintainer）がつき、[`CONTRIBUTORS.md`](./CONTRIBUTORS.md) に掲載されます。

これは「ノウハウを分かりやすく人に伝えられる」ことの、公開された証跡になります。Role の意味と推薦方法は [`CONTRIBUTING.md`](./CONTRIBUTING.md) を参照してください。

---

## このリポジトリの不変条件

- **AI に伝わる内容は人間にも見える** — hidden な AI 向け命令は禁止（`.github/workflows/prompt-injection-check.yml` で CI 強制）
- **概要のみ、詳細は読者の AI へ** — スライドは骨格と主張だけ。詳細は受講者が手元の AI に質問する前提
- **更新される前提で設計** — AI 周辺は移り変わりが激しい。古くなる前提で書き、PR で直し続ける

---

## 鮮度について

AI 周辺は変化が速く、この資料も古くなります。だからこそ次の約束で運用します。

- **数字・主張には as-of 日付を付ける** — 例：「2026/4 時点」。出典も併記し、後から辿れるようにする
- **正本の「最終更新」は Git の履歴** — 誰が・いつ・何を変えたかは `git log` が答え
- **最新の詳細は読者の AI に聞く前提** — スライドは骨格と主張だけを持つ。細部は陳腐化するので抱え込まない

古い記述・誤りを見つけたら、Issue か PR で直してください。直し続けることがこの資料の前提です。

---

## ライセンス

このリポジトリのコンテンツは **[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)** で公開されています（[LICENSE](./LICENSE) 参照）。

| 利用 | 可否 |
|---|---|
| 商用利用 | ◎ |
| 改変 | ◎ |
| 再配布 | ◎ |
| 派生物に同条件を強制 | 不要 |
| クレジット表記 | **必須**（下記の attribution 例を参照）|

### 引用・再利用時の attribution 例

スライドの一部を別の資料で使う、講義に組み込む、改変して公開する — どの場合も以下の形でクレジットを残してください。

```
"Lectures" (https://github.com/co-lect/lectures)
by @watanabe-kohei-jp, licensed under CC BY 4.0.
（必要に応じて）Modified from the original / 改変あり
```

3 要素を含めれば書式は問いません：**① 作者（GitHub アカウント名 or 個人で名乗っている名前）** / **② CC BY 4.0 へのリンク or 明示** / **③ オリジナルへのリンク**。改変している場合は「改変あり」も追加。

サードパーティ素材の出典は [`CREDITS.md`](./CREDITS.md) を参照してください。

---

## 名前・ブランドについて

コンテンツは CC-BY-4.0 で自由に使えますが、**プロジェクト名・ロゴ・ブランドは CC ライセンスの対象外**です（CC ライセンスは商標を許諾しません）。

フォークや派生物を公開するときは：

- 原典（このリポジトリ）へのリンクを残してください
- 本家を騙ったり、本家と紛らわしい名前を名乗らないでください
- 改変したものを「公式」と称さないでください

CC-BY-4.0 が保証する自由（商用利用・改変・再配布）はそのまま尊重します。上記は「どれが原典か」を読者が判断できるようにするためのお願いです。

---

## メンテナ

[@watanabe-kohei-jp](https://github.com/watanabe-kohei-jp)

---

## 関連

- [`CLAUDE.md`](./CLAUDE.md) — このリポジトリの運用方針（AI 向け / 人間向け両方）
- [`CONTRIBUTING.md`](./CONTRIBUTING.md) — 貢献ガイド（Issue / Discussion / PR の使い分け）
- [`CREDITS.md`](./CREDITS.md) — サードパーティ素材の出典
- [`shared/`](./shared/) — HTML スライドエンジン（`deck-stage.js`）とデザインシステム（`theme.css`）
