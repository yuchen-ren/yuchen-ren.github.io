---
layout:     post
title:      "Leetcode892"
subtitle:   "三维形体的表面积"
date:       2020-3-25 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

请你返回最终形体的表面积。



示例1：
```
输入：[[2]]
输出：10
```
示例2：
```
输入：[[1,2],[3,4]]
输出：34
```
示例3：
```
输入：[[1,0],[0,2]]
输出：16
```
示例4：
```
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
```
提示：

1 <= N <= 50
0 <= grid[i][j] <= 50
##做减法
首先要理解题意，[参考链接](https://leetcode-cn.com/problems/surface-area-of-3d-shapes/solution/shi-li-you-tu-you-zhen-xiang-jiang-jie-yi-kan-jiu-/)
计算全部的表面积，再减去重叠的部分。

时间复杂度：O(n^2)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        area=0
        for i in range(n):
            for j in range(n):
                level=grid[i][j]
                if level>0:
                    #一个柱体中：2个底面 + 所有的正方体都贡献了4个侧表面积 
                    area+=(level<<2)+2
                    #减掉 i 与 i-1 相贴的两份表面积                  
                    if i>0:
                        print(grid[i-1][j])
                        area-=min(level,grid[i-1][j])<<1
                    #减掉 j 与 j-1 相贴的两份表面积
                    if j>0:
                        print(grid[i-1][j])
                        area-=min(level,grid[i][j-1])<<1
        return area
```
执行用时 :132 ms, 在所有 Python3 提交中击败了37.16%的用户

内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.77%的用户