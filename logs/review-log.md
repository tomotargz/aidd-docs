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
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Critical | デモ手順が再現できない（前提となる操作の欠落） | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | High | デモ手順に原稿外の知識の補完が必要 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 出力例が実際の出力と一致しない | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 実行のたびに変わる結果を固定の出力例として提示 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 環境依存が明示されていない | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | Critical | ツール固有の挙動を一般化して断定 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | Critical | 読む節か手を動かす節かが判別できない | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | High | 1回の実行結果から因果を断定 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | High | 見出し直下の主張文と本文が矛盾 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | paragraph | High | 1段落に複数トピックが混在 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | High | ツール固有の記述が囲みの外にある | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | High | 文体の混在（ですます調とである調） | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | High | 前提知識にない環境依存が未記載 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | High | 出力例の実物と整形の区別が不明 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 数値の数え方が原稿から再現できない | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 一文が長く主語と述語が離れている | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 指示語の指す先が一意でない | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | tech-writing | Medium | 動作の主体が不明 | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | paragraph | Medium | 段落の要約文が末尾にある | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | paragraph | Medium | 第2文以降に新しい主張が混ざる | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | Medium | 用語集に未登録の語がある | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | style | Medium | 和欧文間のスペース | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | fact | Medium | 記述と出典 URL の内容が一致しない | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | logic | Medium | 反論への言及がない | fixed |
| 2026-09-04 | docs/01-coding-agent/02-demo.md | 1-2 | audience | Medium | 前提知識「なし」の領域を説明せずに使用 | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | fact | Critical | 出典のない断定が一次情報と食い違う | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | logic | Critical | 同じ章の別の節と矛盾する断定 | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | logic | High | 条件を落とした断定が後の章の主張と逆を向く | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | paragraph | High | 段落の第1文が予告文で内容を含まない | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | paragraph | High | 1段落に複数トピックが混在 | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | audience | High | 受講者の主要な不安に受け皿も予告もない | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | style | Medium | 同一概念に複数の呼び名 | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | style | Medium | 省略形を定義より前に使用 | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | style | Medium | 用語集に未登録の語がある | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | paragraph | Medium | 段落の要約文が末尾にある | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | tech-writing | Medium | 一文が長く主語と述語が離れている | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | tech-writing | Medium | 指示語の指す先が一意でない | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | audience | Medium | 数え方が前後で一致しない | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | audience | Medium | 節の導入がなく読む目的が示されない | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | audience | Medium | 後の章に持ち越す論点の予告がない | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | logic | Medium | 主張が定義の言い換えにとどまる | fixed |
| 2026-09-07 | docs/01-coding-agent/01-chat-vs-agent.md | 1-1 | fact | Medium | 記述と出典 URL の内容が一致しない | fixed |
| 2026-09-07 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | Critical | デモ手順が再現できない（前提となる操作の欠落） | fixed |
| 2026-09-07 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | High | デモ手順に原稿外の知識の補完が必要 | fixed |
| 2026-09-07 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | Medium | 出力例が実際の出力と一致しない | fixed |
| 2026-09-07 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | Medium | 画面表示を示さずに確認を求めている | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | Critical | 環境依存が明示されていない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Critical | 用語集に未登録の語がある | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | High | 一次情報より広い範囲で断定 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | High | 機能が働く条件が抜けている | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | High | 安全機構の範囲を実際より広く記述 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | High | 章の主張を回収していない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | High | 見出し直下の主張文と本文が矛盾 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | High | 提示した因果が後段で回収されない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | paragraph | High | 見出し直下に主張文がない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | paragraph | High | 1段落に複数トピックが混在 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | High | 使用禁止の別表記を使用 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 操作の前後関係が書かれていない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 前の手順の結果により次の手順を試せない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 画面表示の読み方が説明されていない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 予告した操作が渡されない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | Medium | 実行記録であることと省略の方針が未記載 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | Medium | 根拠のない数値 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | Medium | 前の節の予告が回収されていない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | paragraph | Medium | 段落の要約文が末尾にある | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 曖昧語を使用 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 並列が文法的に揃っていない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 指示語の指す先が一意でない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 主語と述語がねじれている | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 動作の主体が不明 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | 同一概念に複数の呼び名 | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | ツール固有の記述が囲みの外にある | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | 表記の大文字小文字の揺れ | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | 題材の名前が節をまたいで揃っていない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | Medium | 完了条件が示されていない | 未対応 |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | Medium | 環境によって手順が変わる箇所が未記載 | 未対応 |

## 集計（3回ルールの判定用）

`/review-doc` が実行末尾で更新する。同一カテゴリ・同種の指摘が3件に達したら、`backlog.md` のプロセス改善にタスクを追加する。

| カテゴリ | 指摘要約の類型 | 件数 | 状態 |
|---|---|---|---|
| fact | デモ手順が再現できない（前提となる操作の欠落） | 2 | 監視中 |
| fact | デモ手順に原稿外の知識の補完が必要 | 2 | 監視中 |
| fact | 出力例が実際の出力と一致しない | 2 | 監視中 |
| fact | 環境依存が明示されていない | 2 | 監視中 |
| fact | 記述と出典 URL の内容が一致しない | 2 | 監視中 |
| fact | 一次情報より広い範囲で断定 | 1 | 監視中 |
| fact | 出典のない断定が一次情報と食い違う | 1 | 監視中 |
| fact | 安全機構の範囲を実際より広く記述 | 1 | 監視中 |
| fact | 実行のたびに変わる結果を固定の出力例として提示 | 1 | 監視中 |
| fact | 実行記録であることと省略の方針が未記載 | 1 | 監視中 |
| fact | 機能が働く条件が抜けている | 1 | 監視中 |
| fact | 画面表示を示さずに確認を求めている | 1 | 監視中 |
| logic | 見出し直下の主張文と本文が矛盾 | 2 | 監視中 |
| logic | 1回の実行結果から因果を断定 | 1 | 監視中 |
| logic | ツール固有の挙動を一般化して断定 | 1 | 監視中 |
| logic | 主張が定義の言い換えにとどまる | 1 | 監視中 |
| logic | 前の節の予告が回収されていない | 1 | 監視中 |
| logic | 反論への言及がない | 1 | 監視中 |
| logic | 同じ章の別の節と矛盾する断定 | 1 | 監視中 |
| logic | 提示した因果が後段で回収されない | 1 | 監視中 |
| logic | 条件を落とした断定が後の章の主張と逆を向く | 1 | 監視中 |
| logic | 根拠のない数値 | 1 | 監視中 |
| logic | 章の主張を回収していない | 1 | 監視中 |
| paragraph | 1段落に複数トピックが混在 | 3 | 発火 |
| paragraph | 段落の要約文が末尾にある | 3 | 発火 |
| paragraph | 段落の第1文が予告文で内容を含まない | 1 | 監視中 |
| paragraph | 第2文以降に新しい主張が混ざる | 1 | 監視中 |
| paragraph | 見出し直下に主張文がない | 1 | 監視中 |
| tech-writing | 指示語の指す先が一意でない | 3 | 発火 |
| tech-writing | 一文が長く主語と述語が離れている | 2 | 監視中 |
| tech-writing | 動作の主体が不明 | 2 | 監視中 |
| tech-writing | 並列が文法的に揃っていない | 1 | 監視中 |
| tech-writing | 主語と述語がねじれている | 1 | 監視中 |
| tech-writing | 数値の数え方が原稿から再現できない | 1 | 監視中 |
| tech-writing | 曖昧語を使用 | 1 | 監視中 |
| style | 用語集に未登録の語がある | 3 | 発火 |
| style | ツール固有の記述が囲みの外にある | 2 | 監視中 |
| style | 同一概念に複数の呼び名 | 2 | 監視中 |
| style | 使用禁止の別表記を使用 | 1 | 監視中 |
| style | 和欧文間のスペース | 1 | 監視中 |
| style | 文体の混在（ですます調とである調） | 1 | 監視中 |
| style | 省略形を定義より前に使用 | 1 | 監視中 |
| style | 表記の大文字小文字の揺れ | 1 | 監視中 |
| style | 題材の名前が節をまたいで揃っていない | 1 | 監視中 |
| audience | 予告した操作が渡されない | 1 | 監視中 |
| audience | 出力例の実物と整形の区別が不明 | 1 | 監視中 |
| audience | 前の手順の結果により次の手順を試せない | 1 | 監視中 |
| audience | 前提知識「なし」の領域を説明せずに使用 | 1 | 監視中 |
| audience | 前提知識にない環境依存が未記載 | 1 | 監視中 |
| audience | 受講者の主要な不安に受け皿も予告もない | 1 | 監視中 |
| audience | 完了条件が示されていない | 1 | 監視中 |
| audience | 後の章に持ち越す論点の予告がない | 1 | 監視中 |
| audience | 操作の前後関係が書かれていない | 1 | 監視中 |
| audience | 数え方が前後で一致しない | 1 | 監視中 |
| audience | 環境によって手順が変わる箇所が未記載 | 1 | 監視中 |
| audience | 画面表示の読み方が説明されていない | 1 | 監視中 |
| audience | 節の導入がなく読む目的が示されない | 1 | 監視中 |
| audience | 読む節か手を動かす節かが判別できない | 1 | 監視中 |

状態: `監視中`（1〜2件） / `発火`（3件以上、改善タスク未作成） / `対応済`（改善を適用済み）
