---
layout:     post
title:      "Leetcode223"
subtitle:   "矩形面积"
date:       2020-3-18 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。




示例：
```
输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
```

说明: 假设矩形面积不会超出 int 的范围。



##一维投影

如果两个矩形重叠，代表了两个矩形与x轴平行的边投影到x轴上时会有交集，与y轴平行的边投影到y轴上时也会有交集。
因此，我们可以用投影的交集来求重合部分的面积。


时间复杂度：O(1)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        S1=(C-A)*(D-B)
        S2=(G-E)*(H-F)
        if min(C,G)>max(A,E) and min(D,H)>max(B,F):
            overlap=(min(C,G)-max(A,E))* (min(D,H)-max(B,F))     
            return S1+S2-overlap
        else:
            return S1+S2
```
执行用时 :52 ms, 在所有 Python3 提交中击败了87.46%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了5.36%的用户