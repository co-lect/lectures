# Credits

このリポジトリで使用しているサードパーティ素材・生成物の出典と利用条件を記録します。
**本リポジトリ全体は [CC-BY-4.0](./LICENSE) です** — このファイルは「全体ライセンスに加えて、個別素材ごとの追加情報」を示します。

---

## 画像・アイコン

### Lecture 01 — Chapter 5「何ができるか」の 8 領域アイコン

| ファイル | 用途 | 出典 |
|---|---|---|
| `01-claude-code-intro/_assets/use-research.png` | リサーチ | OpenAI（GPT 画像生成）|
| `01-claude-code-intro/_assets/use-code.png` | コーディング・データ処理 | OpenAI（GPT 画像生成）|
| `01-claude-code-intro/_assets/use-automation.png` | 自動化 | OpenAI（GPT 画像生成）|
| `01-claude-code-intro/_assets/use-doc.png` | 文書作成 | OpenAI（GPT 画像生成）|
| `01-claude-code-intro/_assets/use-slide.png` | スライド・図表 | OpenAI（GPT 画像生成）|
| `01-claude-code-intro/_assets/use-creative.png` | クリエイティブ | OpenAI（GPT 画像生成）|
| `01-claude-code-intro/_assets/use-comm.png` | 連絡管理 | OpenAI（GPT 画像生成）|
| `01-claude-code-intro/_assets/use-learn.png` | 勉強・研究 | OpenAI（GPT 画像生成）|

- 生成日: 2026 年 4–5 月
- 生成元: 作者がプロンプトを与え OpenAI のモデルで生成。`_split-icons.py` で 2×2 グリッドの原本を 4 つに分割し、テラコッタ＋クリームのテーマに合わせた線画スタイルでサイズ統一。
- 権利: OpenAI の利用規約上、生成物の所有・商用利用権はプロンプトを与えたユーザー（本リポジトリのメンテナ (@watanabe-kohei-jp)）に帰属。本リポジトリのライセンスに従い再配布可能。

---

## フォント

スライドは Web フォントを使用しています（CSS 内 `@import` または `link rel=stylesheet`）。

| ファミリー | 用途 | ライセンス |
|---|---|---|
| **Source Serif 4** | 見出し・本文セリフ | [SIL Open Font License 1.1](https://github.com/adobe-fonts/source-serif/blob/main/LICENSE.md) |
| **Inter** | サンセリフ補助 | [SIL Open Font License 1.1](https://github.com/rsms/inter/blob/master/LICENSE.txt) |
| **Noto Sans JP** | 日本語 | [SIL Open Font License 1.1](https://fonts.google.com/noto/specimen/Noto+Sans+JP/license) |

いずれも商用利用・改変・再配布可。フォント自体は本リポジトリには同梱しておらず、ブラウザが Google Fonts 等から都度読み込みます。

---

## コード

| ファイル | 内容 | ライセンス |
|---|---|---|
| `shared/deck-stage.js` | スライドナビゲーション・スケーリング | 本リポジトリのメンテナ (@watanabe-kohei-jp)の自作 / CC BY 4.0 |
| `shared/progress-strip.js` | プログレスバー注入 | 同上 |
| `shared/theme.css` | デザインシステム | 同上 |
| `01-claude-code-intro/_assets/_split-icons.py` | 2×2 グリッド画像の分割ヘルパー | 同上 |

---

## 引用したデータ・情報源

スライド内で参照している統計・実績数値は以下の出典です（2026/4 時点）。スライドはあくまで概要なので、最新情報は出典側で確認してください。

- Anthropic 公式発表 — ARR / 企業導入実績
- Bloomberg — 評価額・採用企業ニュース
- SaaStr — エンタープライズ Claude 採用
- VentureBeat — 開発ツール市場動向

---

## 追加・修正

新しい素材を加えた人は、このファイルにも 1 行加えてください。
不明な点があれば [Discussions](https://github.com/co-lect/lectures/discussions) で相談してください。
