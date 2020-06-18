---
layout:     post
title:      "Leetcode704"
subtitle:   "二分查找"
date:       2020-6-17 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个n个元素有序的（升序）整型数组nums和一个目标值target，写一个函数搜索nums中的target，如果目标值存在返回下标，否则返回 -1。






示例 1：
```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```
示例 2：
```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```
提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。


###分治递归



时间复杂度：O(logn)。
我们可以列出归并排序运行时间 T(n)的递归表达式：
T(n)=T(n/2)+O(1)
​根据主定理我们可以得出时间复杂度为O(logn)。

空间复杂度：O(1)。



### python的code如下：


```python
class Solution:
    def split(self,nums,target,index):
        n=len(nums)
        if n==1:
            if nums[0]==target:
                return index
            else:
                return -1
        else:
            mid=n//2  
        if nums[mid]==target:
            index+=mid
            return index
        elif nums[mid]<target:
            if mid+1==n:
                return -1
            else:                
                index=self.split(nums[mid+1:],target,mid+index+1)
        else:
            index=self.split(nums[:mid],target,index)
        return index
    def search(self, nums: List[int], target: int) -> int:
        return self.split(nums,target,0)
```
执行用时 :304 ms, 在所有 Python3 提交中击败了72.86%的用户

内存消耗 :15 MB, 在所有 Python3 提交中击败了6.67%的用户

###分治迭代



时间复杂度：O(nlogn)。

空间复杂度：O(1)。



### python的code如下：


```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right+left) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```
执行用时 :316 ms, 在所有 Python3 提交中击败了47.88%的用户

内存消耗 :15 MB, 在所有 Python3 提交中击败了6.67%的用户