# カリキュラム

この文書は教材全体の設計図である。`backlog.md` の章立ては、この文書から機械的に展開する。

誰に向けて書くかは `audience.md`、どう書くかは `style-guide.md` に書く。この文書に書くのは**何を教えるか**である。

## 研修の制約

学習目標と章立ての分量は、この制約から決まる。

| 項目 | 内容 |
|---|---|
| 提供形態 | 社外向け研修（有償） |
| 受講形態 | 2日間の集合研修 |
| 進め方 | 講義中心。手を動かすのは講師によるデモのみ |
| 想定人数 | 未確定（講義中心のため章構成への影響は小さい） |

## 教材の方針

- **原則中心、事例として Claude Code**。考え方・進め方を軸に置き、ツールは具体例として登場させる。
- ツール固有の記述は、原則の記述と混ぜず、囲み（`> [!NOTE]`）で分離する。詳細は `style-guide.md` を参照。
- **位置づけ**: 「AIを速く使う技術」ではなく「**AIが効く状態を作るエンジニアリング**」を教える。

### 中心的な主張

> 開発生産性を上げるには、エージェントにコーディングをさせるだけでは不十分である。

この主張は DORA の 2025 年の研究知見に支えられている。

> "AI acts as an amplifier, but the greatest returns come from focusing on the underlying sociotechnical systems."
> — [DORA Research](https://dora.dev/research/?view=detail)（2026-08-26 確認）

AI は既存のシステムを増幅する。制約がコーディング速度以外の場所にあるなら、コーディングを速くしても全体は変わらない。教材はこの一点を軸に構成する。

## 学習目標の水準

各目標には水準を付す。定義は次のとおり。

| 水準 | 定義 |
|---|---|
| **実践できる** | 教材を手元に置いて、自分の実務で実行できる |
| **説明できる** | 必要性とその根拠を、自分の言葉で他者に述べられる |

「実践できる」を**研修中に**できることと定義しない。研修は講義中心で演習がなく、その水準には到達しない。`audience.md` で「研修後の自習」を教材の直接の読者と定義したことに対応させ、**教材を見ながら実務で実行できる**ことを到達点とする。

## 全体の学習目標

受講者の課題（`audience.md`）への応答として設計する。対応する DORA capability があれば注記する。

**目標に capability が対応している必要はない。** 必要なのは根拠であって capability ではない。O1 と O2 は capability を持たないが、それぞれツールの公式ドキュメントと DORA の研究知見に支えられている。

番号は学習の順序を表す。

出典: [DORA Capabilities](https://dora.dev/capabilities/)（2026-08-26 確認）

### O1. エージェントを使った開発がどのように進むかを、自分の手元で再現できる【実践できる】

- **応答する課題**: 1（エージェントを使った開発のイメージが湧いていない）
- **対応する capability**: なし（DORA の射程外。出典はツールの公式ドキュメント）
- **位置づけ**: 前提知識「コーディングエージェント: なし」を埋める。教材の要件2に対応する
- **注記**: 「イメージが湧かない」を解くのは説明ではなく再現である。研修中はデモを見て、研修後に自分で再現する（`audience.md`「受講者が教材を読む状況」）という設計にそのまま対応させる

### O2. AIにコードを書かせるだけでは生産性が上がらないことを、根拠を挙げて説明できる【説明できる】

- **応答する課題**: 5・6（使い始めてから遭遇する問題、慣れた後に生産性が伸びない）
- **根拠**: DORA 2025 の "AI acts as an amplifier" の知見
- **位置づけ**: 教材全体の前提。O3 以降はすべてこの主張の具体化である
- **注記**: O1 の後に置く。エージェントを使った開発がどんなものか分からないうちは、「それだけでは速くならない」も実感できない。**一度手を動かしてから聞くほうが納得しやすい**

### O3. タスクをエージェントに任せられる単位に分割し、必要な文脈を与えて指示できる【実践できる】

- **応答する課題**: 2（使ってみたが期待するアウトプットが得られない）
- **対応する capability**: Working in small batches / Documentation quality / AI-accessible internal data（部分採用）
- **根拠**: DORA は文脈の構成を **"context engineering"** と呼び、"giving teams AI tools that can access internal data directly amplifies the positive impact of AI adoption, serving as a statistically significant multiplier for individual effectiveness and code quality" と述べている。文書品質との関係も DORA が明示しており、"High-quality documentation is a primary driver of AI adoption"
- **注記**: AI-accessible internal data の実装3段階のうち、**第1段階（手動のコンテキストエンジニアリング）のみ**をここで扱う。第2段階（RAG / MCP による自動化）と第3段階（セキュリティ基盤を伴う運用）は組織スケールであり、O6 で「説明できる」水準として扱う

### O4. どこまで任せ、どこで人が確認するかを、リスクに応じて設計できる【実践できる】

- **応答する課題**: 3（使いどころの判断がつかない）
- **対応する capability**: Streamlining change approval（部分採用）
- **根拠**: 重量級の承認が変更失敗率を下げる証拠はなく、むしろバッチを大きくし遅くする。リスクに応じて承認の重さを変えることが推奨されている

### O5. AIの出力を安全に受け入れる仕組みを、自分の開発に組み込める【実践できる】

- **応答する課題**: 4（生成されたコードの品質を保てるか不安）
- **対応する capability**: Version control / Test automation / Continuous integration / Continuous delivery / Deployment automation / Pervasive security（部分採用）
- **根拠**: セキュリティテストの自動化について "code can be continuously tested at scale without requiring a manual review"。エージェントが大量のコードを出すとき人間のレビューはスケールしない
- **注記**: Continuous integration では trunk-based development の3閾値（アクティブブランチ3つ以下、1日1回以上 trunk にマージ、コードフリーズを設けない）を明示的に扱う

### O6. 効果が出ないとき、制約がどこにあるかを見立て、組織に働きかけられる【説明できる】

- **応答する課題**: 5・6
- **対応する capability**: Visibility of work in the value stream / Work in process limits / Loosely coupled teams / Clear and communicated AI stance / AI-accessible internal data / Platform engineering / User-centric focus
- **根拠**: WIP 制限は "expose problems in the system so they can be addressed" のための装置であり、"Without doing this, it's impossible to see the actual bottlenecks"
- **注記1**: Visibility of work in the value stream と Work in process limits は**セットで扱う**。一方向の手順（可視化 → 診断 → WIP 制限で対処）として書くと DORA の主張と食い違う。両者は相互に補強する循環である
- **注記2**: AI-accessible internal data は O3 にも現れる。**同一の capability を、水準を分けて2つの目標に置いている。** ここで扱うのは実装の第2・第3段階（RAG / MCP による自動化、セキュリティ基盤を伴う運用）であり、組織に整備を提起できる水準を目指す。第1段階（手動のコンテキストエンジニアリング）は O3 で「実践できる」水準として扱う

## 扱わないこと

範囲が広がりすぎるのを防ぐため、次は扱わない。教材の冒頭で明示する。

| 扱わないこと | 理由 |
|---|---|
| 特定の言語・フレームワークの習得 | デモで使う題材の範囲を超えない |
| AIエージェント自体の開発（SDK・MCP 実装） | エージェントを使う側に徹する |
| 経営・投資判断の材料（ROI・製品比較・ツール選定） | 受講者は現場のエンジニアである |
| 組織の承認プロセスそのものの改定 | Streamlining change approval の部分採用で落とした部分 |
| InfoSec チームとの協働体制、承認済みライブラリの整備 | Pervasive security の部分採用で落とした部分 |
| LLM の仕組み・プロンプト工学の体系的な理論 | 実践に必要な範囲に限って扱う |
| SAST / DAST / 依存関係スキャンの製品比較 | ツール選定は扱わない範囲 |

## 採用しなかった capability

判断の理由を残す。同じ検討を繰り返さないため、また章立ての設計時に取りこぼしに気づくため。

### 他の capability に包含されるもの

個別に立てる固有の中身が残らないため、採用済みの capability の中で扱う。

| capability | 包含先 | 根拠 |
|---|---|---|
| Visual management | Visibility of work in the value stream | カードウォール、ストーリーボード、カンバンボードは同 capability の推奨実践として挙げられている |
| Trunk-based development | Continuous integration | "Trunk-based development is a required practice for continuous integration"。CI の4実践のひとつとして列挙されている |
| Code maintainability | Version control / Continuous integration / Pervasive security | 推奨実践を分解すると、統一 VCS とコード検索は Version control、依存の互換性検査は Continuous integration、脆弱性検知は Pervasive security に含まれる。「エージェントが読めるコードベース」という論点は AI-accessible internal data（O6）で扱う |

### 見送ったもの

| capability | 理由 |
|---|---|
| Monitoring and observability | 採用を支える論が「AI 駆動開発では読解より観測の比重が上がる」という私たちの推論であり、一次情報の裏付けがない。DORA は observability と AI を結びつけていない。裏付けが見つかれば再検討する |

### 未検討のまま除外しているもの

Customer feedback / Learning culture / Team experimentation / Transformational leadership / Generative organizational culture / Job satisfaction / Well-being / Database change management / Test data management / Flexible infrastructure / Empowering teams to choose tools / Healthy data ecosystems / Proactive failure notification / Monitoring systems to inform business decisions

このうち `Learning culture` と `Team experimentation` は、見送った目標（後述）の裏付け候補として検討したが、どちらも組織・チームスケールであり適合しなかった。

### 部分採用の歯止め

capability の一部だけを採用する場合、次の2条件を満たすこと。無制限に許すと「DORA に基づく」と謳いながら中身が独自解釈になる。

1. その部分だけで一つの観察可能な行動として成立すること
2. 元の capability の主眼から外れていないこと

条件2により、Visibility of work in the value stream は部分採用しない。部門をまたいで見ること自体が要点であり、個人スケールに縮約すると、この capability が警告している局所最適そのものを教えることになる。

## 教材の要件

1. **各章は、`audience.md` の「受講者が抱えている課題」のいずれかに応答するものでなければならない。**
2. **前提知識が「なし」の領域は、教材内で説明する。前提にしてはいけない。** 該当するのはコーディングエージェント、ユニットテストの作成、CI/CD パイプライン。

要件2は分量に直接効く。テスト自動化と CI/CD を前提にできないため、これらを教材内で扱う必要がある。

## 執筆時の注意

**DORA の記述と、私たちの論を書き分ける。** DORA が AI との関連を明示しているのは AI カテゴリの capability のみである。それ以外の capability が「AI 駆動開発で効く」という主張は私たちの論であり、DORA の記述ではない。

**推論による対応づけは現時点で存在しない。** 検討の過程で2件が候補に挙がったが、いずれも解消された。

| 候補だった対応づけ | 解消の経緯 |
|---|---|
| Loosely coupled teams → O5 | 一次情報を確認したところ組織スケールの capability だったため、O6（説明できる）へ移した |
| Documentation quality → O3 | 「文書品質 → AI の有効性」は DORA 自身が述べていた。"High-quality documentation is a primary driver of AI adoption"（AI-accessible internal data のページ）。推論ではなかった |

**新たに推論による対応づけを追加する場合は、この節に記録し、教材では出典として DORA を挙げないこと。**

**Human in the loop / on the loop、Loop Engineering は DORA の語彙ではない。** 教材に載せるなら別途出典が必要。DORA が使うのは **"context engineering"** である（AI-accessible internal data）。

**同一 capability を複数の目標に置く場合は、水準の違いを明示する。** 現在該当するのは AI-accessible internal data のみ（O3 で実践、O6 で説明）。

## 見送った学習目標

### 自分の進め方を振り返って改善できる

インタビューで「受講後の姿」として挙がった項目だが、学習目標には立てない（2026-08-31 決定）。

**主たる理由は中心的主張と向きが逆になることである。** 教材の主張は「制約はコーディング速度ではなく、その周りのシステムにある」。一方この目標は、うまくいかない原因を**自分の使い方**に向ける。受講者が半年後に「思ったより速くならない」と感じたとき、この目標は個人技の改善へ、O2 と O6 はシステムの改善へ誘導する。並べて置くと、受講者はより馴染みのある前者に流れる。

副次的な理由として、DORA の裏付けがない。候補の `Learning culture`（研修予算、心理的安全性、知識共有の場）と `Team experimentation`（チーム外の許可なくアイデアを試せる権限）は、いずれも組織・チームスケールであり、個人の振り返りを裏付けない。

失われるものの受け皿は次のとおり。

| 失われるもの | 受け皿 |
|---|---|
| 課題6への応答 | O6 が対応する。しかも「制約はどこか」という正しい向きで |
| 受講後も学び続けること | `audience.md` の「教材は後で戻ってくる場所として読まれる」で担保。目標に立てなくても、教材の書き方の制約として機能する |
| 受講者の期待「判断基準を持ち帰る」 | O3・O4 が直接対応する |

## 未解決の論点

### 分量の現実性

学習目標6個に対し、capability は16個。2日間・講義中心という制約に収まるかは未検証である。

**これは学習目標の構造の問題ではない。** 目標は受講者の課題に対応する単位であり、目標間で capability 数を揃える理由はない。検証は章立ての設計時に、各章の時間配分を見積もることで行う。収まらない場合に調整するのは章の粒度であって、目標の形ではない。

## 章立て

未策定。**「全体の学習目標の決定」の次のタスク**として設計する。

各章には到達目標と、その章が前提とする章を書く。依存関係が循環していないことを確認する。

> [!IMPORTANT]
> **最初の章は最小の1節から始める。** コマンド5個とサブエージェント5個は、まだ一度も動いていない未検証の仕組みである（`retrospectives/phase-0-1.md` P3）。
> 大きな章から着手すると、仕組みの問題と内容の問題が同時に噴出して切り分けられない。
> 1節を `/draft` → `/verify-demo` → `/review-doc` まで通し、仕組みを検証してから残りに進む。

既に判明している順序の制約:

- **Pervasive security（セキュリティテストの自動化）は、Test automation の後にしか置けない。** 受講者はユニットテストの作成を前提にできないため
- **Continuous integration は Version control と Test automation の後に置く。** CI は両者を組み合わせた実践である

章立ての軸の候補: **「人手の検査に頼らない」**。Pervasive security の "without requiring a manual review" と、Streamlining change approval の「重量級の人手承認は変更失敗率を下げない」は、どちらも人手の検査を自動化された検査とリスクベースの判断に置き換えるという同じ方向を指している。

## 章ごとの詳細

### N章 （タイトル）

- **到達目標**: この章を読み終えた受講者ができるようになること
- **中心となる主張**: この章が伝えたいことを1文で
- **扱わないこと**: 隣接するが範囲外のトピック
- **節構成**: 各節の主題

（章立ての設計時に記述する）

## 依存関係

章の順序が「前提知識の積み上げ」として成立していることを示す。

```
（章立ての設計時に図示する）
```
