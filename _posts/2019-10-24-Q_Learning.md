---
layout: post
title: "Q_Learning"
subtitle: "Why is there more uncomputable functions?"
date:   2019-10-25
author: "TerryRen"
header-img: "img/post-bg-infinity.jpg"
header-mask: 0.3
mathjax: true
tags:
  - ReinforcementLearning

---
off-policy
首先，我们会初始化一个Q-table，可以是全0或者是其他的数值，一般都是全0，然后我们设定训练的轮数episodes，这里从初始状态直到终止状态算作一轮。那么在每一轮中，我们会有一个初始状态，然后会不断的采取动作，这里每一个动作叫做一个step。

$\alpha$是学习率，学习速率α越大，保留之前训练的效果就越少，如果学习率是1的话，完全用新学到的q值替换掉了原来的q值。
$\gamma$是贪婪greedy的值。
在每一个step中，我们根据当前的状态通过一定的策略选择动作A，这里的策略可能是以$\gamma$0.9的概率选择Q-table中当前状态对应的q值最大的动作，以0.1的概率选择随机动作。然后在选择动作A之后，我们可以得到奖励值R和新的状态S
Q_Learning公式如下：


$$
Q(S,A) \leftarrow Q(S,A)+\alpha[R+\gamma max_aQ(S',a)-Q(S,A)]
$$

