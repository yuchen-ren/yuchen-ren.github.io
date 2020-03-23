---
layout:     post
title:      "Leetcode面试题 17.16"
subtitle:   "按摩师"
date:       2020-3-24 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。



示例1：
```
输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
```
示例2：
```
输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
```
示例3：
```
输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
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

