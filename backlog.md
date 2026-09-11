# Backlog

タスク管理はこのファイルに集約する。運用ルールは `CLAUDE.md` を参照。

## In Progress

作業中のタスクを1〜2件だけ書く。ブランチ名を併記する。

- 3章のアウトライン設計 (branch: outline/ch03)

## 教材

### 準備（Phase 1）

- [x] 受講者像の確定 — `foundation/audience.md` の未確定項目を埋める (PR #1)
- [x] 全体の学習目標の決定 — `foundation/curriculum.md` (PR #3)
- [x] 章立ての設計 — `foundation/curriculum.md`、確定後にこのファイルへ展開 (PR #6)
- [x] エージェントの正式表記を決める — `glossary.md`。「AIエージェント」「コーディングエージェント」「エージェント」が混在している。1章の執筆前に確定する (PR #9)
- [x] ツール系の出典を台帳に追加する — `sources/references.md`。`CLAUDE.md` と skills は原則2にかかる。1章の執筆前に確定する (PR #10)

### 章

`foundation/curriculum.md`「章立て」から展開した。

**節は、その章のアウトラインが合意できた時点で展開する。** 節構成は `/outline` で変わりうるため、先に写すと二重管理になる。展開の書式は次のとおり。

```markdown
- [ ] N章 タイトル
  - [x] アウトライン設計 (PR #NN)
  - [ ] M節 タイトル — ドラフト執筆
  - [ ] M節 タイトル — レビュー反映
  - [ ] 章の振り返り
```

- [x] 0章 はじめに（教材の冒頭） (PR #24)
- [x] 1章 コーディングエージェントを使った開発
  - [x] アウトライン設計 (PR #11)
  - [x] 2節 デモ: エージェントに小さな変更を任せる — ドラフト執筆 (PR #13)
  - [x] 2節 デモ: エージェントに小さな変更を任せる — レビュー反映 (PR #13)
  - [x] 1節 チャットとエージェントは何が違うか — ドラフト執筆 (PR #14)
  - [x] 1節 チャットとエージェントは何が違うか — レビュー反映 (PR #14)
  - [x] 3節 自分の環境で再現する — ドラフト執筆 (PR #16)
  - [x] 3節 自分の環境で再現する — レビュー反映 (PR #16)
  - [x] 章の振り返り
  - [x] 章の README を作る — `docs/01-coding-agent/README.md` (PR #25)
- [x] 2章 コーディングだけ速くしても全体は速くならない
  - [x] アウトライン設計 (PR #26)
  - [x] 1節 速くなったのはどこか — ドラフト執筆 (PR #27)
  - [x] 1節 速くなったのはどこか — レビュー反映 (PR #27)
  - [x] 2節 AIは増幅器である — ドラフト執筆 (PR #28)
  - [x] 2節 AIは増幅器である — レビュー反映 (PR #28)
  - [x] 3節 この教材の残りが何をするか — ドラフト執筆
  - [x] 3節 この教材の残りが何をするか — レビュー反映 (PR #34)
  - [x] 章の振り返り
- [ ] 3章 スモールバッチとコンテキスト
  - [x] アウトライン設計
  - [ ] 1節 タスクを分割する — ドラフト執筆
  - [ ] 1節 タスクを分割する — レビュー反映
  - [ ] 2節 コンテキストを渡す — ドラフト執筆
  - [ ] 2節 コンテキストを渡す — レビュー反映
  - [ ] 3節 文書の品質が出力を決める — ドラフト執筆
  - [ ] 3節 文書の品質が出力を決める — レビュー反映
  - [ ] 4節 デモ: 文書が整ったリポジトリと整っていないリポジトリ — ドラフト執筆
  - [ ] 4節 デモ: 文書が整ったリポジトリと整っていないリポジトリ — レビュー反映
  - [ ] 章の振り返り
- [ ] 4章 人による確認
- [ ] 5章 バージョン管理とテスト自動化
- [ ] 6章 継続的インテグレーション
- [ ] 7章 継続的デリバリー
- [ ] 8章 ボトルネックを探す
- [ ] 9章 組織に働きかける

**着手順は章番号順ではない。** 最初に執筆するのは1章2節（デモ）である（`curriculum.md`「執筆の開始点」）。

## プロセス改善

振り返り（`/retro`）と3回ルールから積まれる。適用は `process/` ブランチで行う。

- [x] 用語集を変えた PR で、既存の節への影響を洗い出す手順を追加する — `foundation/glossary.md` の運用ルール（ret-ch02 P1）
- [x] 書き込みとプッシュの前に状態を確認する手順を追加する — `CLAUDE.md`（ret-ch02 P4・P5）
- [x] マージ済みのローカルブランチを削除する手順を追加する — `CLAUDE.md`「タスク管理」（ret-ch02、人の体感）
- [x] 応答の長さに上限を設ける — `CLAUDE.md`（ret-phase-0-1 P1） (PR #5)
- [x] 大きな文書の起案前に構成の合意を必須にする — `CLAUDE.md`（ret-phase-0-1 P1・P2） (PR #5)
- [x] `foundation/` の各文書に責務を1行で明記する — 各 foundation 文書（ret-phase-0-1 P2） (PR #5)
- [x] 最初の章は最小の1節から始め、仕組みを先に検証する — 章立ての設計時（ret-phase-0-1 P3） (PR #5)
- [x] マージ後のバックログ更新の担当とタイミングを定義する — `CLAUDE.md`（ret-phase-0-1 P4） (PR #5)
- [x] タスクと PR の粒度に目安を設ける — `CLAUDE.md`（ret-phase-0-1 P1 のレビューで派生） (PR #5)
- [x] `curriculum.md` を「決定」と「判断の記録」の2部に分ける — `foundation/curriculum.md`（PR #6 のレビューで派生） (PR #7)
- [x] 本文で強調記法を使わない規約を追加する — `foundation/style-guide.md`・`.claude/agents/style-reviewer.md`（1章2節のドラフトのレビューで派生） (PR #12)
- [x] 箇条書きは番号付きを既定にする規約を追加する — `foundation/style-guide.md`・`.claude/agents/style-reviewer.md`（1章1節のレビュー後に指摘） (PR #15)
- [x] 応答が長くなる場合に分割を提案する規約を追加する — `CLAUDE.md`「応答の作法」（ret-ch01 P1） (PR #18)
- [x] 複数の指摘に回答するときは1件ずつ返す規約を追加する — `CLAUDE.md`「応答の作法」（ret-ch01 P1） (PR #18)
- [x] foundation から変更理由を出し、コミットメッセージに移す — `foundation/curriculum.md`・`glossary.md`・`style-guide.md`。理由が3か所に重複しており、curriculum.md の第2部だけで5304字あった
- [x] 同語反復と抽象名詞の主語を避ける項目を追加する — `foundation/style-guide.md`「2. テクニカルライティング」（ret-ch01 P2）
- [x] 日本語としての自然さを見る観点を追加する — `.claude/agents/writing-reviewer.md`（ret-ch01 P2）
- [x] 環境が整っていない状態からの検証を求める — `.claude/commands/verify-demo.md`（ret-ch01 P3）
- [x] 章の執筆前に表記の規約を点検する手順を追加する — `.claude/commands/outline.md`（ret-ch01 P4）
- [x] 振り返りの反映先の一覧に `CLAUDE.md` を加える — `retrospectives/README.md`・`.claude/commands/retro.md`（ret-ch01）
- [x] 【3回ルール】1段落1トピックを執筆中に確かめる仕組みを作る — `.claude/commands/draft.md`。`paragraph`「1段落に複数トピックが混在」が3件目
- [x] 【3回ルール】拾い読みテストを執筆後ではなく執筆中に行わせる — `.claude/commands/draft.md`。`paragraph`「段落の要約文が末尾にある」が3件目
- [x] 【3回ルール】段落の第1文で指示語を使わない規約を追加する — `foundation/style-guide.md`。`tech-writing`「指示語の指す先が一意でない」が3件目
- [x] 【3回ルール】専門用語は本文で使う前に用語集へ登録する手順を作る — `.claude/commands/draft.md`・`foundation/glossary.md`。`style`「用語集に未登録の語がある」が3件目
- [x] 節全体がツール固有になる節の書き方を規約にする — `foundation/style-guide.md`「5. ツール固有の記述」。個々の記述を囲みに入れる前提しかなく、1章3節のような節を冒頭の一括宣言で扱う形式が未規定（1章3節のレビューで派生）
- [x] `curriculum.md` の1章の節構成から4節を削除する — `foundation/curriculum.md`。アウトライン設計で削除に合意したが、`curriculum.md` に「4. エージェントがうまくいかないところ」が残っている（1章1節の執筆で発見）
- [x] `demo_verified` の書式を1か所に統一する — `foundation/style-guide.md`「6. frontmatter」と `.claude/commands/verify-demo.md`「5.」で書式が食い違っている（1章2節の指摘反映で派生）
- [x] `/verify-demo` に `demo_source` と原稿のコードブロックの突き合わせを追加する — `.claude/commands/verify-demo.md`。題材のファイルを正とする運用を機械的に守らせる（1章2節の指摘反映で派生）
- [x] 和欧文間スペースのルールと例を一致させる — `foundation/style-guide.md`。「3. 表記」は「入れない」と定め、「5. ツール固有の記述」のテンプレート例は入れている（1章2節のレビューで派生）
