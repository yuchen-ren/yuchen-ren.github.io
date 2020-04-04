---
layout:     post
title:      "Leetcode42"
subtitle:   "接雨水"
date:       2020-4-4 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。




示例1：
```
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
```

###按列遍历

求每一列的水，我们只需要关注当前列，以及左边最高的墙，右边最高的墙就够了。

装水的多少，当然根据木桶效应，我们只需要看左边最高的墙和右边最高的墙中较矮的一个就够了。

时间复杂度：O(n²）。

空间复杂度：O(1）。




### python的code如下：


```python
class Solution:
    def trap(self, height: List[int]) -> int:
        lens=len(height)
        ans=0
        for i in range(1,lens-1): #最两端的列不用考虑，因为一定不会有水
            max_left=0
            for j in range(i):
                max_left=max(height[j],max_left)
            max_right=0
            for j in range(i+1,lens):
                max_right=max(height[j],max_right)
            smaller=min(max_left,max_right)
            if smaller>height[i]:
                ans+=smaller-height[i]
        return ans
```
超出时间限制。。。。

###动态规划

用dp表来记录每一个位置左边最高的墙和右边最高的墙。

时间复杂度：O(n）。

空间复杂度：O(n）。




### python的code如下：


```python
class Solution:
    def trap(self, height: List[int]) -> int:
        lens=len(height)
        ans=0
        dp_left=[0]*lens
        dp_right=[0]*lens
        for i in range(1,lens-1): 
            dp_left[i]=max(dp_left[i-1],height[i-1])
            j=lens-1-i
            dp_right[j]=max(dp_right[j+1],height[j+1])
        for i in range(1,lens-1):
            smaller=min(dp_left[i],dp_right[i])
            if smaller>height[i]:
                ans+=smaller-height[i]
        return ans
```
执行用时 :56 ms, 在所有 Python3 提交中击败了59.59%的用户

内存消耗 :14 MB, 在所有 Python3 提交中击败了5.04%的用户

###双指针

对动态规划进行空间优化。

时间复杂度：O(n）。

空间复杂度：O(n）。




### python的code如下：


```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        lens=len(height)
        ans=0
        left,right=0,lens-1
        max_left,max_right=height[left],height[right]
        while left<=right:
            max_left=max(max_left,height[left])
            max_right=max(max_right,height[right])
            if max_left < max_right:
                ans += max_left - height[left]
                left += 1
            else:
                ans += max_right - height[right]
                right -= 1
        return ans
```
执行用时 :48 ms, 在所有 Python3 提交中击败了81.04%的用户

内存消耗 :13.8 MB, 在所有 Python3 提交中击败了5.04%的用户