---
layout:     post
title:      "Leetcode695"
subtitle:   " 岛屿的最大面积"
date:       2020-3-15 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)



示例 1：
```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

```
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2：
```
[[0,0,0,0,0,0,0,0]]
```
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

##DFS递归
为了确保每个土地访问不超过一次，每次经过一块土地时，将这块土地置为 0。

时间复杂度：O(R∗C)。其中 R是给定网格中的行数，C是列数。

空间复杂度：O(R∗C)，递归的深度最大可能是整个网格的大小，因此最大可能使用O(R∗C)的栈空间。


### python的code如下：


```python
class Solution:
    def dfs(self,cur_i,cur_j,grid):
        if cur_i<0 or cur_i>=len(grid) or cur_j<0 or cur_j>=len(grid[0]) or grid[cur_i][cur_j]==0:
            return 0                   
        flag=1
        grid[cur_i][cur_j]=0      
        for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
            new_y=cur_i+y
            new_x=cur_j+x
            flag+=self.dfs(new_y,new_x,grid)
        return flag
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width=len(grid)
        lens=len(grid[0])
        flag=0
        for i in range(width):
            for j in range(lens):
                flag=max(self.dfs(i,j,grid),flag)              
        return flag

```
执行用时 :184 ms, 在所有 Python3 提交中击败了37.06%的用户

内存消耗 :15.6 MB, 在所有 Python3 提交中击败了21.53%的用户
### c++的code如下：

```c

```
##DFS栈

时间复杂度：O(R∗C)。其中 R是给定网格中的行数，C是列数。

空间复杂度：O(R∗C)，递归的深度最大可能是整个网格的大小，因此最大可能使用O(R∗C)的栈空间。
### python的code如下：


```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width=len(grid)
        lens=len(grid[0])
        flag=0
        for i in range(width):
            for j in range(lens):
                cur_flag=0
                stack=[(i,j)]
                while stack:
                    cur_i,cur_j=stack.pop()             
                    if cur_i<0 or cur_i>=width or cur_j<0 or cur_j>=lens or grid[cur_i][cur_j]==0:
                        continue                
                    cur_flag+=1
                    grid[cur_i][cur_j]=0      
                    for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                        new_y=cur_i+y
                        new_x=cur_j+x
                        stack.append((new_y,new_x))
                flag=max(flag,cur_flag)
        return flag    
```
执行用时 :168 ms, 在所有 Python3 提交中击败了53.88%的用户

内存消耗 :13.6 MB, 在所有 Python3 提交中击败了68.06%的用户
##BFS队列

时间复杂度：O(R∗C)。其中 R是给定网格中的行数，C是列数。

空间复杂度：O(R∗C)，递归的深度最大可能是整个网格的大小，因此最大可能使用O(R∗C)的栈空间。
### python的code如下：


```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width=len(grid)
        lens=len(grid[0])
        flag=0
        for i in range(width):
            for j in range(lens):
                cur_flag=0
                q=collections.deque([(i,j)])
                while q:
                    cur_i,cur_j=q.popleft()             
                    if cur_i<0 or cur_i>=width or cur_j<0 or cur_j>=lens or grid[cur_i][cur_j]==0:
                        continue                
                    cur_flag+=1
                    grid[cur_i][cur_j]=0      
                    for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                        new_y=cur_i+y
                        new_x=cur_j+x
                        q.append((new_y,new_x))
                flag=max(flag,cur_flag)
        return flag    
```

执行用时 :172 ms, 在所有 Python3 提交中击败了49.29%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了68.06%的用户