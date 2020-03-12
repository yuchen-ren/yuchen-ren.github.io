---
layout:     post
title:      "Leetcode1071"
subtitle:   " 将数组分成和相等的三个部分"
date:       2020-3-12 10:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。




示例 1：
```
输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
```
示例 2：
```
输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
```

示例 3：
```
输入：str1 = "LEET", str2 = "CODE"
输出：""
```

##辗转相除法
对于求解最大公约数的问题，思想是使用辗转相除法：
当a>=b时，gcd(a, b) = b if a % b == 0 else gcd(b, a % b)  

同时，对于字符串来说，想要有最大公约数，则要满足str1 + str2 === str2 + str1
### python的code如下：


```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:       
        len1=len(str1)
        len2=len(str2)
        if len1==0 or len2==0 or str1+str2!=str2+str1:
            return ""
        if len1==len2:
            return str1
        elif len1>len2:
            str1=str1[len2:]
        else:
            str2=str2[len1:]
        return self.gcdOfStrings(str1,str2)
```
执行用时 :28 ms, 在所有 Python3 提交中击败了94.07%的用户

内存消耗 :13.3 MB, 在所有 Python3 提交中击败了7.48%的用户
### c++的code如下：

```c

```

