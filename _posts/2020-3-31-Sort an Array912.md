---
layout:     post
title:      "Leetcode912"
subtitle:   "排序数组"
date:       2020-3-31 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个整数数组 nums，将该数组升序排列



示例1：
```
输入：[5,2,3,1]
输出：[1,2,3,5]
```
示例2：
```
输入：[5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
```
提示：

1 <= A.length <= 10000
-50000 <= A[i] <= 50000

###快速排序

时间复杂度：O(n^2)。
空间复杂度：O(n)。
### python的code如下：


```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lens=len(nums)
        if lens<2:
            return nums
        mid=nums[lens//2]
        nums.remove(mid)
        left=[]
        right=[]
        for num in nums:
            if num>mid:
                right.append(num)
            else:
                left.append(num)
        return self.sortArray(left)+[mid]+self.sortArray(right)
```
执行用时 :264 ms, 在所有 Python3 提交中击败了79.41%的用户

内存消耗 :20.7 MB, 在所有 Python3 提交中击败了5.41%的用户
###数学解法
约瑟夫环问题：(当前index + m)%上一轮剩余数字的个数，
递推公式：f(n,m)=[f(n-1,m)+m]%n。

[参考链接](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/)

时间复杂度：O(n)，需要求解的函数值有n个。

空间复杂度：O(1)。
### python的code如下：


```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans=0
        for i in range(2,n+1):
            ans=(ans+m)%i 
        return ans
```
执行用时 :76 ms, 在所有 Python3 提交中击败了95.50%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户