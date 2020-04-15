---
layout:     post
title:      "Leetcode300"
subtitle:   " 最长上升子序列"
date:       2020-3-14 18:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个无序的整数数组，找到其中最长上升子序列的长度。


示例 1：
```
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
```
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


##动态规划
dp[i]来表示在nums中以第i个数结尾的最长上升子序列的长度。
在遍历nums[i]的过程中，同时看i之前的数有没有满足的最长上升子序列。

时间复杂度：O(n^2)

空间复杂度：O(n)


### python的code如下：


```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        lens=len(nums)
        dp=[1]*lens
        for i in range(lens):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)
```
执行用时 :1244 ms, 在所有 Python3 提交中击败了45.49%的用户

内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.14%的用户
### c++的code如下：

```c

```
##贪心二分
考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。

基于上面的贪心思路，我们维护一个数组 d[i]，表示长度为 i的最长上升子序列的末尾元素的最小值，用 \textit{len}len 记录目前最长上升子序列的长度，起始时 lenlen 为 11，d[1] = \textit{nums}[0]d[1]=nums[0]。



时间复杂度：O(nlogn)

空间复杂度：O(n)


### python的code如下：


```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:       
        lens=len(nums)
        if lens<2:return lens
        tail=[nums[0]]
        for i in range(1,lens):
            if nums[i]>tail[-1]:
                tail.append(nums[i])
                continue
            left=0
            right=len(tail)-1
            while left<right:
                mid=(left+right)//2
                if tail[mid]<nums[i]:
                    left=mid+1
                else:
                    right=mid
            tail[left]=nums[i]
        return len(tail)
```
执行用时 :48 ms, 在所有 Python3 提交中击败了91.52%的用户

内存消耗 :13.9 MB, 在所有 Python3 提交中击败了7.89%的用户

