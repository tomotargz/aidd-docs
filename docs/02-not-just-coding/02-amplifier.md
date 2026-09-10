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

この節では、AIは増幅器であるというDORAの主張を掘り下げます。

> "AI acts as an amplifier, but the greatest returns come from focusing on the underlying sociotechnical systems."
> 訳: AIは増幅器として働くが、最も大きな成果は、その下にある人と技術の仕組みに注目したときに得られる。
> 出典: https://dora.dev/research/?view=detail （2026-09-08 確認）

## 増幅器とは

増幅器とは、入力されたものを大きくして出力する装置です。

大きくなるのは良い部分だけではありません。音の増幅器なら、音楽だけでなく雑音も同じように大きくします。

増幅器として見たとき、AIは組織の強みだけでなく、弱みも大きくして出力します。

> "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses."
> 訳: AIの主な役割は増幅器であり、組織にいまある強みと弱みを大きくする。
> 出典: https://dora.dev/research/2025/dora-report/ （2026-09-09 確認）

## 強みだけでなく弱みも大きくなる

弱みが増幅される一例は、AIの利用が進む組織では、スループットだけでなく不安定さも高まる傾向があることです。

> "higher AI adoption is associated with an increase in both software delivery throughput and software delivery instability."
> 訳: AIの導入が進んでいることは、スループットが増えていることと、不安定さが増していることの両方に関連している。
> 出典: https://dora.dev/insights/balancing-ai-tensions/ （2026-09-09 確認）

スループットとは、一定の期間にリリースした変更の量です。不安定さとは、リリースした変更が問題を起こす割合です。AIを利用することで、スループットが上がりますが、不安定さも上がってしまいます。

不安定さも高まるのは、エージェントにより高まる負荷に検査の工程が耐えきれなくなるからです。エージェントを使うと変更の量が増えるので、検査に負荷がかかります。検査が負荷に耐えきれないと、待ち行列を作ってしまうか、検査精度を落として無理にスループットを上げようとします。検査精度を落とすと、問題のあるコードがリリースされることが増え、不安定さが高まります。

不安定さの高まりは、高負荷に耐えられないという検査工程の弱みが、AIにより増幅され表出したと考えることができます。

## 土台が結果を決める

同じようにAIを導入したとしても、土台により結果は異なります。

先に挙げた検査工程の他に、AIがアクセスできる情報も土台のひとつです。

> "giving teams AI tools that can access internal data directly amplifies the positive impact of AI adoption, serving as a statistically significant multiplier for individual effectiveness and code quality"
> 訳: 内部のデータに直接アクセスできるAIツールをチームに与えることは、AI導入の効果を増幅し、個人の生産性とコードの品質に対して統計的に有意な倍率として働く。
> 出典: https://dora.dev/capabilities/ai-accessible-internal-data/ （2026-09-09 確認）

アクセスできる情報が少なければ、エージェントは足りない情報を補ってコードを出力します。テストコードはエージェントに渡せる情報の一例です。テストコードがあれば、エージェントは変更に問題がないか機械的に判断できるので、正しくコードを生成しやすくなります。テストコードがなくてもエージェントはコードを生成できますが、問題が含まれる可能性は高まります。

エージェントに渡す情報については、3章で扱います。

## ボトルネックの側を変える

AIが増幅した弱みは、ボトルネックとして現れます。

3章から先では、ボトルネックになりうる場所ごとに何をすべきかを扱います。

## この節で確かめたこと

AIは増幅器であり、いまある強みと弱みを大きくします。

AI導入の成果を得るためには、土台を整え、ボトルネックを解消する必要があります。

ボトルネックになりうる場所ごとに何をすればよいかを、次の節で示します。
