---
layout:     post
title:      "Leetcode53"
subtitle:   "最大子序和"
date:       2020-4-01 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。



示例1：
```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

###动态规划
用dp[i][j]来表示数组中第i个数到第j个数的和，有两种情况：

1、i==j：
dp[i][j+1]=dp[i][j]+nums[j],

2、i!=j：
dp[i][j]=nums[j]

时间复杂度：1/2*O(n*n)=O(n*n)。
空间复杂度：O(n*n)。
### python的code如下：


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lens=len(nums)
        if lens==1:return nums[0]
        dp=[[float('-inf')]*lens for i in range(lens)]
        dp[0][0]=nums[0]
        ans=float('-inf')
        for i in range(lens):
            for j in range(i,lens):
                if i==j:
                    dp[i][j]=nums[j]
                else:
                    dp[i][j]=dp[i][j-1]+nums[j]
                ans=max(ans,dp[i][j])
        return ans
```
超出时间限制。。。

###动态规划优化
如果 sum > 0，则说明 sum 对结果有增益效果，则sum保留并加上当前遍历数字

如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则sum直接更新为当前遍历数字


用dp[i]来表示nums中从0到i的时候sum（其实只是朝向最大子序和的趋势，为了保持相邻数相加的连续性)。

用ans来保存真正的最大的子序和，每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果。

如果dp[i-1]>0：dp[i]=dp[i-1]+nums[i]

否则：dp[i]=nums[i]


时间复杂度：O(n)。

空间复杂度：O(n)。
### python的code如下：


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lens=len(nums)
        if lens==1:return nums[0]
        dp=[float('-inf')]*lens 
        dp[0]=nums[0]
        ans=dp[0]
        for i in range(1,lens):
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]         
            ans=max(dp[i],ans)
        return ans
```
执行用时 :52 ms, 在所有 Python3 提交中击败了75.34%的用户

内存消耗 :14.5 MB, 在所有 Python3 提交中击败了5.35%的用户

再优化一下空间，O(n)优化为O(1)：
### python的code如下：


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lens=len(nums)
        if lens==1:return nums[0]
        last=nums[0]
        cur=float('-inf')
        ans=last
        for i in range(1,lens):
            if last>0:
                cur=last+nums[i]
            else:
                cur=nums[i] 
            last=cur
            ans=max(cur,ans)
        return ans
```
###动态规划
用dp[i][j]来表示数组中第i个数到第j个数的和，有两种情况：

1、i==j：
dp[i][j+1]=dp[i][j]+nums[j],

2、i!=j：
dp[i][j]=nums[j]

时间复杂度：1/2*O(n*n)=O(n*n)。
空间复杂度：O(n*n)。
### python的code如下：


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lens=len(nums)
        if lens==1:return nums[0]
        dp=[[float('-inf')]*lens for i in range(lens)]
        dp[0][0]=nums[0]
        ans=float('-inf')
        for i in range(lens):
            for j in range(i,lens):
                if i==j:
                    dp[i][j]=nums[j]
                else:
                    dp[i][j]=dp[i][j-1]+nums[j]
                ans=max(ans,dp[i][j])
        return ans
```
超出时间限制。。。
