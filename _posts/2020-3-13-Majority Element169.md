---
layout:     post
title:      "Leetcode169"
subtitle:   " 多数元素"
date:       2020-3-13 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于[n/2 ]的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。




示例 1：
```
输入: [3,2,3]
输出: 3
```
示例 2：
```
输入: [2,2,1,1,1,2,2]
输出: 2
```


##哈希表
利用字典来当哈希表，数字作为key，出现的次数作为value。

时间复杂度：O(n)

空间复杂度：O(n)
### python的code如下：


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:              
        if len(nums)==1:return nums[0]
        lens=len(nums)//2
        flag=dict()
        print(lens)
        for i,value in enumerate(nums):
            print(flag)
            if value in flag:
                flag[value]+=1
                if flag[value]>lens:
                    return value
            else:
                flag[value]=1
```
执行用时 :160 ms, 在所有 Python3 提交中击败了76.59%的用户

内存消耗 :15.1 MB, 在所有 Python3 提交中击败了5.04%的用户
### c++的code如下：

```c

```
##排序法
对列表排序找中间那个值。

时间复杂度：O(nlogn)

空间复杂度：O(n)

(复杂度取决于python自带的sort函数，用的方法是Timesort)
### python的code如下：


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:              
        if len(nums)==1:return nums[0]
        lens=len(nums)//2
        nums.sort()
        return nums[lens]
```

执行用时 :44 ms, 在所有 Python3 提交中击败了95.58%的用户

内存消耗 :15.1 MB, 在所有 Python3 提交中击败了5.04%的用户