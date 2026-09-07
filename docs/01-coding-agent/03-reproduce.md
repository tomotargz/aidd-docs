---
title: 自分の環境で再現する
chapter: 1
section: 3
status: draft
updated: 2026-09-08
sources:
  - REF-019
  - REF-020
tool_version:
  claude_code: "2.1.263"
demo_source: demos/ch01-02-shop
demo_verified:
  date: 2026-09-08
  os: macOS 15
---

# 自分の環境で再現する

## はじめに

2節で見たループは、自分のリポジトリで同じように再現できます。

この節では手を動かします。2節と同じ題材を作り、同じ指示を出し、途中で止める操作と取り消す操作まで試します。所要時間は20分です。

インストールと認証は済んでいるものとします。まだの場合は公式ドキュメントの手順で完了させてください。案内は次の囲みにあります。

> [!NOTE]
> **Claude Code v2.1.263 時点** — この節に出てくるコマンドとキー操作は、すべてClaude Codeのものです。ほかのコーディングエージェントでは異なります。
> インストールは`curl -fsSL https://claude.ai/install.sh | bash`（macOS・Linux・WSL）で行います。Windowsの手順は出典のページにあります。
> 利用にはPro、Max、Team、Enterprise、Consoleのいずれかのアカウントが必要です。無料プランは対象外です。認証は`claude`を起動してブラウザの指示に従います。
> 出典: https://code.claude.com/docs/en/setup （2026-09-07 確認）

## 動くことを確かめる

作業を始める前に、Claude Codeが動く状態かを2つのコマンドで確かめます。

1つ目はバージョンの表示です。

```
$ claude --version
2.1.263 (Claude Code)
```

2つ目は設定の診断です。セッションを開始せず、インストールと設定の状態だけを表示します。

```
$ claude doctor
Claude Code doctor

Running: native (2.1.263)
Platform: darwin-arm64
Search: OK (bundled)
Auto-updates: enabled
（環境の情報が数行続きます）

No installation issues found.
```

`No installation issues found.`が出れば次に進めます。バージョンが表示されない場合や問題が報告された場合は、前の囲みの出典にある手順を確認してください。

## 題材を用意する

2節と同じ3つのファイルを、空のディレクトリに作ります。

```
$ mkdir price-demo
$ cd price-demo
```

`price.py`、`test_price.py`、`CLAUDE.md`の3つを、2節に載せた内容で作成します。作成したら、Gitのリポジトリにして最初のコミットを入れます。

```
$ git init
$ git add .
$ git commit -m "初期状態"
```

コミットしておくのは、あとで`git diff`を使い、エージェントが何を変えたかを見るためです。

テストが1件失敗することを先に確かめます。

```
$ python3 -m unittest
.F
（省略）
FAILED (failures=1)
```

失敗が1件出れば、2節と同じ出発点に立てています。

## 任せてみる

リポジトリのディレクトリでエージェントを起動します。

```
$ claude
```

初めて開くディレクトリでは、そのフォルダを信頼するかの確認が出ます。

```
Quick safety check: Is this a project you created or one you trust?

❯ No, exit
  Yes, I trust this folder

Enter to confirm · Esc to cancel
```

選択されているのは`No, exit`です。そのままEnterを押すと終了します。矢印キーで`Yes, I trust this folder`に移し、Enterを押してください。

起動すると、画面の下に現在の権限モードが出ます。

```
⏵⏵ auto mode on (shift+tab to cycle)
```

ここで2節と同じ1文を入力します。

```
> 失敗しているテストを直してください
```

エージェントがファイルを読み、テストを実行し、`price.py`を書き換え、テストを実行し直します。完了すると報告が出て、入力を待つ状態に戻ります。

2節と同じ手順を踏んでも、実行されるコマンドと回数は同じになりません。エージェントは毎回その場で判断します。確かめるのは、テストが通ったかどうかと、変更が`price.py`の1行に収まっているかどうかです。

終わったら`git diff`で変更を確認します。

```
$ git diff
```

## 途中で止める

エージェントが動いている最中に`Esc`を押すと、その場で止まります。

実行中のツールの呼び出しは取り消され、エージェントは次の指示を待ちます。画面には次の表示が出ます。

```
⎿  Interrupted · What should Claude do instead?
```

2節で「途中のどの時点でも割り込める」と述べたのは、この操作のことです。

止めずに方向だけ変えることもできます。訂正を入力して`Enter`を押すと、いま動いている操作は続き、その操作が終わった時点でエージェントが訂正を読みます。

試すときは、もう一度同じ指示を出し、エージェントが最初のコマンドを実行したあたりで`Esc`を押してください。止まったことを確認したら、続きを指示するか、次の手順に進みます。

## 変更を取り消す

`Esc`を2回押すと、どこまで巻き戻すかを選ぶ画面が出ます。

```
Rewind
Restore the code and/or conversation to the point before…

  失敗しているテストを直してください
  No code changes
❯ (current)

Enter to continue · Esc to cancel
```

戻したい時点を矢印キーで選び、Enterで確定します。何もせずに閉じる場合は`Esc`を押します。コードだけを戻すか、会話も戻すかも選べます。

Claude Codeはファイルを編集する前に、そのファイルの内容を保存しています。巻き戻しはこの保存された内容を使います。「元に戻して」と言葉で頼むこともできます。

巻き戻せる範囲には限りがあります。

1. 対象はファイルの変更だけです。
2. データベース、API、デプロイのように、外部のシステムに及んだ操作は戻せません。
3. Gitとは別の仕組みです。コミットは変わりません。

外部に及ぶ操作を戻せないことが、次の操作を必要にします。

## 実行を許可するかを決める

`Shift+Tab`を押すと、エージェントに何を許可するかのモードを切り替えられます。

モードは4つあります。

1. Auto。多くの操作を背後で判定し、危険なものだけを止めます。Pro、Max、Teamプランのターミナルでの初期モードです。
2. Manual。ファイルの編集とシェルコマンドの実行の前に、毎回確認を求めます。
3. Accept edits。ファイルの編集と`mkdir`、`mv`のような操作は確認せずに行い、それ以外のコマンドでは確認を求めます。
4. Plan。ファイルを変更せず、調べて計画を提案するところまでを行います。

`Shift+Tab`を1回ずつ押すと、画面の下の表示がこの順に変わります。

```
⏵⏵ auto mode on (shift+tab to cycle)
⏸  manual mode on
⏵⏵ accept edits on (shift+tab to cycle)
⏸  plan mode on (shift+tab to cycle)
```

4回押すとautoに戻ります。表示が一巡することを確認できれば十分です。

どのモードで作業するか、チームでどう揃えるかは、この節では決めません。人の確認をどこに置くかは4章で扱います。

## 環境による差

ここまでの手順は、環境によって結果が変わる箇所が3つあります。

1. OSです。macOSは13.0以降、Windowsは10 1809以降、Ubuntuは20.04以降、Debianは10以降、Alpineは3.19以降が必要です。WindowsではWSLを使う選択肢もあります。
2. シェルです。Bash、Zsh、PowerShell、CMDが使えます。この節の表示例はmacOSのZshのものです。
3. Pythonです。`python3 -m unittest`が動くことを前提にしています。`python3`が見つからない場合は、Pythonを入れるか、コマンド名を環境に合わせてください。

エージェント自身も環境の差を踏むことがあります。2節では、エージェントが最初に実行した`ls`のオプションがmacOSで通らず、別のコマンドで取り直していました。

> [!NOTE]
> **Claude Code v2.1.263 時点** — 割り込み、巻き戻し、権限モードの記述はこのページによります。割り込みは`Esc`、巻き戻しは`Esc`を2回、権限モードの切り替えは`Shift+Tab`です。チェックポイントはgitとは別の仕組みで、会話を再開しても残ります。
> 動作環境の要件は https://code.claude.com/docs/en/setup によります。
> 出典: https://code.claude.com/docs/en/how-claude-code-works （2026-09-07 確認）
