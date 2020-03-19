---
layout:     post
title:      "Leetcode5"
subtitle:   "最长回文子串"
date:       2020-3-19 10:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。




示例1：
```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```
示例2：
```
输入: "cbbd"
输出: "bb"
```


##动态规划

设i,j为子串的左边界和右边界，如果是回文子串则首先满足s[i]=s[j]。
除此之外，我们判断是否为回文子串时从两边向中间判断，也就是还要看s[i+1]和s[j-1]；
如果到了最小边界就不用看s[i+1]和s[j-1]，此时直接可判断为回文子串的最小边界条件为j-i<=2。

于是构建二维dp，dp[i][j]里存放是否是回文子串的状态True或False。

时间复杂度：O(n^2)。


空间复杂度：O(n^2)。


### python的code如下：


```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lens=len(s)
        if lens<2:
            return s
        dp=[[False]*lens for i in range(lens)]
        max_len=1
        cur_i=0
        for i in range(lens):
            dp[i][i]=True
        for j in range(1,lens):
            for i in range(j):
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False
                if dp[i][j]:
                    cur_len=j-i+1
                    if cur_len>max_len:
                        max_len=cur_len
                        cur_i=i 
        return s[cur_i:cur_i+max_len]
```
执行用时 :4224 ms, 在所有 Python3 提交中击败了34.87%的用户

内存消耗 :21.2 MB, 在所有 Python3 提交中击败了19.55%的用户
##中心扩散
既然我们上面方法是从两边向中心收缩，那么当然也可以从中心向两边判断。


时间复杂度：O(n^2)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def center_spread(self,s,lens,left,right):
        """
        left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        """
        i,j=left,right
        while i>=0 and j<lens and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j],j-i-1
    def longestPalindrome(self, s: str) -> str:
        lens=len(s)
        if lens<2:
            return s
        max_len=1
        res=s[0]
        for i in range(lens):
            pal_odd,odd_len=self.center_spread(s,lens,i,i)
            pal_even,even_len=self.center_spread(s,lens,i,i+1)
            cur_max_sub = pal_odd if odd_len >= even_len else pal_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub
        return res
```
执行用时 :772 ms, 在所有 Python3 提交中击败了81.82%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了31.42%的用户