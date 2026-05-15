# 00 — About / Read me

このシリーズ全体の取扱説明書。「1 年で陳腐化する世界で、教材をどう作り・運用するか」という思想を 9 枚のスライドで説明します。

## このディレクトリの中身

```
00-about/
├── lecture.html       ← 本体（ブラウザで開く / AI に読ませる）
└── README.md          ← このファイル
```

`lecture.html` は隣接する `../shared/` に依存します（`deck-stage.js` / `theme.css` / `progress-strip.js`）。

## 何を説明しているか

- **課題** — AI 周辺は半年〜1 年で別物になる。PPTx は「1 回作って終わり」の前提で追いつけない
- **解決策 01** — PPTx ではなく HTML（AI が読める / Git で履歴が残る / 編集が速い）
- **解決策 02** — 詰め込まない。詳細は読者の AI に深掘りしてもらう
- **解決策 03** — Git/GitHub のエコシステム（履歴・Issue・PR・Discussions）を丸ごと使う

詳しい思想はルートの [`CLAUDE.md`](../CLAUDE.md) を参照してください。

## 関連

- [`../01-claude-code-intro/`](../01-claude-code-intro/lecture.html) — 最初の応用例（Lecture 01）

## Authors

| 役割 | 名前 | 貢献 |
|---|---|---|
| Initial author | [@watanabe-kohei-jp](https://github.com/watanabe-kohei-jp) | 資料全体の構成・執筆 |

> このセクションは PR 単位で追加されます。修正・改善した方は、PR でこの表に行を追加してください。Role に関係なく、貢献した資料に名前を入れて OK です。
