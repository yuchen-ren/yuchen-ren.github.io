---
layout:     post
title:      "Leetcode289"
subtitle:   "生命游戏"
date:       2020-4-2 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。



示例1：
```
输入： 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出：
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
```

进阶：

你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？

###暴力遍历

用额外数组来保存初始的状态(注意需要深拷贝)。

时间复杂度：O(m*n)。
空间复杂度：O(m*n)。
### python的code如下：


```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy=copy.deepcopy(board)
        m,n=len(board),len(board[0])
        dirs=[(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        for i in range(m):
            for j in range(n):
                live=0
                for d in dirs:
                    x,y=i+d[0],j+d[1]
                    if x<0 or x>=m or y<0 or y>=n:
                        continue
                    if board_copy[x][y]==1:
                        live+=1
                if live<2 or live>3:
                    board[i][j]=0
                elif live==3 and board_copy[i][j]==0:
                    board[i][j]=1
```
执行用时 :40 ms, 在所有 Python3 提交中击败了60.31%的用户

内存消耗 :13.6 MB, 在所有 Python3 提交中击败了9.52%的用户

###原地标记算法
1——保持1
-1——1转0
0——保持0
-2——0转1


时间复杂度：O(m*n)。

空间复杂度：O(1)。
### python的code如下：


```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        1——保持1
        -1——1转0
        0——保持0
        -2——0转1
        """
        m,n=len(board),len(board[0])
        dirs=[(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        for i in range(m):
            for j in range(n):
                live=0
                for d in dirs:
                    x,y=i+d[0],j+d[1]
                    if x<0 or x>=m or y<0 or y>=n:
                        continue
                    if board[x][y]==1 or board[x][y]==-1:
                        live+=1
                if board[i][j]==1 and (live<2 or live>3)  :
                    board[i][j]=-1
                elif board[i][j]==0 and live==3:
                    board[i][j]=-2
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==-2:
                    board[i][j]=1
```
执行用时 :40 ms, 在所有 Python3 提交中击败了60.76%的用户

内存消耗 :13.6 MB, 在所有 Python3 提交中击败了10.53%的用户


###cv中的卷积操作

[参考链接](https://leetcode-cn.com/problems/game-of-life/solution/xiong-mao-shua-ti-python3-bao-xue-bao-hui-cvzhong-/)

时间复杂度：O(m*n)。
空间复杂度：O(m*n)。
### python的code如下：


```python
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        import numpy as np
        m,n=len(board),len(board[0])
        #下面两行做zero padding
        board_exp=np.array([[0 for _ in range(n+2)] for _ in range(m+2)])
        board_exp[1:1+m,1:1+n]=np.array(board)
        #设置卷积核
        kernel=np.array([[1,1,1],[1,0,1],[1,1,1]])
        #开始卷积
        for i in range(1,m+1):
            for j in range(1,n+1):
                live=np.sum(kernel*board_exp[i-1:i+2,j-1:j+2])
                if board_exp[i,j]==1:
                    if live<2 or live>3:
                        board[i-1][j-1]=0
                else:
                    if live==3:
                        board[i-1][j-1]=1
```
执行用时 :100 ms, 在所有 Python3 提交中击败了6.56%的用户

内存消耗 :29.4 MB, 在所有 Python3 提交中击败了10.53%的用户
