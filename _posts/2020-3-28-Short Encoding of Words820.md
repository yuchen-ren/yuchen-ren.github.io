---
layout:     post
title:      "Leetcode820"
subtitle:   "单词的压缩编码"
date:       2020-3-28 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

那么成功对给定单词列表进行编码的最小字符串长度是多少呢？




示例1：
```
输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
```
提示：

1 <= words.length <= 2000
1 <= words[i].length <= 7
每个单词都是小写字母 。

##非字典树




### python的code如下：


```python
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words=sorted(words,key=lambda i:len(i),reverse=True)
        s=""
        for i in words:
            if i in s and i+"#" in s:
                continue
            s+=i+"#"
        return len(s)
```
执行用时 :264 ms, 在所有 Python3 提交中击败了30.16%的用户

内存消耗 :14.2 MB, 在所有 Python3 提交中击败了8.33%的用户