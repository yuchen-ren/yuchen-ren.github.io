---
layout:     post
title:      "Leetcode206"
subtitle:   " 反转链表"
date:       2020-3-2 21:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

反转一个单链表。

示例:
```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？



## 迭代
使用双指针的方式进行迭代，定义两个指针pre和cur，cur先指向head，然后不断遍历cur。

在遍历的过程中将 cur 的 next 指向 pre，用一个中间的变量来存储原来的指向，然后 pre 和 cur 往后进一位。



### c++的code如下：


```c
* struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL) return NULL;
        ListNode* pre=NULL;
        ListNode* cur=head;
        while(cur)
        {
            ListNode* temp=cur->next;
            cur->next=pre;
            pre=cur;
            cur=temp;
        }
        return pre;
    }
};
```
执行用时 :8 ms, 在所有 C++ 提交中击败了78.19%的用户

内存消耗 :10.2 MB, 在所有 C++ 提交中击败了5.00%的用户
### python的code如下：


```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        pre=None
        cur=head
        while cur:
            #中间变量temp存储当前节点的下一节点
            temp=cur.next
            cur.next=pre
            #pre和cur往后移动一位
            pre=cur
            cur=temp
        return pre
```
执行用时 :40 ms, 在所有 Python3 提交中击败了65.15%的用户

内存消耗 :14.4 MB, 在所有 Python3 提交中击败了47.81%的用户

## 递归
递归处理好之后的，然后处理好现在的

我们首先通过递归确定尾端结点，并进行翻转操作，返回代表着我已经将你下一个结点以后的结点都翻转好了，只需要翻转你和你的下一个结点。


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
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next==NULL) return head;
        ListNode* cur=reverseList(head->next);
        head->next->next=head;
        head->next=NULL;
        return cur;      
    }
};
```
执行用时 :4 ms, 在所有 C++ 提交中击败了97.38%的用户

内存消耗 :10.3 MB, 在所有 C++ 提交中击败了5.08%的用户
### python的code如下：


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归终止条件是当前为空，或者下一个节点为空
        if head==None or head.next==None:
            return head
        # 这里的cur就是最后一个节点
        cur=self.reverseList(head.next)
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
		# 而head是4，head的下一个是5，下下一个是空
		# 所以head.next.next 就是5->4
        head.next.next=head
        # 防止链表循环，需要将head.next设置为空，比如5->4->5
        head.next=None
        # 每层递归函数都返回cur，也就是最后一个节点,也就是反转后的首节点
        return cur
```
执行用时 :40 ms, 在所有 Python3 提交中击败了64.97%的用户

内存消耗 :18.1 MB, 在所有 Python3 提交中击败了7.94%的用户

