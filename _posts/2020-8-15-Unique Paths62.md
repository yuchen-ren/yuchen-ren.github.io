---
layout:     post
title:      "Leetcode62"
subtitle:   "不同路径"
date:       2020-8-15 21:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？




示例 1：
```
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
```

示例 2：
```
输入: m = 7, n = 3
输出: 28
```

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9
###动态规划

把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。

时间复杂度：O(m*n)。


空间复杂度：O(m*n)。

### python的code如下：


```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
```
执行用时：44 ms, 在所有 Python3 提交中击败了50.67%的用户

内存消耗：13.5 MB, 在所有 Python3 提交中击败了91.35%的用户


