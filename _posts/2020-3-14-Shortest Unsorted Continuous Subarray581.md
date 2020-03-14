---
layout:     post
title:      "Leetcode581"
subtitle:   " 最短无序连续子数组"
date:       2020-3-13 18:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。


示例 1：
```
输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
```
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。


##排序找不同
再建一个排好序的数组，找到两个边界。

时间复杂度：O(nlogn)

空间复杂度：O(n)

(复杂度取决于python自带的sorted函数，用的方法是Timesort)
### python的code如下：


```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lens=len(nums)
        sort_nums=sorted(nums)
        left,right=lens,0       
        for i in range(lens):
            if sort_nums[i]!=nums[i]:
                left=min(left,i)
                right=max(right,i)
        return right-left+1 if right>=left else 0
```
执行用时 :160 ms, 在所有 Python3 提交中击败了76.59%的用户

内存消耗 :15.1 MB, 在所有 Python3 提交中击败了5.04%的用户
### c++的code如下：

```c

```
##暴力循环
寻找右边界：如果rightmax大于nums[i]，就更新rightmax；否则将右边界更新为i。
寻找左边界：如果leftmin小于nums[lens-i-1]，就更新leftmin；否则将左边界更新为lens-i-1。

时间复杂度：O(n)

空间复杂度：O(1)

### python的code如下：


```python
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lens=len(nums)
        left,right=1,0
        leftmin=nums[lens-1]
        rightmax=nums[0]
        for i in range(lens):
            if rightmax<=nums[i]:
                rightmax=nums[i]
            else: right=i
            if leftmin>=nums[lens-1-i]:
                leftmin=nums[lens-1-i]
            else: left=lens-1-i
        return right-left+1
```
执行用时 :240 ms, 在所有 Python3 提交中击败了74.43%的用户

内存消耗 :14.6 MB, 在所有 Python3 提交中击败了5.56%的用户

