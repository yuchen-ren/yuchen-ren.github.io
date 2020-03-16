---
layout:     post
title:      "Leetcode75"
subtitle:   "颜色分类"
date:       2020-3-16 14:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。


示例：
```
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
```

进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？


##扫描个数重写数组

时间复杂度：O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fre=[0]*3
        for value in nums:
            if value==0:fre[0]+=1
            elif value==1:fre[1]+=1
            elif value==2:fre[2]+=1
        nums[:fre[0]]=[0]*fre[0]
        nums[fre[0]:fre[0]+fre[1]]=[1]*fre[1]
        nums[fre[0]+fre[1]:]=[2]*fre[2]
```
执行用时 :36 ms, 在所有 Python3 提交中击败了70.22%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.14%的用户
### c++的code如下：

```c

```
##三指针快排

用三个指针（p0,p2和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。

只扫描一遍数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p2]互换。

时间复杂度：O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens=len(nums)
        p0=0
        p2=lens-1
        cur=0
        while cur<=p2:
            if nums[cur]==0:
                nums[p0],nums[cur]=nums[cur],nums[p0]
                p0+=1
                cur+=1
            elif nums[cur]==2:
                nums[p2],nums[cur]=nums[cur],nums[p2]
                p2-=1 #等于2的情况不能cur+1，因为cur还没有扫描过后面的数
            elif nums[cur]==1:
                cur+=1

```
执行用时 :32 ms, 在所有 Python3 提交中击败了87.15%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.14%的用户
### c++的code如下：

```c

```