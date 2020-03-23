---
layout:     post
title:      "Leetcode876"
subtitle:   "链表的中间结点"
date:       2020-3-23 10:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

示例1：
```
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
```
示例2：
```
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
```
提示：

给定链表的结点数介于 1 和 100 之间。

##单指针法
首先遍历一遍得到链表的长度，然后就可以得知中点的位置。

第二遍遍历到中点的地方。

时间复杂度：O(n)+O(n/2)=O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        lens=1
        p1=head
        while p1.next:
            p1=p1.next
            lens+=1
        mid=lens//2+1
        for i in range(1,mid):
            head=head.next
        return head
```
执行用时 :36 ms, 在所有 Python3 提交中击败了54.54%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.55%的用户


##单指针+数组辅助
在上面单指针的方法上，可以牺牲一些空间来换取时间，用一个数组来保存链表里的数，这样就不需要第二遍遍历了。

时间复杂度：O(n)。

空间复杂度：O(n)。


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        lens=1       
        p1=head
        nums=[p1]
        while p1.next:
            p1=p1.next
            lens+=1
            nums.append(p1)
        return nums[lens//2]
```
执行用时 :36 ms, 在所有 Python3 提交中击败了54.54%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了5.55%的用户

##快慢双指针法
只需一次遍历，快指针步长为慢指针的两倍，即快指针指到结尾时，慢指针指到中间。

时间复杂度：O(n)。


空间复杂度：O(1)。


### python的code如下：


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        lens=1
        p1=head
        while p1.next!=None:
            p1=p1.next
            lens+=1
        mid=lens//2+1
        for i in range(1,mid):
            head=head.next
        return head
```
执行用时 :36 ms, 在所有 Python3 提交中击败了54.54%的用户

内存消耗 :13.3 MB, 在所有 Python3 提交中击败了5.55%的用户