---
layout:     post
title:      "Leetcode面试题 08.01"
subtitle:   "三步问题"
date:       2020-7-13 19:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。




示例1：
```
输入：n = 3 
 输出：4
 说明: 有四种走法
```
示例2：
```
输入：n = 5
 输出：13
```
提示:

n范围在[1, 1000000]之间


##动态规划
dp[i]=dp[i-1]+dp[i-2]+dp[i-3]


时间复杂度：O(n)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def waysToStep(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        dp=[0]*n
        dp[0],dp[1],dp[2]=1,2,4
        for i in range(3,n):
            dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%1000000007
        return dp[n-1]
```
执行用时：576 ms, 在所有 Python3 提交中击败了47.93%的用户

内存消耗：50.4 MB, 在所有 Python3 提交中击败了100.00%的用户