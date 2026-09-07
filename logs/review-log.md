# レビュー指摘ログ

`/review-doc` が実行のたびに追記する。振り返り（`/retro`）と3回ルールの唯一の入力データ。

## 記録ルール

1. `Critical` `High` `Medium` のみ記録する。`Low` は記録しない（ノイズになるため）。
2. カテゴリと重大度は `foundation/review-criteria.md` の固定語彙のみを使う。
3. 「指摘要約」は**類型として書く**。「第3段落が長い」ではなく「1段落に複数トピックが混在」と書く。集計できることを優先する。
4. 対応欄は、修正 PR のマージ時に `fixed` / `wontfix` に更新する。`wontfix` の場合は理由を1行添える。
5. 行を削除しない。過去の傾向が振り返りの材料になる。

## ログ

| 日付 | 対象 | 章 | カテゴリ | 重大度 | 指摘要約 | 対応 |
|---|---|---|---|---|---|---|
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Critical | デモ手順が再現できない（前提となる操作の欠落） | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | High | デモ手順に原稿外の知識の補完が必要 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 出力例が実際の出力と一致しない | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 実行のたびに変わる結果を固定の出力例として提示 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 環境依存が明示されていない | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | Critical | ツール固有の挙動を一般化して断定 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | Critical | 読む節か手を動かす節かが判別できない | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | High | 1回の実行結果から因果を断定 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | High | 見出し直下の主張文と本文が矛盾 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | paragraph | High | 1段落に複数トピックが混在 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | High | ツール固有の記述が囲みの外にある | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | High | 文体の混在（ですます調とである調） | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | High | 前提知識にない環境依存が未記載 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | High | 出力例の実物と整形の区別が不明 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 数値の数え方が原稿から再現できない | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 一文が長く主語と述語が離れている | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 指示語の指す先が一意でない | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 動作の主体が不明 | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | paragraph | Medium | 段落の要約文が末尾にある | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | paragraph | Medium | 第2文以降に新しい主張が混ざる | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | Medium | 用語集に未登録の語がある | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | Medium | 和欧文間のスペース | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 記述と出典 URL の内容が一致しない | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | Medium | 反論への言及がない | 未対応 |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | Medium | 前提知識「なし」の領域を説明せずに使用 | 未対応 |

## 集計（3回ルールの判定用）

`/review-doc` が実行末尾で更新する。同一カテゴリ・同種の指摘が3件に達したら、`backlog.md` のプロセス改善にタスクを追加する。

| カテゴリ | 指摘要約の類型 | 件数 | 状態 |
|---|---|---|---|
| fact | デモ手順が再現できない（前提となる操作の欠落） | 1 | 監視中 |
| fact | デモ手順に原稿外の知識の補完が必要 | 1 | 監視中 |
| fact | 出力例が実際の出力と一致しない | 1 | 監視中 |
| fact | 実行のたびに変わる結果を固定の出力例として提示 | 1 | 監視中 |
| fact | 環境依存が明示されていない | 1 | 監視中 |
| fact | 記述と出典 URL の内容が一致しない | 1 | 監視中 |
| logic | ツール固有の挙動を一般化して断定 | 1 | 監視中 |
| logic | 1回の実行結果から因果を断定 | 1 | 監視中 |
| logic | 見出し直下の主張文と本文が矛盾 | 1 | 監視中 |
| logic | 反論への言及がない | 1 | 監視中 |
| paragraph | 1段落に複数トピックが混在 | 1 | 監視中 |
| paragraph | 段落の要約文が末尾にある | 1 | 監視中 |
| paragraph | 第2文以降に新しい主張が混ざる | 1 | 監視中 |
| tech-writing | 数値の数え方が原稿から再現できない | 1 | 監視中 |
| tech-writing | 一文が長く主語と述語が離れている | 1 | 監視中 |
| tech-writing | 指示語の指す先が一意でない | 1 | 監視中 |
| tech-writing | 動作の主体が不明 | 1 | 監視中 |
| style | ツール固有の記述が囲みの外にある | 1 | 監視中 |
| style | 文体の混在（ですます調とである調） | 1 | 監視中 |
| style | 用語集に未登録の語がある | 1 | 監視中 |
| style | 和欧文間のスペース | 1 | 監視中 |
| audience | 読む節か手を動かす節かが判別できない | 1 | 監視中 |
| audience | 前提知識にない環境依存が未記載 | 1 | 監視中 |
| audience | 出力例の実物と整形の区別が不明 | 1 | 監視中 |
| audience | 前提知識「なし」の領域を説明せずに使用 | 1 | 監視中 |

状態: `監視中`（1〜2件） / `発火`（3件以上、改善タスク未作成） / `対応済`（改善を適用済み）
