---
layout:     post
title:      "Leetcode8"
subtitle:   "字符串转换整数 (atoi)"
date:       2020-4-3 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。




示例1：
```
输入: "42"
输出: 42
```
示例2：
```
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
```
示例3：
```
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
```
示例4：
```
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
```
示例5：
```
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。
```

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
