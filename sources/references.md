# 出典台帳

教材で参照した一次情報を記録する。`fact-checker` が確認のたびに追記・更新する。

## 記録ルール

1. **一次情報を参照する**。公式ドキュメント、公式ブログ、仕様書、論文を優先する。二次情報しかない場合は「種別」に明記する。
2. ID（`REF-NNN`）を振り、教材の frontmatter `sources` から参照する。
3. **確認日を必ず書く**。ツールの仕様は変わるため、確認日のない出典は出典として扱わない。
4. 参照した箇所を「引用・要点」に残す。リンク切れに備える。
5. 出典が更新された場合は、行を書き換えず新しい ID を追加し、旧 ID に「更新: REF-NNN」と注記する。

## 台帳

| ID | 種別 | タイトル | URL | 確認日 | 引用・要点 | 参照している教材 |
|---|---|---|---|---|---|---|
| REF-001 | 一次 | DORA Capabilities カタログ | https://dora.dev/capabilities/ | 2026-08-26 | capability の一覧。AI カテゴリが独立して存在する。Version control と Working in small batches は Core と AI の両方に属する | foundation/curriculum.md |
| REF-002 | 一次 | DORA Research（Core Model） | https://dora.dev/research/?view=detail | 2026-08-26 | "AI acts as an amplifier, but the greatest returns come from focusing on the underlying sociotechnical systems." 教材の中心的主張の根拠 | foundation/curriculum.md |
| REF-003 | 一次 | DORA: Streamlining change approval | https://dora.dev/capabilities/streamlining-change-approval/ | 2026-08-26 | "no evidence...that a more formal, external review process was associated with lower change fail rates" / "Such heavyweight approaches tend to slow down the delivery process leading to the release of larger batches less frequently" / 推奨はリスクベースの変更区分とチェックイン時点のピアレビュー | foundation/curriculum.md（O4） |
| REF-004 | 一次 | DORA: Pervasive security | https://dora.dev/capabilities/pervasive-security/ | 2026-08-26 | "Building security tests into the automated testing process means that code can be continuously tested at scale without requiring a manual review." / 2016年の知見「high-performing teams spend 50 percent less time remediating security issues than low-performing teams」 | foundation/curriculum.md（O5） |
| REF-005 | 一次 | DORA: Visibility of work in the value stream | https://dora.dev/capabilities/work-visibility-in-value-stream/ | 2026-08-26 | バリューストリームマッピングは全工程（ビジネス、デザイン、テスト、QA、運用、サポート）のステークホルダーを集めて行う。部門をまたいで見ること自体が要点 | foundation/curriculum.md（O6） |
| REF-006 | 一次 | DORA: Work in process limits | https://dora.dev/capabilities/wip-limits/ | 2026-08-26 | "The point of WIP limits is to expose problems in the system so they can be addressed. Without doing this, it's impossible to see the actual bottlenecks" / "particularly when they are combined with the use of visual displays and feedback" | foundation/curriculum.md（O6） |
| REF-007 | 一次 | DORA: Visual management | https://dora.dev/capabilities/visual-management/ | 2026-08-26 | カードウォール、ストーリーボード、カンバンボード等の可視化。Visibility of work in the value stream の推奨実践に含まれる | foundation/curriculum.md（O6 の背景） |
| REF-008 | 一次 | DORA: Trunk-based development | https://dora.dev/capabilities/trunk-based-development/ | 2026-08-26 | "Trunk-based development is a required practice for continuous integration." 3閾値: アクティブブランチ3つ以下 / 1日1回以上 trunk にマージ / コードフリーズと統合フェーズを設けない | foundation/curriculum.md（O5） |
| REF-009 | 一次 | DORA: Continuous integration | https://dora.dev/capabilities/continuous-integration/ | 2026-08-26（2026-09-02 再確認） | CI の4実践: 各コミットが自動ビルドを起動 / 各コミットが数分で返る自動テストを起動 / trunk-based development / ビルドが壊れたら最優先で直す合意。"CI requires automated unit tests." / "helping software development teams implement continuous integration should be the number one priority for any organization wanting to start the journey to continuous delivery"（2026-09-02 追加） | foundation/curriculum.md（O5、6章） |
| REF-010 | 一次 | DORA: Monitoring and observability | https://dora.dev/capabilities/monitoring-and-observability/ | 2026-08-26 | Monitoring は事前定義した指標の監視、Observability は "actively debug their system" による "unknown unknowns" の発見。**採用を見送った判断の根拠として記録** | なし（不採用） |
| REF-011 | 一次 | DORA: Code maintainability | https://dora.dev/capabilities/code-maintainability/ | 2026-08-31 | 組織横断のコード検索・再利用・依存管理。「他チームのコードを変更できる」「known-good なバージョンを使い迅速に更新できる」。**個別採用せず、Version control / CI / Pervasive security に包含される判断の根拠** | なし（包含） |
| REF-012 | 一次 | DORA: Loosely coupled teams | https://dora.dev/capabilities/loosely-coupled-teams/ | 2026-08-31 | Conway の法則に基づくチーム編成と権限。「他チームと調整せずデプロイできる」「大規模な変更に外部の許可が要らない」。組織スケールの capability であるため「説明できる」水準に置く | foundation/curriculum.md（O6） |
| REF-013 | 一次 | DORA: Documentation quality | https://dora.dev/capabilities/documentation-quality/ | 2026-08-31 | 内部文書の品質を明確さ・見つけやすさ・信頼性など8指標で測る。"documentation quality driving the implementation of every single technical practice we studied"。トランクベース開発の導入時、文書品質が平均以上なら組織パフォーマンス1525%向上、平均以下なら36%。**このページ自体は AI に言及しない** | foundation/curriculum.md（O3） |
| REF-014 | 一次 | DORA: AI-accessible internal data | https://dora.dev/capabilities/ai-accessible-internal-data/ | 2026-08-31 | "This connection, often implemented through a discipline known as **context engineering**, transforms generic AI models into specialized experts." / "giving teams AI tools that can access internal data directly amplifies the positive impact of AI adoption, serving as a statistically significant multiplier for individual effectiveness and code quality" / **"High-quality documentation is a primary driver of AI adoption."** 実装3段階: 手動のコンテキストエンジニアリング → RAG / MCP による自動化 → セキュリティ基盤を伴う運用 | foundation/curriculum.md（O3 第1段階 / O6 第2・3段階） |
| REF-015 | 一次 | DORA: Continuous delivery | https://dora.dev/capabilities/continuous-delivery/ | 2026-09-02 | "Continuous delivery is the ability to release changes of all kinds on demand quickly, safely, and sustainably." / **"While continuous delivery is often combined with continuous integration and shortened to CI/CD, research shows that continuous integration is only one element of implementing continuous delivery."** foundational drivers に Test automation / Deployment automation / Trunk-based development / Pervasive security / Continuous integration / Version control を挙げる。**CD を5〜7章の到達点として位置づける判断の根拠** | foundation/curriculum.md（O5、7章） |
| REF-016 | 一次 | Claude Code: Overview | https://code.claude.com/docs/en/overview | 2026-09-02 | "Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your development tools. Available in your terminal, IDE, desktop app, and browser." ターミナル / IDE 拡張 / デスクトップアプリ / ブラウザの4つの surface で動く | foundation/curriculum.md（1章） |
| REF-017 | 一次 | Claude Code: How Claude remembers your project（CLAUDE.md） | https://code.claude.com/docs/en/memory | 2026-09-02 | "CLAUDE.md files are markdown files that give Claude persistent instructions for a project, your personal workflow, or your entire organization. You write these files in plain text; Claude reads them at the start of every session." 配置は managed policy / `~/.claude/CLAUDE.md` / `./CLAUDE.md` または `./.claude/CLAUDE.md` / `./CLAUDE.local.md` の4スコープで、この順に読み込まれる。**1ファイル200行以下を目安とする**。`/init` で雛形を生成できる | foundation/curriculum.md（1章2節・3章3節） |
| REF-018 | 一次 | Claude Code: Skills | https://code.claude.com/docs/en/skills | 2026-09-02 | "Skills extend what Claude can do. Create a `SKILL.md` file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with `/skill-name`." **本文は使用時にのみ読み込まれる**（"a skill's body loads only when it's used, so long reference material costs almost nothing until you need it"）。配置は `~/.claude/skills/<name>/SKILL.md`（個人）と `.claude/skills/<name>/SKILL.md`（プロジェクト）。**カスタムコマンド（`.claude/commands/`）は skills に統合された** | foundation/curriculum.md（3章3節） |
| REF-019 | 一次 | Claude Code: Advanced setup | https://code.claude.com/docs/en/setup | 2026-09-02 | 動作要件: macOS 13.0+ / Windows 10 1809+ / Ubuntu 20.04+ / Debian 10+ / Alpine 3.19+、メモリ4GB 以上、インターネット接続必須。インストールは `curl -fsSL https://claude.ai/install.sh \| bash`（macOS・Linux・WSL）。確認は `claude --version`。Pro / Max / Team / Enterprise / Console のいずれかのアカウントが必要で、無料プランは対象外 | foundation/curriculum.md（1章3節） |

## 再確認が必要な出典

ツールのバージョンに依存する出典は、章の完了時と半年ごとに再確認する。

| ID | 再確認の理由 | 次回確認予定 |
|---|---|---|
| REF-001 | DORA は毎年の研究で capability を追加・改訂する。AI カテゴリは特に変動しやすい | 2027-02 |
| REF-002 | 年次レポートの更新により知見が差し替わる可能性がある | 2027-02 |
| REF-016〜REF-019 | ツールの公式ドキュメントであり、DORA より更新が速い。**章の完了ごとに必ず再確認する** | 2026-12 |

## 取得時の注意

REF-001 は2回の取得でカテゴリ表示が一部食い違った（`Trunk-based development` の Core 表示、`Working in small batches` の AI 表示）。**個別 capability のカテゴリを教材に書く場合は、カタログではなく各 capability のページで確認する。**

Claude Code のドキュメントは `docs.claude.com/en/docs/claude-code/*` から `code.claude.com/docs/en/*` へ移動している（2026-09-02 時点で 301 リダイレクト）。**台帳には移動後の URL を記録する。**

**教材に書くツールの挙動は、記述時点の最新版で確認する。** 2026-09-02 に手元で確認したバージョンは `2.1.258`。ネイティブインストールは背景で自動更新されるため、確認日とバージョンの両方を frontmatter の `tool_version` に残す。
