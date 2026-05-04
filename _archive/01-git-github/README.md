# Lecture 01 — AI ネイティブ世代の Git / GitHub 入門

大学の同期・後輩 5 名向け、90 分対面のハンズオン講義。第 1 回。

## 構成

```
01-git-github/
├── slides/
│   └── lecture01.pptx          ← Claude Design からエクスポート（39 枚版）
├── handson/
│   ├── Asan/                   ← デモ用 clone（pbl-git-warmup）
│   └── Bsan/                   ← デモ用 clone（pbl-git-warmup）
├── plan.md                     ← Claude Plan モードで書いた当初の追加プラン
├── source-structure.md         ← スライド構成（旧 39 枚 → 新 36 枚への組み直し設計）
└── README.md                   ← このファイル
```

## 関連リソース

- **練習用リポジトリ**: <https://github.com/ko-dhinngumuzuiyoo/pbl-git-warmup>
- **本番リポジトリ**: <https://github.com/ko-dhinngumuzuiyoo/PBL>
- **Claude Design Slide deck**: <https://claude.ai/design/p/38d0372e-0b81-4ded-82a7-cb485865a1e3>
- **Claude Design Design system**: <https://claude.ai/design/p/c707154d-a467-41a9-bff2-b26cfaacfc73>

## 講義の方針

| 軸 | 内容 |
|---|---|
| 聴衆 | 大学の同期・後輩 5 名（CLI 未経験前提） |
| 時間 | 90 分・対面 |
| ゴール | ① Git/GitHub の必要性を体感 ② 実際に触る ③ AI 時代の使い方を知る |
| トーン | 静か・知的（OpenAI / Anthropic 風）、白基調＋テラコッタ |
| アナロジー | Word vs Google Drive のみ（ドラクエは没にした） |

## ハンズオンの設計

受講者は基本操作（clone / 自分のファイル commit & push）まで。
コンフリクトの実演は発表者が `handson/Asan` と `handson/Bsan` を使って前で見せる。

実演の流れ（既に動作確認済み）：
1. `Asan` で README 編集 → commit → push（成功）
2. `Bsan` で同じ行を別の内容で編集 → commit → push（**rejected**）
3. `Bsan` で pull → コンフリクト発生（マーカー出現）
4. 両方の変更を残す形で解決 → commit → push
5. `git log --oneline --graph` で Y 字のマージグラフを見せる

## TODO（次回までに）

- [ ] PPTx の構成組み直し（旧 39 枚 → 新 36 枚、`source-structure.md` 参照）
- [ ] 受講者 5 名を `pbl-git-warmup` の Collaborator に招待
- [ ] コンフリクト実演のリハーサル（事前に 1 回通しておく）
- [ ] Claude Code セットアップを案内（次回までの宿題）

## シリーズ計画（暫定）

| 回 | テーマ |
|---|---|
| 01 | Git / GitHub 入門（今回） |
| 02 | ブランチ / Pull Request / AI に任せる |
| 03 | Claude Code 実践（コード書き） |
