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


##动态规划
用dp来保存当前的结果，max_summ来保存当前为止的最大值。
dp[i]=nums[i]+max_sum[i-2]


时间复杂度：O(n)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:return 0
        lens=len(nums)       
        if lens==1:return nums[0]
        if lens==2:return max(nums[0],nums[1])
        dp=[0]*lens
        max_sum=[0]*lens
        max_sum[0]=dp[0]=nums[0]
        dp[1]=nums[1]
        max_sum[1]=max(max_sum[0],nums[1])
        for i in range(2,lens):
            dp[i]=nums[i]+max_sum[i-2]
            max_sum[i]=max(max_sum[i-1],dp[i])
        return max(dp[lens-2],dp[lens-1])
```
执行用时 :32 ms, 在所有 Python3 提交中击败了93.06%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户