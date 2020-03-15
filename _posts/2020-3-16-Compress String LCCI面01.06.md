---
layout:     post
title:      "Leetcode面试题 01.06"
subtitle:   "字符串压缩"
date:       2020-3-16 00:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。

比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。





示例 1：
```
输入："aabcccccaaa"
输出："a2b1c5a3"
```


示例 2：
```
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
```
提示：

字符串长度在[0, 50000]范围内。

##双指针法
用新字符串的指针new和原来字符串的指针i，来判断是否有新的字符出现，以及记录上一个字符的出现次数。

时间复杂度：O(n)。

空间复杂度：O(1)，只需要常数空间（不包括存储压缩答案的空间）。



### python的code如下：


```python
class Solution:
    def compressString(self, S: str) -> str:
        if not S:return S
        new_s=""+S[0]
        new,flag=0,1 #new是新字符串的指针，flag是出现次数
        lens=len(S)
        for i in range(1,lens): #i是原来字符串的指针
            if new_s[new]!=S[i]:
                new_s+=str(flag)
                new=new+len(str(flag))+1
                new_s+=S[i]
                flag=1               
            else:flag+=1
        new_s+=str(flag)
        return new_s if len(new_s)<lens else S
```
执行用时 :56 ms, 在所有 Python3 提交中击败了76.34%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
### c++的code如下：

```c

```
