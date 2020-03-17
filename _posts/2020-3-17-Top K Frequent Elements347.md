---
layout:     post
title:      "Leetcode347"
subtitle:   "前 K 个高频元素"
date:       2020-3-17 12:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。



示例1：
```
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```
示例2：
```
输入: nums = [1], k = 1
输出: [1]
```
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。


##哈希表

直接利用collections.Counter构建哈希表，然后用most_common函数直接找到topk。

时间复杂度：O(nlogk)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in collections.Counter(nums).most_common(k)]
```
执行用时 :120 ms, 在所有 Python3 提交中击败了71.35%的用户

内存消耗 :17.8 MB, 在所有 Python3 提交中击败了6.09%的用户
##最小堆

利用哈希表和最小堆。
[参考解析](https://leetcode-cn.com/problems/top-k-frequent-elements/solution/python-dui-pai-xu-by-xxinjiee/)

时间复杂度：O(nlogk)。


空间复杂度：O(n)。


### python的code如下：


```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap 统计频率
        freq_count = {}
        for num in nums:
            if num in freq_count:
                freq_count[num] += 1
            else:
                freq_count[num] = 1

        def sift_up(arr, k):
            """ 时间复杂度 O(logk) k 为堆的规模"""
            new_index= k
            new_val=arr[new_index]
            while (new_index > 0 and arr[(new_index-1)//2][1] > new_val[1]):
                arr[new_index] = arr[(new_index-1)//2]
                new_index = (new_index-1)//2
            arr[new_index] = new_val # 这里采用的是类似插入排序的赋值交换

        def sift_down(arr, root, k):
            """ O(logk). 右节点index 2*root+1，左节点 2*root+1, 父节点 (child-1)//2"""
            root_val = arr[root]
            while (2*root+1 < k):
                # 右节点 2*root+1，左节点 2*root+1, 父节点 (child-1)//2
                child = 2 * root + 1
                # 小顶锥 用 >，大顶锥 用 <
                if child+1 < k and arr[child][1] > arr[child+1][1]:
                    child += 1
                if root_val[1] > arr[child][1]:
                    arr[root] = arr[child]
                    root = child # 继续向下检查
                else: break # 如果到这里没乱序，不用再检查后续子节点
            arr[root] = root_val

        # 注意构造规模为k的堆, 时间复杂度O(n)，因为堆的规模是从0开始增长的
        freq_list = list(freq_count.items())
        min_heap = []
        for i in range(k):
            min_heap.append(freq_list[i])
            print(min_heap)
            sift_up(min_heap, i)

        # 遍历剩下元素，大于堆顶入堆，下沉维护小顶堆
        for item in freq_list[k:]:
            priority = item[1]
            if priority > min_heap[0][1]:
                min_heap[0] = item
                sift_down(min_heap, 0, k)

        return [item[0] for item in min_heap]
```

