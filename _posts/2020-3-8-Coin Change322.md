---
layout:     post
title:      "Leetcode322"
subtitle:   " 零钱兑换"
date:       2020-3-8 10:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。





示例 1：
```
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

```
示例 2：
```
输入: coins = [2], amount = 3
输出: -1
```
说明:
你可以认为每种硬币的数量是无限的。




## 贪心 + DFS


参考了大佬的思路，这里有详细介绍[参考来源](https://leetcode-cn.com/problems/coin-change/solution/322-by-ikaruga/)


### python的code如下：


```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lens=len(coins)
        #i=lens-1
        j=lens-1
        flag=0
        coins.sort()     
        while j>=0:
            i=j
            dif=amount
            while i>=0: 
                print(i) 
                print(dif)        
                if dif==coins[i]:
                    return flag+1
                elif dif>coins[i]:
                    dif-=coins[i]
                    flag+=1
                    while dif>=coins[i]:
                        dif-=coins[i] 
                        flag+=1
                i-=1
            print(dif)
            if dif!=0: j-=1
            else: break 
        return flag if dif==0 else -1


```
执行用时 :276 ms, 在所有 Python3 提交中击败了60.77%的用户

内存消耗 :16.9 MB, 在所有 Python3 提交中击败了100.00%的用户

### c++的code如下：

```c

```
## 动态规划从下向上
参考了官方的思路，这里有详细介绍[参考来源](https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/

时间复杂度：O(Sn)，其中 S是金额，n是面额数。我们一共需要计算 O(S)个状态，S为题目所给的总金额。
对于每个状态，每次需要枚举 n个面额来转移状态，所以一共需要 O(Sn)的时间复杂度。

空间复杂度：O(S)。DP数组需要开长度为总金额 S的空间。


### python的code如下：


```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1]!=float("inf") else -1
```
执行用时 :1584 ms, 在所有 Python3 提交中击败了64.90%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了24.21%的用户


### c++的code如下：

```c
class Solution {
public:
    void coinChange(vector<int>& coins, int amount, int c_index, int count, int& ans)
    {
        if (amount == 0)
        {
            ans = min(ans, count);
            return;
        }
        if (c_index == coins.size()) return;

        for (int k = amount / coins[c_index]; k >= 0 && k + count < ans; k--)
        {
            coinChange(coins, amount - k * coins[c_index], c_index + 1, count + k, ans);
        }
    }

    int coinChange(vector<int>& coins, int amount)
    {
        if (amount == 0) return 0;
        sort(coins.rbegin(), coins.rend());
        cout<<coins[0]<<endl;
        int ans = INT_MAX;
        coinChange(coins, amount, 0, 0, ans);
        return ans == INT_MAX ? -1 : ans;
    }

};
```
执行用时 :16 ms, 在所有 C++ 提交中击败了97.82%的用户

内存消耗 :12.3 MB, 在所有 C++ 提交中击败了88.64%的用户

## 动态规划自顶向下
用first来保存当前队列中最大的数，用second来保存第二大的，first中的数被弹出后再取second中的数
本意是对上一种方法的优化，减少了一个额外队列的空间，但这样貌似时间不能平均了。

时间复杂度：O(1)（插入，求最大值），O(n)（删除）。

空间复杂度：O(n)


### python的code如下：


```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={0:0}
        def helper(n):
            if n in memo:
                return memo[n]
            res=float("inf")
            for coin in coins:
                if n>=coin:
                    res=min(res,helper(n-coin)+1)
            memo[n]=res
            return res
        return helper(amount) if helper(amount)!=float("inf") else -1
        
```
执行用时 :1840 ms, 在所有 Python3 提交中击败了40.50%的用户

内存消耗 :43.9 MB, 在所有 Python3 提交中击败了5.03%的用户


### c++的code如下：

```c

```
