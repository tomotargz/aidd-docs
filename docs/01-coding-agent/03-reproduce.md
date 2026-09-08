---
title: 自分の環境で再現する
chapter: 1
section: 3
status: fixed
updated: 2026-09-08
sources:
  - REF-019
  - REF-020
  - REF-024
  - REF-025
  - REF-026
  - REF-027
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

この節では手を動かします。2節と同じ題材を作り、同じ指示を出し、そのあとで巻き戻す・割り込む・許可のモードを切り替えるの3つの操作を試します。

インストールと認証は済んでいるものとします。まだの場合は公式ドキュメントの手順で完了させてください。案内は次の囲みにあります。

> [!NOTE]
> **Claude Code v2.1.263 時点** — この節に出てくるコマンドとキー操作は、すべてClaude Codeのものです。ほかのコーディングエージェントでは異なります。
> インストールは`curl -fsSL https://claude.ai/install.sh | bash`（macOS・Linux・WSL）で行います。Windowsの手順は出典のページにあります。
> 利用にはPro、Max、Team、Enterprise、Consoleのいずれかのアカウントが必要です。無料プランは対象外です。認証は`claude`を起動してブラウザの指示に従います。この節の手順は、いずれのプランでも再現できます。
> 出典: https://code.claude.com/docs/en/setup （2026-09-08 確認）

> [!NOTE]
> **記録について** — この節に載せる画面は、2026-09-08にmacOS 15、Zsh、Python 3.13、Claude Code v2.1.263で実際に実行した記録です。画面上の進行状況の表示と装飾は省いています。長い出力を切り詰めた箇所には「（省略）」と書きます。
> 表示は環境と契約プランで変わります。変わる箇所はその都度示します。

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
（インストール先と更新の状態が数行続きます）

No installation issues found.
```

`No installation issues found.`が出れば次に進めます。バージョンが表示されない場合や問題が報告された場合は、「はじめに」の囲みにある出典の手順を確認してください。

`Platform: darwin-arm64`は実行した環境を表します。ここが自分の環境の値になっていれば問題ありません。

## 題材を用意する

2節と同じ3つのファイルを、空のディレクトリに作ります。

```
$ mkdir demo-shop
$ cd demo-shop
```

`price.py`、`test_price.py`、`CLAUDE.md`の3つを、2節に載せた内容で作成します。`CLAUDE.md`は、テストコマンドをコードブロックで囲んだ形のまま書き写してください。

作成したらGitのリポジトリにして、最初のコミットを入れます。あとで`git diff`を使い、エージェントが何を変えたかを見るためです。

```
$ git init
$ git add .
$ git commit -m "初期状態"
```

題材が2節と同じ状態にあることを、テストの失敗で確かめます。

```
$ python3 -m unittest
.F
（省略）
FAILED (failures=1)
```

失敗が1件出れば、2節と同じ出発点に立てています。失敗が0件、または2件以上出た場合は、3つのファイルの内容を2節と照合してください。

## 任せてみる

2節と同じ1文を自分のリポジトリで入力し、テストが通るところまでエージェントに任せます。

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

初期状態のカーソルは`No, exit`にあります。そのままEnterを押すと終了します。矢印キーで`Yes, I trust this folder`に移し、Enterを押してください。

起動すると、画面の下に現在の権限モードが出ます。表示は契約プランと利用状況で変わります。

```
⏵⏵ auto mode on (shift+tab to cycle)     ← Pro・Max・Teamプランのターミナル
⏸  manual mode on                        ← Enterprise・Console、および初回起動時
```

ここで2節と同じ1文を入力します。

```
> 失敗しているテストを直してください
```

Autoの場合、エージェントはファイルを読み、テストを実行し、`price.py`を書き換え、テストを実行し直します。完了すると報告が出て、入力を待つ状態に戻ります。

Manualの場合は、ファイルの編集とコマンドの実行のたびに承認を求められます。

```
Bash command
  ls -R . | head -50 && echo "---" && python3 -m unittest 2>&1 | tail -40
  List files and run tests

This command requires approval

Do you want to proceed?
❯ 1. Yes
  2. Yes, and don't ask again for: python3 -m unittest
  3. Yes, and switch to auto mode
  4. No

Esc to cancel · Tab to amend
```

内容を読んで`1`を選ぶと、その操作だけを許可して先に進みます。この節では毎回`1`を選んでください。

再現できたかどうかは、2点で判定します。テストが通ったことと、変更が`price.py`の1行に収まっていることです。

実行されるコマンドと回数までは一致しません。同じ指示でも、エージェントが選ぶコマンドは毎回同じにはなりません。

エージェントは起動したままにしてください。次の手順で使います。変更内容は、別のターミナルを開き、同じディレクトリで`git diff`を実行して確認します。

```
$ git diff
```

2節の`git diff`と同じ1行の変更になっていれば、再現できています。

## 変更を巻き戻す

入力欄が空の状態で`Esc`を2回押すと、どこまで巻き戻すかを選ぶ画面が出ます。

入力欄に文字が残っていると、`Esc`は入力を消すだけで、この画面は出ません。`/rewind`と入力しても同じ画面が開きます。

```
Rewind
Restore the code and/or conversation to the point before…

  失敗しているテストを直してください
  No code changes
❯ (current)

Enter to continue · Esc to cancel
```

一覧には、このセッションで出した指示が並び、最後に`(current)`（いまの状態）が入ります。戻したい時点を矢印キーで選び、Enterを押すと、その時点に対して何をするかを選ぶ画面に進みます。

選べる操作は6つあります。この節で使うのは1つ目です。

1. Restore code and conversation。コードと会話の両方をその時点に戻します。
2. Restore conversation。コードはそのままにして、会話だけを戻します。
3. Restore code。会話はそのままにして、ファイルの変更だけを戻します。
4. Summarize from here。その時点から先の会話を要約に圧縮します。
5. Summarize up to here。その時点までの会話を要約に圧縮します。
6. Never mind。何もせずに一覧へ戻ります。

`失敗しているテストを直してください`を選び、`Restore code and conversation`を選んでください。`price.py`が元に戻り、テストがまた1件失敗する状態になります。

巻き戻しが成立するのは、Claude Codeがファイルを編集する前に、そのファイルの内容を保存しているためです。この保存をチェックポイントと呼びます。巻き戻しは、保存された内容を書き戻します。

同じ操作は言葉でも頼めます。「元に戻して」と入力すると、エージェントが巻き戻しを実行します。

巻き戻せる範囲には限りがあります。

1. 巻き戻せるのは、エージェントがファイル編集の機能で加えた変更だけです。`rm`や`mv`のようなシェルコマンドで起きた変更は戻せません。
2. 巻き戻しは、データベース、API、デプロイのように外部のシステムに及んだ操作を戻しません。
3. 巻き戻しはGitとは別の仕組みで、コミットを変えません。

## 途中で割り込む

エージェントが動いている最中に`Esc`を押すと、その場で止まります。

巻き戻したことで、テストはまた失敗する状態に戻っています。もう一度同じ指示を出してください。

```
> 失敗しているテストを直してください
```

エージェントが最初のコマンドを実行し、画面に`esc to interrupt`が出ている間に`Esc`を押します。次の表示が出れば止まっています。

```
⎿  Interrupted · What should Claude do instead?
```

エージェントは実行中のツールの呼び出しを取り消し、次の指示を待ちます。2節で「人が関わる3か所」の1つに挙げた途中の割り込みは、この操作のことです。

割り込む場面は3つあります。方向を変えたいとき、コンテキストを足したいとき、別のやり方を試させたいときです。

止めずに方向だけ変えることもできます。エージェントが動いている最中にそのままキーボードで訂正を打ち、`Enter`を押します。いま動いている操作は最後まで続き、その操作が終わった時点でエージェントが訂正を読みます。

## 実行を許可するかのモードを切り替える

`Shift+Tab`を押すと、エージェントに何を許可するかのモードを切り替えられます。

巻き戻しは操作のあとに効きます。外部のシステムに及んだ操作のように戻せないものを、実行される前に止められるのは権限モードだけです。

`Shift+Tab`で順に切り替わるモードは4つです。

1. Auto。ファイルの編集とコマンドの実行を自動で判定し、危険と判定したものだけ確認を求めます。Pro、Max、Teamプランのターミナルでの初期モードです。
2. Manual。ファイルの編集とシェルコマンドの実行の前に、毎回確認を求めます。
3. Accept edits。ファイルの編集と、`mkdir`や`mv`にあたるファイルシステムのコマンドを確認せずに行い、それ以外のコマンドでは確認を求めます。
4. Plan。ファイルを変更せず、調べて計画を提案するところまでを行います。

`Shift+Tab`を1回ずつ押すと、画面の下の表示がAuto、Manual、Accept edits、Planの順に変わります。

```
⏵⏵ auto mode on (shift+tab to cycle)
⏸  manual mode on
⏵⏵ accept edits on (shift+tab to cycle)
⏸  plan mode on (shift+tab to cycle)
```

4回押すとAutoに戻ります。表示が元に戻ることを確認できれば十分です。

どのモードで作業するか、チームでどう揃えるかは、この節では決めません。人の確認をどこに置くかは4章で扱います。

> [!NOTE]
> **Claude Code v2.1.263 時点** — モードは全部で6つあります。`Shift+Tab`の巡回に現れる4つのほかに、`dontAsk`と`bypassPermissions`があり、起動時のオプションでのみ選べます。`bypassPermissions`はすべての確認を省くモードです。
> 出典: https://code.claude.com/docs/en/permission-modes （2026-09-08 確認）

## 環境による差

ここまでの手順には、環境によって結果が変わる箇所が4つあります。

1. OSです。macOSは13.0以降、Windowsは10 1809以降、Ubuntuは20.04以降、Debianは10以降、Alpineは3.19以降が必要です。WindowsではWSLを使う選択肢もあります。
2. シェルです。Bash、Zsh、PowerShell、CMDが使えます。
3. Pythonです。`python3 -m unittest`が動くことを前提にしています。`python3`が見つからない場合は、Pythonを入れるか、コマンド名を環境に合わせてください。
4. 起動時の権限モードです。契約プランと、そのマシンで初めて起動したかどうかで変わります。

`Esc`と`Shift+Tab`のキー操作は、macOSでのみ確認しました。ほかのOSで同じかどうかは確認していません。

エージェント自身も環境の差につまずきます。2節では、エージェントが最初に実行した`ls`のオプションがmacOSで通らず、別のコマンドで取り直しました。

> [!NOTE]
> **Claude Code v2.1.263 時点** — 割り込み、巻き戻し、権限モードの記述の出典は次のとおりです。割り込みと権限モードは https://code.claude.com/docs/en/how-claude-code-works 、巻き戻しの操作と制限は https://code.claude.com/docs/en/checkpointing 、起動時のモードは https://code.claude.com/docs/en/permission-modes 、動作環境の要件は https://code.claude.com/docs/en/setup 、初回の信頼確認は https://code.claude.com/docs/en/security によります（いずれも 2026-09-08 確認）。
> 画面に出る文字列は公式ドキュメントに載っていないため、実行記録から引用しています。

## ここまでで再現できたこと

1章で見たことが、自分の手元でも起きることを確かめました。

`/exit`と入力するとエージェントが終了し、シェルに戻ります。最後に状態を確認してください。

```
$ python3 -m unittest
$ git diff
```

確かめたことは3つです。

1. 情報収集・変更・動作確認を、エージェントが自分で回しました。人が指示したのは1文だけです。
2. 人が関わったのは入口と出口、そして途中の割り込みの3か所でした。止めることも、戻すことも、実行を許可するかを決めることもできました。
3. 速くなったのは、コードを書く部分だけです。

自分の実務のリポジトリで同じことをすると、3つが変わります。`CLAUDE.md`がないこと、テストの実行コマンドが違うこと、変更が1行では済まないことです。1つ目と2つ目は3章で、3つ目は3章と4章で扱います。

3つ目の「速くなったのはコードを書く部分だけ」は、2章の出発点になります。
