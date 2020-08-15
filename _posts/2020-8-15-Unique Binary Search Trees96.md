---
layout:     post
title:      "Leetcode62"
subtitle:   "不同路径"
date:       2020-8-15 21:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？




示例 1：
```
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

```

###动态规划

把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。

时间复杂度：O(n^2)。


空间复杂度：O(n)。

### python的code如下：


```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n<2:return 1
        dp=[0]*(n+1)
        dp[0],dp[1]=1,1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-1-j]
        return dp[n]
```
执行用时：32 ms, 在所有 Python3 提交中击败了95.91%的用户

内存消耗：13.6 MB, 在所有 Python3 提交中击败了82.18%的用户
