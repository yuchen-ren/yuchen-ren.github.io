---
layout:     post
title:      "Leetcode1013"
subtitle:   " 将数组分成和相等的三个部分"
date:       2020-3-11 08:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。



示例 1：
```
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

```
示例 2：
```
输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false
```

示例 3：
```
输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

```

##双指针遍历
将先求出原来数组所有数的总和sumtotal，如果可以被3整除的话，那么将数组分为三部分。
前一部分开始遍历求和，如果和等于sumtotal的三分之一，那么再判断一下最后一部分之和是否也为同样的值。


### python的code如下：


```python
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sumtotal=sum(A)
        if sumtotal%3 !=0:return False
        lens=len(A)
        sum1,sum3=0,0
        for i in range(0,lens-2):        
            sum1+=A[i]         
            if sum1==sumtotal/3:
                sum3=0   
                for j in range(lens-1,i+1,-1):
                    sum3+=A[j]        
                    if sum3==sumtotal/3:return True                    
        return False
```
执行用时 :64 ms, 在所有 Python3 提交中击败了98.19%的用户

内存消耗 :18.7 MB, 在所有 Python3 提交中击败了98.29%的用户
### c++的code如下：

```c

```

