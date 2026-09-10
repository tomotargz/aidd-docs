# レビュー指摘ログ

`/review-doc` が実行のたびに追記する。振り返り（`/retro`）と3回ルールの唯一の入力データ。

## 記録ルール

1. `Critical` `High` `Medium` のみ記録する。`Low` は記録しない（ノイズになるため）。
2. カテゴリと重大度は `foundation/review-criteria.md` の固定語彙のみを使う。
3. 「指摘要約」は**類型として書く**。「第3段落が長い」ではなく「1段落に複数トピックが混在」と書く。集計できることを優先する。
4. 対応欄は、修正 PR のマージ時に `fixed` / `wontfix` に更新する。`wontfix` の場合は理由を1行添える。
5. 行を削除しない。過去の傾向が振り返りの材料になる。

### wontfix の理由

- 2-2「中心となる主張がまとめから落ちている」— 章の中心となる主張の後半は、2章3節で述べることにした（2026-09-10 の判断）

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
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | Critical | 環境依存が明示されていない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Critical | 用語集に未登録の語がある | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | High | 一次情報より広い範囲で断定 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | High | 機能が働く条件が抜けている | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | High | 安全機構の範囲を実際より広く記述 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | High | 章の主張を回収していない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | High | 見出し直下の主張文と本文が矛盾 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | High | 提示した因果が後段で回収されない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | paragraph | High | 見出し直下に主張文がない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | paragraph | High | 1段落に複数トピックが混在 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | High | 使用禁止の別表記を使用 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 操作の前後関係が書かれていない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 前の手順の結果により次の手順を試せない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 画面表示の読み方が説明されていない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | High | 予告した操作が渡されない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | fact | Medium | 実行記録であることと省略の方針が未記載 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | Medium | 根拠のない数値 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | logic | Medium | 前の節の予告が回収されていない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | paragraph | Medium | 段落の要約文が末尾にある | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 曖昧語を使用 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 並列が文法的に揃っていない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 指示語の指す先が一意でない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 主語と述語がねじれている | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | tech-writing | Medium | 動作の主体が不明 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | 同一概念に複数の呼び名 | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | ツール固有の記述が囲みの外にある | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | 表記の大文字小文字の揺れ | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | style | Medium | 題材の名前が節をまたいで揃っていない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | Medium | 完了条件が示されていない | fixed |
| 2026-09-08 | docs/01-coding-agent/03-reproduce.md | 1-3 | audience | Medium | 環境によって手順が変わる箇所が未記載 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | fact | High | 同じ文書内で章の役割の説明が食い違う | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | fact | High | 出典の名称・URL・確認日が本文にない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | logic | High | 引用から導けない主張を引用の直後に置いている | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | logic | High | 扱わない理由と提供するものが同じ性質で矛盾する | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | logic | High | 規約にない前提を断定している | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | logic | High | 基準文書と食い違う記述 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | paragraph | High | 段落の第1文が前置きや指示語で内容を含まない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | paragraph | High | 1段落に複数トピックが混在 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | paragraph | High | 段落に要約文がない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | style | High | 使用禁止の別表記を使用 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | style | High | 定義前に省略形を使用 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | style | High | 用語集に未登録の語がある | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | style | High | 受講者を主語にした決めつけ | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | audience | High | 到達点が示されていない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | audience | High | 必要な準備物への案内がない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | audience | High | 前提知識との違いが示されず新規性が伝わらない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | fact | Medium | 宣言が複数の場所で重複している | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | logic | Medium | 根拠のない断定 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | logic | Medium | 数値が何のものか定まっていない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | tech-writing | Medium | 指示語の指す先が一意でない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | tech-writing | Medium | 同じ語を1文で2回使用 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | tech-writing | Medium | 動作の主語が抽象名詞 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | tech-writing | Medium | 曖昧語を使用 | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | tech-writing | Medium | 並列が文法的に揃っていない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | tech-writing | Medium | 日本語として読み下しにくい | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | paragraph | Medium | 第2文以降に新しい主張が混ざる | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | style | Medium | 和欧文間のスペース | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | style | Medium | 英文引用の形式が章をまたいで揺れている | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | style | Medium | 見出し直下の主張文が1文になっていない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | audience | Medium | 研修と自習の区別が数値から読み取れない | fixed |
| 2026-09-08 | docs/00-introduction/README.md | 0 | audience | Medium | 書式の例が実物の形になっていない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | fact | High | 参照先の対応づけが一意でない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | fact | High | 前提としている環境が列挙から漏れている | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | audience | High | 前提知識では意味を取れない語で到達目標を定義 | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | style | High | 定義前に省略形を使用 | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | paragraph | High | 1段落に複数トピックが混在 | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | paragraph | High | 段落の第1文が前置きや指示語で内容を含まない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | logic | High | 節どうしの依存関係が示されていない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | fact | Medium | 数値の適用先が読者の状況と合っていない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | logic | Medium | 結論が根拠より狭い範囲に圧縮されている | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | style | Medium | 同一概念に複数の呼び名 | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | style | Medium | H1 と frontmatter の title が一致しない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | style | Medium | 見出し直下の主張文が1文になっていない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | audience | Medium | 前の文書と準備物の記述が食い違う | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | audience | Medium | 参照の順序が循環している | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | audience | Medium | 抽象語のまま説明されず読者の関心に応えていない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | tech-writing | Medium | 指示語の指す先が一意でない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | tech-writing | Medium | 同じ語を1文で2回使用 | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | tech-writing | Medium | 動作の主語が抽象名詞 | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | tech-writing | Medium | 主語が省かれ文が単独で閉じない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | tech-writing | Medium | 件数を述べたリストが番号付きでない | fixed |
| 2026-09-08 | docs/01-coding-agent/README.md | 1 | paragraph | Medium | 段落の切り分けの基準が示されていない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | fact | Critical | 前の章の記述と矛盾する断定 | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | style | Critical | 用語集に未登録の語がある | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | fact | High | 経験的な主張に出典がない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | logic | High | 主張を支える根拠が成立していない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | logic | High | 条件つきの命題を無条件に断定 | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | paragraph | High | 段落に要約文がない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | paragraph | High | 1段落に複数トピックが混在 | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | style | High | 用語集に未登録の語がある | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | logic | Medium | 反論への言及がない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | logic | Medium | 1件の事例から一般化している | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | paragraph | Medium | 主張文が図の位置参照に依存している | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | paragraph | Medium | 段落が短く意味の単位になっていない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | tech-writing | Medium | 同じ語を1文で2回使用 | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | tech-writing | Medium | 指示語の指す先が一意でない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | tech-writing | Medium | 理由を述べる位置に事実の言い換えがある | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | tech-writing | Medium | 日本語として読み下しにくい | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | style | Medium | 同一概念に複数の呼び名 | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | audience | Medium | 後の章との担当範囲が読み取れない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | audience | Medium | 前の節と重複し新しく分かることが少ない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | audience | Medium | 比喩の指す対象が定まらない | fixed |
| 2026-09-09 | docs/02-not-just-coding/01-where-it-got-faster.md | 2-1 | fact | Medium | 引用の来歴が frontmatter にない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | fact | High | 相関を因果として記述 | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | fact | High | 引用が主張を支えていない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | fact | High | 出典のない定量的な断定 | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | logic | High | 比喩からの導出を根拠として扱っている | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | logic | High | 節の冒頭が立てた問いに本文が答えていない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | logic | High | 前提の一部しか使わずに結論づけている | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | paragraph | High | 段落の要約文が末尾にある | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | paragraph | High | 1段落に複数トピックが混在 | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | audience | High | 英文引用に訳がなく根拠が読み取れない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | audience | High | 見出しが本文の結論と逆に読める | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | audience | High | 中心となる一文の具体例がない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | logic | Medium | 比喩と観察の間に橋がない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | logic | Medium | 中心となる主張がまとめから落ちている | wontfix |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | logic | Medium | アウトラインの根拠が原稿で入れ替わっている | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | fact | Medium | 用語の言い換えに出典がない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | fact | Medium | 同一文書内で用語の定義がずれている | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | fact | Medium | エージェントの挙動を出典なく断定 | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | style | Medium | 同一概念に複数の呼び名 | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | style | Medium | 和欧文間のスペース | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | style | Medium | 見出し直下の1文が見出しの主張になっていない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | style | Medium | 用語集に未登録の語がある | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | tech-writing | Medium | 指示語の指す先が一意でない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | tech-writing | Medium | 同じ語を1文で2回使用 | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | tech-writing | Medium | 動作の主語が抽象名詞 | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | tech-writing | Medium | 日本語として読み下しにくい | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | paragraph | Medium | 段落が短く意味の単位になっていない | fixed |
| 2026-09-09 | docs/02-not-just-coding/02-amplifier.md | 2-2 | audience | Medium | 同じ引用の再掲の理由が書かれていない | fixed |

## 集計（3回ルールの判定用）

`/review-doc` が実行末尾で更新する。同一カテゴリ・同種の指摘が3件に達したら、`backlog.md` のプロセス改善にタスクを追加する。

| カテゴリ | 指摘要約の類型 | 件数 | 状態 |
|---|---|---|---|
| fact | デモ手順が再現できない（前提となる操作の欠落） | 2 | 監視中 |
| fact | デモ手順に原稿外の知識の補完が必要 | 2 | 監視中 |
| fact | 出力例が実際の出力と一致しない | 2 | 監視中 |
| fact | 環境依存が明示されていない | 2 | 監視中 |
| fact | 記述と出典 URL の内容が一致しない | 2 | 監視中 |
| fact | エージェントの挙動を出典なく断定 | 1 | 監視中 |
| fact | 一次情報より広い範囲で断定 | 1 | 監視中 |
| fact | 出典のない定量的な断定 | 1 | 監視中 |
| fact | 出典のない断定が一次情報と食い違う | 1 | 監視中 |
| fact | 出典の名称・URL・確認日が本文にない | 1 | 監視中 |
| fact | 前の章の記述と矛盾する断定 | 1 | 監視中 |
| fact | 前提としている環境が列挙から漏れている | 1 | 監視中 |
| fact | 参照先の対応づけが一意でない | 1 | 監視中 |
| fact | 同じ文書内で章の役割の説明が食い違う | 1 | 監視中 |
| fact | 同一文書内で用語の定義がずれている | 1 | 監視中 |
| fact | 安全機構の範囲を実際より広く記述 | 1 | 監視中 |
| fact | 実行のたびに変わる結果を固定の出力例として提示 | 1 | 監視中 |
| fact | 実行記録であることと省略の方針が未記載 | 1 | 監視中 |
| fact | 宣言が複数の場所で重複している | 1 | 監視中 |
| fact | 引用が主張を支えていない | 1 | 監視中 |
| fact | 引用の来歴が frontmatter にない | 1 | 監視中 |
| fact | 数値の適用先が読者の状況と合っていない | 1 | 監視中 |
| fact | 機能が働く条件が抜けている | 1 | 監視中 |
| fact | 用語の言い換えに出典がない | 1 | 監視中 |
| fact | 画面表示を示さずに確認を求めている | 1 | 監視中 |
| fact | 相関を因果として記述 | 1 | 監視中 |
| fact | 経験的な主張に出典がない | 1 | 監視中 |
| logic | 反論への言及がない | 2 | 監視中 |
| logic | 見出し直下の主張文と本文が矛盾 | 2 | 監視中 |
| logic | 1件の事例から一般化している | 1 | 監視中 |
| logic | 1回の実行結果から因果を断定 | 1 | 監視中 |
| logic | アウトラインの根拠が原稿で入れ替わっている | 1 | 監視中 |
| logic | ツール固有の挙動を一般化して断定 | 1 | 監視中 |
| logic | 中心となる主張がまとめから落ちている | 1 | 監視中 |
| logic | 主張が定義の言い換えにとどまる | 1 | 監視中 |
| logic | 主張を支える根拠が成立していない | 1 | 監視中 |
| logic | 前の節の予告が回収されていない | 1 | 監視中 |
| logic | 前提の一部しか使わずに結論づけている | 1 | 監視中 |
| logic | 同じ章の別の節と矛盾する断定 | 1 | 監視中 |
| logic | 基準文書と食い違う記述 | 1 | 監視中 |
| logic | 引用から導けない主張を引用の直後に置いている | 1 | 監視中 |
| logic | 扱わない理由と提供するものが同じ性質で矛盾する | 1 | 監視中 |
| logic | 提示した因果が後段で回収されない | 1 | 監視中 |
| logic | 数値が何のものか定まっていない | 1 | 監視中 |
| logic | 条件つきの命題を無条件に断定 | 1 | 監視中 |
| logic | 条件を落とした断定が後の章の主張と逆を向く | 1 | 監視中 |
| logic | 根拠のない数値 | 1 | 監視中 |
| logic | 根拠のない断定 | 1 | 監視中 |
| logic | 比喩からの導出を根拠として扱っている | 1 | 監視中 |
| logic | 比喩と観察の間に橋がない | 1 | 監視中 |
| logic | 章の主張を回収していない | 1 | 監視中 |
| logic | 節どうしの依存関係が示されていない | 1 | 監視中 |
| logic | 節の冒頭が立てた問いに本文が答えていない | 1 | 監視中 |
| logic | 結論が根拠より狭い範囲に圧縮されている | 1 | 監視中 |
| logic | 規約にない前提を断定している | 1 | 監視中 |
| paragraph | 1段落に複数トピックが混在 | 7 | 発火 |
| paragraph | 段落の要約文が末尾にある | 4 | 発火 |
| paragraph | 段落が短く意味の単位になっていない | 2 | 監視中 |
| paragraph | 段落に要約文がない | 2 | 監視中 |
| paragraph | 段落の第1文が前置きや指示語で内容を含まない | 2 | 監視中 |
| paragraph | 第2文以降に新しい主張が混ざる | 2 | 監視中 |
| paragraph | 主張文が図の位置参照に依存している | 1 | 監視中 |
| paragraph | 段落の切り分けの基準が示されていない | 1 | 監視中 |
| paragraph | 段落の第1文が予告文で内容を含まない | 1 | 監視中 |
| paragraph | 見出し直下に主張文がない | 1 | 監視中 |
| tech-writing | 指示語の指す先が一意でない | 7 | 発火 |
| tech-writing | 同じ語を1文で2回使用 | 4 | 発火 |
| tech-writing | 動作の主語が抽象名詞 | 3 | 発火 |
| tech-writing | 日本語として読み下しにくい | 3 | 発火 |
| tech-writing | 一文が長く主語と述語が離れている | 2 | 監視中 |
| tech-writing | 並列が文法的に揃っていない | 2 | 監視中 |
| tech-writing | 動作の主体が不明 | 2 | 監視中 |
| tech-writing | 曖昧語を使用 | 2 | 監視中 |
| tech-writing | 主語が省かれ文が単独で閉じない | 1 | 監視中 |
| tech-writing | 主語と述語がねじれている | 1 | 監視中 |
| tech-writing | 件数を述べたリストが番号付きでない | 1 | 監視中 |
| tech-writing | 数値の数え方が原稿から再現できない | 1 | 監視中 |
| tech-writing | 理由を述べる位置に事実の言い換えがある | 1 | 監視中 |
| style | 用語集に未登録の語がある | 7 | 発火 |
| style | 同一概念に複数の呼び名 | 5 | 発火 |
| style | 和欧文間のスペース | 3 | 発火 |
| style | ツール固有の記述が囲みの外にある | 2 | 監視中 |
| style | 使用禁止の別表記を使用 | 2 | 監視中 |
| style | 定義前に省略形を使用 | 2 | 監視中 |
| style | 見出し直下の主張文が1文になっていない | 2 | 監視中 |
| style | H1 と frontmatter の title が一致しない | 1 | 監視中 |
| style | 受講者を主語にした決めつけ | 1 | 監視中 |
| style | 文体の混在（ですます調とである調） | 1 | 監視中 |
| style | 省略形を定義より前に使用 | 1 | 監視中 |
| style | 英文引用の形式が章をまたいで揺れている | 1 | 監視中 |
| style | 表記の大文字小文字の揺れ | 1 | 監視中 |
| style | 見出し直下の1文が見出しの主張になっていない | 1 | 監視中 |
| style | 題材の名前が節をまたいで揃っていない | 1 | 監視中 |
| audience | 中心となる一文の具体例がない | 1 | 監視中 |
| audience | 予告した操作が渡されない | 1 | 監視中 |
| audience | 出力例の実物と整形の区別が不明 | 1 | 監視中 |
| audience | 到達点が示されていない | 1 | 監視中 |
| audience | 前の手順の結果により次の手順を試せない | 1 | 監視中 |
| audience | 前の文書と準備物の記述が食い違う | 1 | 監視中 |
| audience | 前の節と重複し新しく分かることが少ない | 1 | 監視中 |
| audience | 前提知識「なし」の領域を説明せずに使用 | 1 | 監視中 |
| audience | 前提知識では意味を取れない語で到達目標を定義 | 1 | 監視中 |
| audience | 前提知識との違いが示されず新規性が伝わらない | 1 | 監視中 |
| audience | 前提知識にない環境依存が未記載 | 1 | 監視中 |
| audience | 参照の順序が循環している | 1 | 監視中 |
| audience | 受講者の主要な不安に受け皿も予告もない | 1 | 監視中 |
| audience | 同じ引用の再掲の理由が書かれていない | 1 | 監視中 |
| audience | 完了条件が示されていない | 1 | 監視中 |
| audience | 後の章との担当範囲が読み取れない | 1 | 監視中 |
| audience | 後の章に持ち越す論点の予告がない | 1 | 監視中 |
| audience | 必要な準備物への案内がない | 1 | 監視中 |
| audience | 抽象語のまま説明されず読者の関心に応えていない | 1 | 監視中 |
| audience | 操作の前後関係が書かれていない | 1 | 監視中 |
| audience | 数え方が前後で一致しない | 1 | 監視中 |
| audience | 書式の例が実物の形になっていない | 1 | 監視中 |
| audience | 比喩の指す対象が定まらない | 1 | 監視中 |
| audience | 環境によって手順が変わる箇所が未記載 | 1 | 監視中 |
| audience | 画面表示の読み方が説明されていない | 1 | 監視中 |
| audience | 研修と自習の区別が数値から読み取れない | 1 | 監視中 |
| audience | 節の導入がなく読む目的が示されない | 1 | 監視中 |
| audience | 英文引用に訳がなく根拠が読み取れない | 1 | 監視中 |
| audience | 見出しが本文の結論と逆に読める | 1 | 監視中 |
| audience | 読む節か手を動かす節かが判別できない | 1 | 監視中 |

状態: `監視中`（1〜2件） / `発火`（3件以上、改善タスク未作成） / `対応済`（改善を適用済み）
