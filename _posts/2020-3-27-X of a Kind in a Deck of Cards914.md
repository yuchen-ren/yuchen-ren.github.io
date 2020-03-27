---
layout:     post
title:      "Leetcode914"
subtitle:   "卡牌分组"
date:       2020-3-27 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。





示例1：
```
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
```
示例2：
```
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。
```
示例3：
```
输入：[1]
输出：false
解释：没有满足要求的分组。
```
示例4：
```
输入：[1,1]
输出：true
解释：可行的分组是 [1,1]
```
示例5：
```
输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]
```

提示：

1 <= deck.length <= 10000
0 <= deck[i] < 10000
##求最大公约数
统计每个元素的频率f，需满足f>=2，并且不同数的f都相同，
或者至少有一个除1以外的最大公约数，例如4个1和6个2,3个1和9个2，(其实这个条件包括了前一个条件)
才能满足true的条件。

用gcd求最大公约数。

时间复杂度：O(nlog C)，其中n是卡牌的个数，C是map中数的范围，在本题中C的值为10000。
求两个数最大公约数的复杂度是O(logC)，需要求最多n−1次。

空间复杂度：O(n)。




### python的code如下：


```python
class Solution:
    def gcd(self,p,q):
        if p%q==0:
            return q
        return self.gcd(q,p%q)
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        lens=len(deck)
        if lens==1:return False
        cnt={}
        cd=2
        for i in range(lens):
            if deck[i] not in cnt:
                cnt[deck[i]]=1
            else:
                cnt[deck[i]]+=1
            if i==lens-1:
                cd=cnt[deck[i]]       
        for value in cnt.values():
            if value<2 :
                return False
            else:
                cd=self.gcd(cd,value)
                if cd==1:
                    return False
        return True
```
执行用时 :56 ms, 在所有 Python3 提交中击败了83.26%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.38%的用户