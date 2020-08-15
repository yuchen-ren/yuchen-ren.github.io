---
layout:     post
title:      "Leetcode21"
subtitle:   "合并两个有序链表"
date:       2020-8-15 23:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 


示例 1：
```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

###动态规划

把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。

时间复杂度：O(n+m)。


空间复杂度：O(1)。

### python的code如下：


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        new_l=head
        left,right=l1,l2
        while left and right:
            if left.val<=right.val:
                new_l.next=left
                new_l=new_l.next
                left=left.next             
            else:
                new_l.next=right
                new_l=new_l.next
                right=right.next          
        if right:
            new_l.next=right
        elif left:
            new_l.next=left
        return head.next
```
执行用时：44 ms, 在所有 Python3 提交中击败了86.35%的用户

内存消耗：13.6 MB, 在所有 Python3 提交中击败了81.15%的用户