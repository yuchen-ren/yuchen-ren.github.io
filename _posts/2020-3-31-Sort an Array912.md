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

###插入排序（Insertion Sort）

插入排序是前面已排序数组找到插入的位置。

性质：稳定，原址排序。


时间复杂度：O(n^2)。

空间复杂度：O(1)。

### python的code如下：


```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lens=len(nums)
        if lens<2:
            return nums
        for i in range(lens):
            while i>0 and nums[i-1]>nums[i]:
                nums[i-1],nums[i]=nums[i],nums[i-1]
                i-=1
        return nums
```
超出时间限制。。。


###归并排序（Merge Sort）

采用是分治法，先将数组分成子序列，让子序列有序，再将子序列间有序，合并成有序数组。

性质：稳定，非原址排序。


时间复杂度：O(nlogn)。由于归并排序每次都将当前待排序的序列折半成两个子序列递归调用，
然后再合并两个有序的子序列，而每次合并两个有序的子序列需要O(n)的时间复杂度，
所以我们可以列出归并排序运行时间 T(n)的递归表达式：
T(n)=2T(n/2)+O(n)
​根据主定理我们可以得出归并排序的时间复杂度为O(nlogn)。

空间复杂度：O(n)。我们需要额外O(n)空间的数组，且归并排序递归调用的层数最深为logn,
所以我们还需要额外的O(logn)的栈空间，所需的空间复杂度即为O(n+log n) = O(n)。

### python的code如下：


```python
class Solution:
    def merge(self,left,right):
        res=[]
        i,j=0,0
        while i<len(left) and j <len(right):
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        res+=left[i:]
        res+=right[j:]
        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        lens=len(nums)
        if lens<2:
            return nums
        mid=lens//2
        left=self.sortArray(nums[:mid])
        right=self.sortArray(nums[mid:])
        return self.merge(left,right)
```
执行用时 :420 ms, 在所有 Python3 提交中击败了27.97%的用户

内存消耗 :20.5 MB, 在所有 Python3 提交中击败了100.00%的用户

###快速排序（Quick Sort）

用（list）分为两个子串（sub-lists）,选取一个“哨兵”(pivot)（通常选用数组的第一个数或最后一个数），
将小于pivot放在左边，把大于pivot放在右边，分割成两部分，并且可以固定pivot在数组的位置，在对左右两部分继续进行排序。

性质：不稳定，原址排序。

时间复杂度：基于随机选取主元的快速排序时间复杂度为期望O(nlogn)。

空间复杂度：O(logn)，平均期望情况下递归调用的层数最深为logn。

### python的code如下：


```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lens=len(nums)
        if lens<2:
            return nums
        def quick_sort(left,right):
            if left>=right:
                return nums
            pivot=left
            i,j=left,right
            while i<j:
                while i<j and nums[j]>nums[pivot]:
                    j-=1
                while i<j and nums[i]<=nums[pivot]:
                    i+=1
                nums[i],nums[j]=nums[j],nums[i]
            nums[pivot],nums[j]=nums[j],nums[pivot]
            quick_sort(left,j-1)
            quick_sort(j+1,right)
            return nums
        return quick_sort(0,lens-1)
```
执行用时 :312 ms, 在所有 Python3 提交中击败了53.15%的用户

内存消耗 :20 MB, 在所有 Python3 提交中击败了100.00%的用户