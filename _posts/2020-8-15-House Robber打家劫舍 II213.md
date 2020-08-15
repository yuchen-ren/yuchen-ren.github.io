---
layout:     post
title:      "Leetcode213"
subtitle:   "打家劫舍II"
date:       2020-8-15 20:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。





示例 1：
```
输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

示例 2：
```
输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```


###动态规划

把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。

时间复杂度：O(n)。


空间复杂度：O(n)。

### python的code如下：


```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        def single_rob(left,right):
            dp=[0]*(right-left) 
            for i in range(right-left):
                if i==0 or i==1:
                    dp[i]=nums[i+left]
                elif i==2:
                    dp[i]=dp[i-2]+nums[i+left]
                elif i>2:
                    dp[i]=max(dp[i-2],dp[i-3])+nums[i+left]
            return max(dp)
        return max(single_rob(0,n-1),single_rob(1,n))
```
执行用时：48 ms, 在所有 Python3 提交中击败了22.55%的用户

内存消耗：13.5 MB, 在所有 Python3 提交中击败了89.47%的用户


###动态规划优化

时间复杂度：O(n)。


空间复杂度：O(1)。

### python的code如下：

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        def single_rob(left,right):
            dp=[0]*3
            for i in range(right-left):
                if i==0 or i==1:
                    dp[i]=nums[i+left]
                elif i==2:
                    dp[i]=dp[i-2]+nums[i+left]
                elif i>2:
                    dp[i%3]=max(dp[(i-2)%3],dp[(i-3)%3])+nums[i+left]
            return max(dp)
        return max(single_rob(0,n-1),single_rob(1,n))
```
执行用时：36 ms, 在所有 Python3 提交中击败了89.03%的用户

内存消耗：13.7 MB, 在所有 Python3 提交中击败了22.31%的用户