---
layout:     post
title:      "Leetcode172"
subtitle:   "阶乘后的零"
date:       2020-3-17 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个整数 n，返回 n! 结果尾数中零的数量。




示例1：
```
输入: 3
输出: 0
解释: 3! = 6, 尾数中没有零。
```
示例2：
```
输入: 5
输出: 1
解释: 5! = 120, 尾数中有 1 个零.
```
说明: 你算法的时间复杂度应为 O(log n) 。
##暴力递归

在递归的过程中找到包含5的数，每有一个，ans就加一。还有特殊情况像25的倍数，里面包含多个5的需要额外判断。

然而用递归的方法最后会超时报错，当n特别大的时候。。。。。
因为python的递归深度是有限制的，默认为1000。当递归深度超过1000时，就会报错。

时间复杂度：O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def rec(self,n,ans):
        if n==1:return 0
        ans+=self.rec(n-1,ans)
        if n%25==0:
            res=n/25
            ans+=2           
            while res%5==0:
                ans+=1
                res/=5
        elif n%5==0:ans+=1
        return ans
    def trailingZeroes(self, n: int) -> int:
        if n==0:return 0
        ans=0
        ans+=self.rec(n,ans)
        return ans
```

##用循环代替递归

直接从1到n，循环遍历，来优化上一个方法中的递归。
然而也会超出时间限制。。。。。。。

时间复杂度：O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:return 0
        ans=0
        for i in range(1,n+1):
            if i%25==0:
                res=i/25
                ans+=2           
                while res%5==0:
                    ans+=1
                    res/=5
            elif i%5==0:ans+=1
        return ans
```

##用数学公式优化

无需遍历，我们就可以用n//5来找出现了多少5，并且每次判断之后n//5,相当于 n / 5 + n/ 25 + n /125 ...。

时间复杂度：O(logn)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:return 0
        ans=0
        while(n>0):
            ans+=n//5
            n=n//5
        return ans
```
执行用时 :32 ms, 在所有 Python3 提交中击败了80.17%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.52%的用户
### c++的code如下：

```c

```