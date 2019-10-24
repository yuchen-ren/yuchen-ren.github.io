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
Q_Learning公式如下：


$$
Q(S,A) \leftarrow Q(S,A)+\alhpa[R+\gammamax_aQ(S',a)-Q(S,A)]
$$

