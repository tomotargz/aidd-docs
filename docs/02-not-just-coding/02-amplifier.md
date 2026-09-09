---
title: AIは増幅器である
chapter: 2
section: 2
status: fixed
updated: 2026-09-09
sources:
  - REF-002
  - REF-014
  - REF-028
  - REF-029
  - REF-030
---

# AIは増幅器である

## はじめに

1節では、エージェントが速くしたのがコーディングだけであり、その先で検査の列が長くなることを確かめました。この節では、なぜ速さだけが増えるのではないのか、そして何がその大きさを決めるのかを扱います。

答えの起点は、0章で一度引用したDORAの一文です。ここでは根拠として展開します。

## 増幅器は、いまあるものを大きくする

増幅器は、入ってきたものを大きくして出す装置です。

音の増幅器なら、演奏も雑音も同じように大きくなります。DORAはAIをこの増幅器にたとえています。

> "AI acts as an amplifier, but the greatest returns come from focusing on the underlying sociotechnical systems."
> 出典: https://dora.dev/research/?view=detail （2026-09-08 確認）

AIは増幅器として働くが、最も大きな成果は、その下にある人と技術の仕組みに手を入れたときに得られる、と述べています。

何が大きくなるのかも、DORAは書いています。

> "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses."
> 出典: https://dora.dev/research/2025/dora-report/ （2026-09-09 確認）

AIの主な役割は増幅器であり、組織にいまある強みと弱みを大きくする、と述べています。大きくなるのは強みだけではありません。

## 強みだけでなく弱みも大きくなる

AIの利用が進んでいる組織では、届ける量と不安定さの両方が高い傾向があります。

1節でも引いたDORAの一文を、ここでは2つの指標に分けて見ます。

> "higher AI adoption is associated with an increase in both software delivery throughput and software delivery instability."
> 出典: https://dora.dev/insights/balancing-ai-tensions/ （2026-09-09 確認）

AIの導入が進んでいることは、届ける量が増えていることと、不安定さが増していることの両方に関連している、と述べています。

届ける量とは、一定の期間に本番へ届けた変更の量です。不安定さとは、届けた変更が問題を起こす割合です。上がるのは片方だけではありません。

1節で見た検査の列は、届ける量が上がることの帰結です。コードを書く速さが上がると、確かめる対象も増えます。確かめる側の能力が変わらなければ、列は長くなります。

不安定さが上がるのは、AIが新しい欠陥を持ち込むからではありません。確かめる力が足りないという、もともとあった弱みが、量が増えたことで表に出るからです。

## 下地が結果を決める

同じエージェントを入れても、下地が違えば結果は変わります。

下地とは、エージェントの外側にある、人とツールと手順の組み合わせです。DORAの一文の後半にある"underlying sociotechnical systems"がこれにあたります。この言い換えは教材独自のもので、DORAが定義しているわけではありません。

下地の代表例は、エージェントに渡せる情報です。DORAは、内部のデータにAIが直接アクセスできることの効果をこう述べています。

> "giving teams AI tools that can access internal data directly amplifies the positive impact of AI adoption, serving as a statistically significant multiplier for individual effectiveness and code quality"
> 出典: https://dora.dev/capabilities/ai-accessible-internal-data/ （2026-09-09 確認）

内部のデータに直接アクセスできるAIツールをチームに与えることは、AI導入の効果を増幅し、個人の生産性とコードの品質に対して統計的に有意な倍率として働く、と述べています。

渡せる情報がなければ、AIは足りない前提を補って書きます。1章2節で置いた`CLAUDE.md`は、渡せる情報の一例です。テストコードのないリポジトリでは、エージェントが変更を確かめる手段も増えません。

文書の品質をどう上げ、エージェントに何を渡すかは、3章で扱います。

## ボトルネックの側を変える

ボトルネックがコーディングの外にあるなら、書く速さを上げても全体は変わりません。

増幅器はコーディングの速さを上げます。しかし1節で見たとおり、変更が届くまでには、レビュー、テスト、統合、リリースが残ります。この4つの工程のどれかがボトルネックなら、上流を速くしても、その手前に変更が溜まるだけです。

変えるべきなのは、ボトルネックの側です。3章から先では、ボトルネックになりうる場所ごとに何をすればよいかを扱います。

## この節で確かめたこと

AIは増幅器であり、いまある強みと弱みを大きくします。

大きくなるのは速さだけではありません。届ける量が増えれば、確かめる量も、問題が起きる割合も上がります。

ボトルネックがコーディングの外にあるなら、書く速さを上げても全体は変わりません。変えるべきなのはボトルネックの側です。

ボトルネックになりうる場所ごとに何をすればよいかを、次の節で示します。
