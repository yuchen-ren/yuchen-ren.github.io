---
layout:     post
title:      "Leetcode575"
subtitle:   " 分糖果 "
date:       2020-3-4 10:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。
你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。


示例 1：
```
输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
```
示例 2：
```
输入: candies = [1,1,2,3]
输出: 2
解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。
这样使得妹妹可以获得的糖果种类数最多。

```
注意:

数组的长度为[2, 10,000]，并且确定为偶数。
数组中数字的大小在范围[-100,000, 100,000]内。




# 总体思路
比较糖果种类与二分之一糖果数量

先每种都喂妹妹吃一块，一边喂一边数吃了几块，如果吃了超过糖果总数的一半的数量就停手不喂了；
如果每种都吃过了都还没到糖果总数一半，就随便喂点之前已经吃过的种类的糖果。

所以按照这个思路分类讨论一下，如果糖果种类≥糖果总数一半，则能吃到等于糖果总数一半的数量；
如果糖果种数≤糖果总数一半，则能吃到所有种类的糖果，也就是能吃到等于糖果种数的数量。

所以目标就是求出糖果种数。

## 使用集合
用集合去重复的特性


时间复杂度 O(n)

空间复杂度 O(n)

### python的code如下：


```python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        lens=len(candies) //2
        candies_set=set(candies)
        num=len(candies_set)
        if num>=lens:
            return lens
        else:
            return num
```
执行用时 :1056 ms, 在所有 Python3 提交中击败了57.56%的用户

内存消耗 :15.3 MB, 在所有 Python3 提交中击败了17.21%的用户


### c++的code如下：

```c

```

## 使用字典
将糖果种类的数字值作为key存储在字典中，糖果一旦存在则进行标记，并将糖果种类加一。

利用字典特性：不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住

时间复杂度 O(n)

空间复杂度 O(n)

### python的code如下：


```python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        lens=len(candies) //2
        candies_dic=dict()
        for i,value in enumerate(candies):
            candies_dic[value]=i
        num=len(candies_dic)
        if num>=lens:
            return lens
        else:
            return num
```
执行用时 :1000 ms, 在所有 Python3 提交中击败了67.70%的用户

内存消耗 :15 MB, 在所有 Python3 提交中击败了18.03%的用户


### c++的code如下：

```c

```
## 使用排序比较
先对数组进行排序，然后将相邻的数字进行对比，如果相邻数字不同，则说明出现了糖果种类不同。

时间复杂度：O(nlogn)

空间复杂度：O(1)

### python的code如下：


```python
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        lens=len(candies) 
        candies.sort()
        num=1
        for i in range(lens-1):
            if candies[i]!=candies[i+1]:
                num+=1
        if num>=lens//2:
            return lens//2
        else:
            return num
```
执行用时 :1312 ms, 在所有 Python3 提交中击败了19.68%的用户

内存消耗 :14.7 MB, 在所有 Python3 提交中击败了19.67%的用户

### c++的code如下：

```c

```