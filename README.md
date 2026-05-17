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
| [`00-about/`](./00-about/index.html) | この資料の歩き方（Read me） | 9 枚 |
| [`01-claude-code-intro/`](./01-claude-code-intro/index.html) | Claude Code 入門 | 12 枚 |

各章は単体の HTML として完結しているので、ブラウザで開けばそのまま読めます。

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
