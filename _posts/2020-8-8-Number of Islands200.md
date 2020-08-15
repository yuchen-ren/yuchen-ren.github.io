---
layout:     post
title:      "Leetcode200"
subtitle:   "岛屿数量"
date:       2020-8-8 23:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 






示例 1：
```
输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
```

示例 2：
```
输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
```


###DFS




### python的code如下：


```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            if x>=0 and x<row and y>=0 and y<col and grid[x][y]=='1':              
                grid[x][y]='2'
                for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    dfs(x+i,y+j)
            return 
        row=len(grid)
        if row==0:
            return 0
        count=0
        col=len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    dfs(r,c)
                    count+=1      
        return count
```
执行用时：68 ms, 在所有 Python3 提交中击败了94.57%的用户

内存消耗：14.4 MB, 在所有 Python3 提交中击败了47.97%的用户