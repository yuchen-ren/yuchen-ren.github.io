---
layout:     post
title:      "Leetcode54"
subtitle:   "螺旋矩阵"
date:       2020-3-16 18:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

注意:
不能使用代码库中的排序函数来解决这道题。


示例1：
```
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
```
示例2：
```
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
```

##扫描个数重写数组

设置上下左右四个边界，新数组按照从左至右，从上至下，从右至左，从下至上的顺序循环扩充。
所以每次遍历时遍历的行或列进行加一或者减一，逐渐缩小边界的范围。

时间复杂度：O(m*n)。


空间复杂度：O(m*n)。


### python的code如下：


```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        if not matrix:
            return res
        count=0
        m=len(matrix)
        n=len(matrix[0])
        left,right,up,down=0,n,0,m
        while True:
            if count==m*n: break
            for i in range(left,right):
                res.append(matrix[up][i])         
                count+=1
            up+=1
            if count==m*n: break
            for j in range(up,down):
                res.append(matrix[j][right-1])
                count+=1
            right-=1
            if count==m*n: break
            for k in range(right-1,left-1,-1):
                res.append(matrix[down-1][k])
                count+=1
            down-=1
            if count==m*n: break
            for l in range(down-1,up-1,-1):
                res.append(matrix[l][left])
                count+=1
            left+=1
        return res
```

执行用时：36 ms, 在所有 Python3 提交中击败了84.48%的用户

内存消耗：13.7 MB, 在所有 Python3 提交中击败了49.54%的用户

### c++的code如下：

```c

```
