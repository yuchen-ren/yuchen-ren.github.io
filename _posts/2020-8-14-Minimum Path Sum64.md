---
layout:     post
title:      "Leetcode64"
subtitle:   "最小路径和"
date:       2020-8-14 19:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



 




示例 1：
```
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
```


###动态规划

时间复杂度：O(n^2)。


空间复杂度：O(n^2)。

### python的code如下：


```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        dp=[[float('inf')]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0:
                    dp[i][j]=grid[i][j]+dp[i][j-1]
                elif j==0:
                    dp[i][j]=grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]
```
执行用时：56 ms, 在所有 Python3 提交中击败了81.83%的用户

内存消耗：15.1 MB, 在所有 Python3 提交中击败了32.40%的用户
###动态规划优化

时间复杂度：O(n^2)。


空间复杂度：O(1)。

### python的code如下：


```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    grid[i][j]=grid[i][j]
                elif i==0:
                    grid[i][j]=grid[i][j]+grid[i][j-1]
                elif j==0:
                    grid[i][j]=grid[i][j]+grid[i-1][j]
                else:
                    grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]
```
执行用时：52 ms, 在所有 Python3 提交中击败了93.04%的用户

内存消耗：14.9 MB, 在所有 Python3 提交中击败了73.46%的用户