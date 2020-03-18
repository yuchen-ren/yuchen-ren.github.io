---
layout:     post
title:      "Leetcode215"
subtitle:   "数组中的第K个最大元素"
date:       2020-3-18 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例1：
```
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
```
示例2：
```
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
```
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。


##快速排序



时间复杂度：O(nlogn)。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def quick_sort(self,arr):
        n=len(arr)
        if n<2:
            return arr
        mid=arr[n//2]
        left,right=[],[]
        arr.remove(mid)
        for num in arr:
            if num>=mid:
                right.append(num)
            else:
                left.append(num)
        return self.quick_sort(right)+[mid]+self.quick_sort(left)      
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_sort(nums)[k-1]
```
执行用时 :68 ms, 在所有 Python3 提交中击败了73.04%的用户

内存消耗 :14.4 MB, 在所有 Python3 提交中击败了16.39%的用户
##堆排序
建立规模为k的最小堆，最终堆为前nums中前k个最大的数，顶点为其中最小的数，即我们要找的第k大的数。


时间复杂度：O(nlogk)。


空间复杂度：O(k)。


### python的code如下：


```python
class Solution:
    def sift_up(self,arr, k):
            new_val =arr[k]
            while (k > 0 and arr[(k-1)//2] > new_val):
                arr[k] = arr[(k-1)//2]
                k = (k-1)//2
            arr[k] = new_val 
    def sift_down(self,arr, k): 
            root=0          
            root_val = arr[root]
            while (2*root+1 < k):
                child = 2 * root + 1
                if child+1 < k and arr[child] > arr[child+1]:
                    child += 1
                if root_val> arr[child]:
                    arr[root] = arr[child]
                    root = child 
                else: break 
            arr[root] = root_val
    def findKthLargest(self, nums: List[int], k: int) -> int:      
        min_heap=[]
        for i in range(k):
            min_heap.append(nums[i])
            self.sift_up(min_heap,i)
        for num in nums[k:]:
            if num > min_heap[0]:
                min_heap[0] = num
                self.sift_down(min_heap, k)
        return min_heap[0]
```
执行用时 :60 ms, 在所有 Python3 提交中击败了79.50%的用户

内存消耗 :14 MB, 在所有 Python3 提交中击败了17.50%的用户