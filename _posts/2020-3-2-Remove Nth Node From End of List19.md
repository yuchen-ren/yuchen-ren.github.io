---
layout:     post
title:      "Leetcode19"
subtitle:   " 删除链表的倒数第N个节点"
date:       2020-3-2 15:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例:
```
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
```
说明：

给定的 n 保证是有效的。

进阶:

你能尝试使用一趟扫描实现吗？



## 使用两次遍历
第一遍遍历，先求出链表的总长度，即找出从n从前面数的位置。

第二遍遍历的时候，根据总长度k的值减去n，就算出需要再遍历多少个节点，找到要删除的节点的前一个节点x。
然后将x节点的next指针指向下下一个节点就可以删除节点了。

时间复杂度：O(L)，该算法对列表进行了两次遍历，首先计算了列表的长度 L其次找到第 (L−n) 个结点。 操作执行了2L−n 步，时间复杂度为O(L)。

空间复杂度：O(1)，我们只用了常量级的额外空间。



* 注：链表类题目，在前面加一个哑结点，方便边界处理！
### c++的code如下：


```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {

    }
};/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p=new ListNode(0); 
        p->next=head;
        ListNode* front=p;
        int lens=0;
        while(front->next)
        {
            front=front->next;
            lens++;
        }
        int num=lens-n;
        front=p;
        for(int i=0;i<num;i++)
        {
            front=front->next;
        }
        front->next=front->next->next;
        return p->next;
    }
};
```
执行用时 :8 ms, 在所有 C++ 提交中击败了51.31%的用户

内存消耗 :12.9 MB, 在所有 C++ 提交中击败了5.35%的用户
### python的code如下：


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        p=ListNode(0) #虚拟节点
        p.next=head
        front=p #第一次遍历
        lens=0      
        while front.next:
            front=front.next
            lens+=1
        num=lens-n #从0正数，要删节点到head的间隔数+1
        front=p
        for i in range(num):#找到删除节点的前一个节点
            front=front.next
        front.next=front.next.next
        return p.next
```
执行用时 :36 ms, 在所有 Python3 提交中击败了69.65%的用户

内存消耗 :13.3 MB, 在所有 Python3 提交中击败了26.35%的用户

## 使用一次遍历
用双指针法，只经过一次遍历

定义前后两个指针front和rear，使两个指针之间的间隔保持n，后面的指针rear负责找链表尾端，则front找到删除节点的前一个节点

### c++的code如下：


```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next==NULL)
        {
            return NULL;
        }
        ListNode* p=new ListNode(0); 
        p->next=head;
        ListNode* front=p;
        ListNode* rear=p;
        while(n)
        {
            rear=rear->next;
            n--;
        }
        while(rear->next)
        {
            front=front->next;
            rear=rear->next;
        }
        front->next=front->next->next;
        return p->next;
        
    }
};
```
执行用时 :8 ms, 在所有 C++ 提交中击败了51.31%的用户

内存消耗 :12.8 MB, 在所有 C++ 提交中击败了5.35%的用户

### python的code如下：


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        p=ListNode(0) #虚拟节点
        p.next=head
        front=p #前指针
        rear=p #后指针
        while(n):
            rear=rear.next
            n-=1
        while(rear.next):
            front=front.next
            rear=rear.next
        front.next=front.next.next
        return p.next
```
执行用时 :40 ms, 在所有 Python3 提交中击败了46.26%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了26.35%的用户

