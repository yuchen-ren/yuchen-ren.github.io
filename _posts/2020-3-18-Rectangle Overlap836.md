---
layout:     post
title:      "Leetcode836"
subtitle:   "矩形重叠"
date:       2020-3-18 00:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。

如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。




示例1：
```
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true
```
示例2：
```
输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false
```
说明：

两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
矩形中的所有坐标都处于 -10^9 和 10^9 之间。


##利用不重叠部分


求重叠部分的话，可以通过找非重叠以外的情况。

非重叠一共有四种情况，如下：

矩形 rec1 在矩形 rec2 的左侧；

矩形 rec1 在矩形 rec2 的右侧；

矩形 rec1 在矩形 rec2 的上方；

矩形 rec1 在矩形 rec2 的下方。



时间复杂度：O(1)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0]>=rec2[2] or rec2[0]>=rec1[2] or rec1[1]>=rec2[3] or rec2[1]>=rec1[3]:
            return False
        else:
            return True
```
执行用时 :32 ms, 在所有 Python3 提交中击败了70.00%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.77%的用户
##一维投影

如果两个矩形重叠，代表了两个矩形与x轴平行的边投影到x轴上时会有交集，与y轴平行的边投影到y轴上时也会有交集。
因此，我们可以将问题看作一维线段是否有交集的问题。


时间复杂度：O(1)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if min(rec1[2],rec2[2])>max(rec1[0],rec2[0])and min(rec1[3],rec2[3])>max(rec1[1],rec2[1]):
            return True
        else:
            return False
```
执行用时 :28 ms, 在所有 Python3 提交中击败了89.31%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.77%的用户