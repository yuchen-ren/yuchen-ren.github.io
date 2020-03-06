---
layout:     post
title:      "Leetcode70"
subtitle:   " 爬楼梯"
date:       2020-3-6 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：
```
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
```
示例 2：
```
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
```



## 动态规划
本问题其实常规解法可以分成多个子问题，爬第n阶楼梯的方法数量，等于 2 部分之和

爬上 n-1n−1 阶楼梯的方法数量。因为再爬1阶就能到第n阶
爬上 n-2n−2 阶楼梯的方法数量，因为再爬2阶就能到第n阶
所以我们得到公式 dp[n] = dp[n-1] + dp[n-2]dp[n]=dp[n−1]+dp[n−2]
同时需要初始化 dp[0]=1dp[0]=1 和 dp[1]=1dp[1]=1

时间复杂度：O(n)，单循环到n。

空间复杂度：O(n)，dp数组用了n的空间。






时间复杂度：由于枚举以后只需要 O(1)的时间判断，所以时间复杂度为枚举起点的复杂度O(target) 。

空间复杂度：O(1)，除了答案数组只需要常数的空间存放若干变量。


### python的code如下：


```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res=[]
        flag=-1
        for i in range(1,target):
            n_float=0.5*((1-2*i)+((2*i-1)**2+8*target)**0.5)
            n_int=int(n_float)
            n_fl_int=float(n_int)
            if n_float==n_fl_int:
                flag+=1
                res.append([])
                for j in range(i,i+n_int):
                    res[flag].append(j)
        return res

```
执行用时 :484 ms, 在所有 Python3 提交中击败了24.11%的用户

内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户


### c++的code如下：

```c

```

## 斐波那契数
在这个题目中，其实前面的动态规划也可以看作求斐波那契数的形式，我们在这里直接求最终的数，不借助额外的数组。

时间复杂度 O(target)

空间复杂度：O(1)，除了答案数组只需要常数的空间存放若干变量。

### python的code如下：


```python
class Solution:
    def climbStairs(self, n: int) -> int:      
        if(n<=2):
            return n
        first=1
        second=2
        third=0
        for i in range(3,n+1):
            third=first+second
            first=second
            second=third
        return third

```
执行用时 :32 ms, 在所有 Python3 提交中击败了72.11%的用户

内存消耗 :13.3 MB, 在所有 Python3 提交中击败了19.03%的用户


### c++的code如下：

```c

```
