---
layout:     post
title:      "Leetcode1143"
subtitle:   "最长公共子序列"
date:       2020-3-31 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。




示例1：
```
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace"，它的长度为 3。
```
示例2：
```
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
```
提示:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
输入的字符串只含有小写英文字符。

###动态规划
1.　S{s1,s2,s3....si} T{t1,t2,t3,t4....tj}

2.　子问题划分

(1) 如果S的最后一位等于T的最后一位，则最大子序列就是{s1,s2,s3...si-1}和{t1,t2,t3...tj-1}的最大子序列+1

(2) 如果S的最后一位不等于T的最后一位，那么最大子序列就是

① {s1,s2,s3..si}和 {t1,t2,t3...tj-1} 最大子序列

② {s1,s2,s3...si-1}和{t1,t2,t3....tj} 最大子序列

以上两个自序列的最大值

3.　边界

只剩下{s1}和{t1}，如果相等就返回1，不等就返回0

4.　使用一个表格来存储dp的结果

如果 S[i] == T[j] 则dp[i][j] = dp[i-1][j-1] + 1

否则dp[i][j] = max(dp[i][j-1],dp[i-1][j])


[参考链接](https://leetcode-cn.com/problems/longest-common-subsequence/solution/chao-xiang-xi-dong-tai-gui-hua-jie-fa-by-shi-wei-h/)

时间复杂度：O(m*n)。
空间复杂度：O(m*n)。
### python的code如下：


```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[0]*(m+1) for i in range(n+1)]
        for i in range(m):
            dp[0][i]=0
        for i in range(n):
            dp[n][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[j-1]==text2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1  
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n][m]
```
执行用时 :464 ms, 在所有 Python3 提交中击败了67.52%的用户

内存消耗 :21.4 MB, 在所有 Python3 提交中击败了12.09%的用户

###动态规划空间压缩
把原来的(m+1)*(n+1)大小的动态表进行压缩，因为动态方程只涉及到左上、上、左三个位置，
所以可以压缩为一维列表+一个变量，一维列表来记录上的位置，两个个变量来记录左和左上的位置。

时间复杂度：O(m*n)。

空间复杂度：O(m)。
### python的code如下：


```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[0]*m 
        left=0
        left_up=0
        for i in range(n):           
            left_up=0
            left=0
            for j in range(m):             
                if text1[j]==text2[i]:
                    dp[j],left_up=left_up+1,dp[j]
                    left=dp[j]
                else:
                    left_up=dp[j]
                    dp[j]=max(dp[j],left)
                    left=dp[j]          
        return dp[m-1]
```
执行用时 :328 ms, 在所有 Python3 提交中击败了98.56%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了89.01%的用户