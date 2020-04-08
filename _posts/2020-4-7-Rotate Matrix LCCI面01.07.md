---
layout:     post
title:      "Leetcode面试题 01.07"
subtitle:   "旋转矩阵"
date:       2020-4-7 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一幅由N × N矩阵表示的图像，其中每个像素的大小为4字节，编写一种方法，将图像旋转90度。

不占用额外内存空间能否做到？

示例1：
```
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

```
示例2：
```
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

```
###额外数组
新矩阵与原来矩阵之间坐标的关系：
new_x=y，
new_y=N-1-x。

用一个额外数组来保存源数组，在新的数组上计算对应关系。


时间复杂度：O(n²）。

空间复杂度：O(n²）。




### python的code如下：


```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        matrix_copy=copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j]=matrix_copy[n-1-j][i]
```
执行用时 :40 ms, 在所有 Python3 提交中击败了60.92%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户

###不使用额外空间

不使用额外空间就不能像之前那样一步得到计算关系，我们可以拆成两步，即先根据对角线对称，然后每一行再根据每一行的中点对称。

时间复杂度：O(n²）。

空间复杂度：O(1）。
### python的code如下：


```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        mid=n//2
        for i in range(n):
            for j in range(mid):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]
```
执行用时 :36 ms, 在所有 Python3 提交中击败了80.33%的用户

内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户