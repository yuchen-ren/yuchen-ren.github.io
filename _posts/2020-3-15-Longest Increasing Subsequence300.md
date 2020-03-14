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

(复杂度取决于python自带的sort函数，用的方法是Timesort)
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

##摩尔投票法
如果我们把众数记为+1，把其他数记为-1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。
遇到相同的数，就投一票，遇到不同的数，就减一票，最后还存在票的数就是众数。

时间复杂度：O(n)

空间复杂度：O(1)


### python的code如下：


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:              
        lens=len(nums)
        count=1
        candidate=nums[0]
        for i in range(1,lens):
            if count==0:
                candidate=nums[i]
            if candidate==nums[i]:
                count+=1
            else:
                count-=1
        return candidate
```

执行用时 :48 ms, 在所有 Python3 提交中击败了92.78%的用户

内存消耗 :15.1 MB, 在所有 Python3 提交中击败了5.04%的用户