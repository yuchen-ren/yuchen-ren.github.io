---
layout:     post
title:      "Leetcode35"
subtitle:   "链表的中间结点"
date:       2020-3-23 14:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例1：
```
输入: [1,3,5,6], 5
输出: 2
```
示例2：
```
输入: [1,3,5,6], 2
输出: 1
```
示例3：
```
输入: [1,3,5,6], 7
输出: 4
```
示例4：
```
输入: [1,3,5,6], 0
输出: 0
```

##二分搜索
每次都以数组的中间位置寻找，并且记录位置。


时间复杂度：O(logn)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lens=len(nums)
        mid=(lens-1)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            if lens==1 or mid==0:
                return 0
            return self.searchInsert(nums[:mid],target)
        else:
            if lens==1 or mid==lens:
                return 1
            return mid+1+self.searchInsert(nums[mid+1:],target)
```
执行用时 :32 ms, 在所有 Python3 提交中击败了97.52%的用户

内存消耗 :14 MB, 在所有 Python3 提交中击败了5.05%的用户

