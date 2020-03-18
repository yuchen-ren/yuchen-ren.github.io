---
layout:     post
title:      "Leetcode409"
subtitle:   "最长回文串"
date:       2020-3-19 00:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。




示例1：
```
输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
```



##哈希表

根据每个字符出现的次数，构建哈希表。看次数是奇数还是偶数，偶数可以直接累加（因为可以直接对称）。
奇数的话减一变成偶数再累加。



时间复杂度：O(n)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:return 0
        freq_map={}
        odd_flag=False
        for i in range(len(s)):
            if s[i] in freq_map:
                freq_map[s[i]]+=1
            else:
                freq_map[s[i]]=1
        count=0
        for key in freq_map:
            if freq_map[key]%2==0:
                count+=freq_map[key]
            else:
                count+=(freq_map[key]-1)
                odd_flag=True
        return count+1 if odd_flag else count
```
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
70.67%
的用户
内存消耗 :
13.3 MB
, 在所有 Python3 提交中击败了
5.23%
的用户
##一维投影

如果两个矩形重叠，代表了两个矩形与x轴平行的边投影到x轴上时会有交集，与y轴平行的边投影到y轴上时也会有交集。
因此，我们可以将问题看作一维线段是否有交集的问题。


时间复杂度：O(1)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if min(rec1[2],rec2[2])>max(rec1[0],rec2[0])and min(rec1[3],rec2[3])>max(rec1[1],rec2[1]):
            return True
        else:
            return False
```
执行用时 :28 ms, 在所有 Python3 提交中击败了89.31%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.77%的用户