---
layout:     post
title:      "Leetcode面试题 08.02"
subtitle:   "迷路的机器人"
date:       2020-7-14 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。


网格中的障碍物和空位置分别用 1 和 0 来表示。

返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。

示例1：
```
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
解释: 
输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
```
说明：r 和 c 的值均不超过 100。


##动态规划
dp[i]=dp[i-1]+dp[i-2]+dp[i-3]


时间复杂度：O(n)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def waysToStep(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        dp=[0]*n
        dp[0],dp[1],dp[2]=1,2,4
        for i in range(3,n):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000007
        return dp[n-1]
```
执行用时：576 ms, 在所有 Python3 提交中击败了47.93%的用户

内存消耗：50.4 MB, 在所有 Python3 提交中击败了100.00%的用户