---
layout:     post
title:      "Leetcode1162"
subtitle:   "地图分析"
date:       2020-3-29 11:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。

我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。

如果我们的地图上只有陆地或者海洋，请返回 -1。




示例1：
```
输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
```
示例2：
```
输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
```
提示：

1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1
##题意理解
找一个海洋，使得其离所有的陆地区域达到最远（是所有的，不是距离哪一个最远）。
###多源BFS

这道题实际上就是求海洋格子到陆地格子的最长路径。
### python的code如下：


```python
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        queue=[]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((i,j))
        if len(queue)==0 or len(queue)==n*n:return -1
        distance=-1
        while queue:
            distance+=1
            lens=len(queue)
            for i in range(lens):
                x,y=queue.pop(0)
                if x-1>=0 and grid[x-1][y]==0:
                    grid[x-1][y]=2
                    queue.append((x-1,y))
                if x+1<n and grid[x+1][y]==0:
                    grid[x+1][y]=2
                    queue.append((x+1,y))
                if y-1>=0 and grid[x][y-1]==0:
                    grid[x][y-1]=2
                    queue.append((x,y-1))
                if y+1<n and grid[x][y+1]==0:
                    grid[x][y+1]=2
                    queue.append((x,y+1))
        return distance
```
执行用时 :
740 ms
, 在所有 Python3 提交中击败了
60.29%
的用户
内存消耗 :
14 MB
, 在所有 Python3 提交中击败了
17.65%
的用户