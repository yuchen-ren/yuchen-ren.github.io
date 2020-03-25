---
layout:     post
title:      "Leetcode204"
subtitle:   "计数质数"
date:       2020-3-25 23:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

统计所有小于非负整数 n 的质数的数量。



示例1：
```
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
```

##暴力循环
遍历每个比n小的元素i，并在判断元素i是否在除1到i本身范围内有因数，没有的话i就是质数。

时间复杂度：O(n^2)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:return 0       
        count=0
        for i in range(2,n):
            is_prime=True
            for j in range(2,i-1):
                if i%j==0:
                    is_prime=False
            if is_prime:
                count+=1
        return count
```
会超时。。。。
##优化
[参考解析](https://leetcode-cn.com/problems/count-primes/solution/ru-he-gao-xiao-pan-ding-shai-xuan-su-shu-by-labula/)

时间复杂度：O(n * loglogn)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:return 0       
        count=0
        is_prime=[True]*n
        sqrt_n=int(n**(1/2))
        for i in range(2,sqrt_n+1):
            if is_prime[i]:
                j=i*i
                while j<n:
                    is_prime[j] = False
                    j+=i
        for i in range(2,n):
            if is_prime[i]:
                count+=1
        return count
```
执行用时 :592 ms, 在所有 Python3 提交中击败了44.13%的用户

内存消耗 :25.2 MB, 在所有 Python3 提交中击败了69.69%的用户