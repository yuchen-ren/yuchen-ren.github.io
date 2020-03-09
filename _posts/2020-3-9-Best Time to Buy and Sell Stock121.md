---
layout:     post
title:      "Leetcode121"
subtitle:   " 买卖股票的最佳时机"
date:       2020-3-9 00:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。




示例 1：
```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

```
示例 2：
```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

```
限制：

1 <= target <= 10^5






## 双指针暴力破解
用两个指针形成滑动窗口，找rear-front最大的差值

时间复杂度：O(n^2)
空间复杂度：O(1)





### python的code如下：


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lens=len(prices)
        maxdif=0
        flag=0
        for front in range(lens):
            for rear in range(front+1,lens):
                dif=prices[rear]-prices[front]
                if dif>maxdif:
                    maxdif=dif
        if maxdif<=0:
            return 0
        return maxdif

```
提交会超时


### c++的code如下：

```c

```

## 动态规划


参考了大佬的思路，这里有详细介绍[参考来源](https://leetcode-cn.com/problems/coin-change/solution/322-by-ikaruga/)

用一个dp二维数组来保存每个状态对应的利润

时间复杂度：O(n)

空间复杂度：O(n)

### python的code如下：


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lens=len(prices)
        #dp[i][0 or 1]第i天手头没有或持有股票，所对应的利润
        dp= [[0] *2 for _ in range(lens+1)]       
        dp[0][1]=float("-inf")
        for i in range(1,lens+1):
            #prices列表比dp少一位，prices[i-1]对应dp[i]
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i-1]) 
            dp[i][1]=max(dp[i-1][1],-prices[i-1])
        return dp[lens][0]
```
执行用时 :52 ms, 在所有 Python3 提交中击败了87.88%的用户

内存消耗 :16.7 MB, 在所有 Python3 提交中击败了5.06%的用户
### c++的code如下：

```c

```
## 动态规划空间优化
对上面方法的优化，用两个数来代替dp数组。


时间复杂度：O(n)

空间复杂度：O(1)

### python的code如下：


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lens=len(prices)
        #dp[i][0 or 1]第i天手头没有或持有股票，所对应的利润
        dp= [[0] *2 for _ in range(lens+1)]       
        dp[0][1]=float("-inf")
        print(dp)
        for i in range(1,lens+1):
            #prices列表比dp少一位，prices[i-1]对应dp[i]
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i-1]) 
            dp[i][1]=max(dp[i-1][1],-prices[i-1])
        return dp[lens][0]
```
执行用时 :48 ms, 在所有 Python3 提交中击败了90.96%的用户

内存消耗 :14.2 MB, 在所有 Python3 提交中击败了18.65%的用户

### c++的code如下：

```c

```
