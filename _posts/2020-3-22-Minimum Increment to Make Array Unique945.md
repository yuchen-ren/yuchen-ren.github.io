---
layout:     post
title:      "Leetcode945"
subtitle:   "使数组唯一的最小增量"
date:       2020-3-22 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

返回使 A 中的每个值都是唯一的最少操作次数。

示例1：
```
输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
```
示例2：
```
输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。

```
提示：

0 <= A.length <= 40000
0 <= A[i] < 40000

##先排序再遍历
首先将数组进行排序，然后从左到右遍历数组：

如果当前元素大于上一个元素，保持不变；
如果当前元素小于等于上一个元素，就需要增加当前元素，直到大于上一个元素。
例如输入 [3, 2, 1, 2, 1, 7]，排序后为 [1, 1, 2, 2, 3, 7]。




时间复杂度：O(nlogn)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        count=0
        for i in range(1,len(A)):
            if A[i]<=A[i-1]:             
                count+=A[i-1]-A[i]+1
                A[i]=A[i-1]+1
        return count
```
执行用时 :388 ms, 在所有 Python3 提交中击败了71.59%的用户

内存消耗 :18.9 MB, 在所有 Python3 提交中击败了15.38%的用户

##计数
当我们找到一个没有出现过的数的时候，将之前某个重复出现的数增加成这个没有出现过的数。
注意，这里 「之前某个重复出现的数」 是可以任意选择的，
它并不会影响最终的答案，因为将 P 增加到 X 并且将 Q 增加到 Y，
与将 P 增加到 Y 并且将 Q 增加到 X 都需要进行 (X + Y) - (P + Q) 次操作。


当数组 A 为 [1, 1, 1, 1, 3, 5] 时，我们发现有 3 个重复的 1，且没有出现过 2，4 和 6，
因此一共需要进行 (2 + 4 + 6) - (1 + 1 + 1) = 9 次操作。

以 [1, 1, 1, 1, 3, 5] 为例，
当我们发现有 3 个重复的 1 时，我们先将操作次数减去 1 + 1 + 1。接下来，
当我们发现 2，4 和 6 都没有出现过时，我们依次将操作次数增加 2，4 和 6。

时间复杂度：O(L)，其中L的数量级是数组A的长度加上其数据范围内的最大值，因为在最坏情况下，数组A中的所有数都是数据范围内的最大值。

空间复杂度：O(L)，需要长度L的数组统计每个数出现的次数。


[参考链接](https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/solution/shi-shu-zu-wei-yi-de-zui-xiao-zeng-liang-by-leet-2/)

```python
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:return 0
        n=len(A)+max(A)
        cnt=[0]*n
        for i in A:
            cnt[i]+=1
        count,flag=0,0
        for i in range(n):
            if cnt[i]>1:
                flag+=cnt[i]-1
                count-=i*(cnt[i]-1)
            elif flag>0 and cnt[i]==0:
                flag-=1
                count+=i
        return count
```
执行用时 :336 ms, 在所有 Python3 提交中击败了96.55%的用户

内存消耗 :19.6 MB, 在所有 Python3 提交中击败了11.54%的用户