---
layout:     post
title:      "Leetcode1160"
subtitle:   "拼写单词"
date:       2020-3-17 00:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。




示例1：
```
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
```
示例2：
```
输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
```

##暴力循环

用一个数组来记录字典里的字符是否被用过，也就是剩下的可使用次数。

时间复杂度：O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lens=len(words)
        ans=0
        charscount=[0]*26
        for k in range(len(chars)):
            charscount[ord(chars[k])-97]+=1
        for i in range(lens):
            charscount2=copy.copy(charscount)
            flag=True
            n=len(words[i])
            for j in range(n):
                if words[i][j] in chars :
                    if charscount2[ord(words[i][j])-97]<1 :
                        flag=False
                        break
                    else:
                        charscount2[ord(words[i][j])-97]-=1
                else:
                    flag=False
                    break
            if flag:
                ans+=n
        return ans
```
执行用时 :144 ms, 在所有 Python3 提交中击败了76.70%的用户

内存消耗 :14 MB, 在所有 Python3 提交中击败了5.04%的用户
### c++的code如下：

```c

```
##哈希表

直接统计字母表 chars 中每个字母出现的次数，然后检查词汇表 words 中的每个单词，
如果该单词中每个字母出现的次数都小于等于词汇表中对应字母出现的次数，就将该单词长度加入答案中。


时间复杂度：O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for w in words:
            c = collections.Counter(w)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(w)
        return ans
```
执行用时 :256 ms, 在所有 Python3 提交中击败了40.43%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.04%的用户
### c++的code如下：

```c

```