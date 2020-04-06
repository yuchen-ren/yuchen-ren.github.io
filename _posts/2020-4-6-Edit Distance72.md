---
layout:     post
title:      "Leetcode72"
subtitle:   "编辑距离"
date:       2020-4-6 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符







示例1：
```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```
示例1：
```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```
###动态规划

dp[i][j] 代表 word1 到 i 位置转换成 word2 到 j 位置需要最少步数

所以，

当 word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]；

当 word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

其中，dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作。

[参考链接](https://leetcode-cn.com/problems/edit-distance/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-3/)

以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，即要将 word1的前 5 个字符转换为 word2的前 3 个字符，也就是将 horse 转换为 ros，因此有：

(1) dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，然后将第五个字符 word1[4]（因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）

(2) dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，然后在末尾补充一个 s，即插入操作

(3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，然后删除 word1 的第 5 个字符

时间复杂度：O(m*n）。

空间复杂度：O(m*n）。




### python的code如下：


```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row=len(word1)+1
        cul=len(word2)+1
        dp=[[0]*cul for i in range(row)]
        for c in range(1,cul):
            dp[0][c]=c 
        for r in range(1,row):
            dp[r][0]=r 
        for r in range(1,row):
            for c in range(1,cul):
                if word1[r-1]==word2[c-1]:
                    dp[r][c]=dp[r-1][c-1]
                else:
                    dp[r][c]=min(dp[r-1][c-1],dp[r][c-1],dp[r-1][c])+1
        return dp[row-1][cul-1]
```
执行用时 :196 ms, 在所有 Python3 提交中击败了68.32%的用户

内存消耗 :17.2 MB, 在所有 Python3 提交中击败了12.88%的用户

###动态规划空间优化

当前状态主要和左上、上、左三个状态有关，于是我们可以用一个n长度列表来保存上，两个变量来保存左上和左。

时间复杂度：O(m*n）。

空间复杂度：O(n）。
### python的code如下：


```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row=len(word1)+1
        cul=len(word2)+1
        if row-1+cul-1==1:
            return 1
        dp=[0]*cul
        for c in range(1,cul):
            dp[c]=c
        for r in range(1,row):
            left_up=r-1
            left=r  
            for c in range(1,cul):
                if word1[r-1]==word2[c-1]:
                    dp[c],left_up=left_up,dp[c]
                else:
                    dp[c],left_up=min(left_up,left,dp[c])+1,dp[c]
                left=dp[c]
        return dp[cul-1]
```
执行用时 :156 ms, 在所有 Python3 提交中击败了91.05%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了95.71%的用户