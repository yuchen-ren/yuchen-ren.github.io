---
layout:     post
title:      "Leetcode1382"
subtitle:   "将二叉搜索树变平衡"
date:       2020-3-30 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。

如果有多种构造方法，请你返回任意一种。





示例1：
```
输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
```
提示：

树节点的数目在 1 到 10^4 之间。
树节点的值互不相同，且在 1 到 10^5 之间。
###递归
1中序遍历得到从小到大的排序保存在数组中。

2将排好序的数组通过二分的方案进行切分，中间的点是根结点，左边是左子树，右边是右子树，然后递归将左子树切分，右子树切分。
[参考链接](https://leetcode-cn.com/problems/balance-a-binary-search-tree/solution/python3-shuang-100ti-jie-by-yang-jian-li/)

时间复杂度：O(n)+O(nlogn)=O(nlogn)。第一步中序遍历获取到排序好的结果：O(n)；第二部递归拆成了两个子问题T(n)=2T(n/2)+O(n)，由主定理知：O(nlogn)
空间复杂度：O(n)。

### python的code如下：


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mid_sort(self,root,res):
        if root:
            if root.left:
                self.mid_sort(root.left,res)
            res.append(root)
            if root.right:
                self.mid_sort(root.right,res)
    def createBST(self,res,left_idx,right_idx):
        mid=(left_idx+right_idx)//2
        mid_point=res[mid]
        mid_point.left=None
        mid_point.right=None
        if left_idx<mid:
            mid_point.left=self.createBST(res,left_idx,mid-1)
        if right_idx>mid:
            mid_point.right=self.createBST(res,mid+1,right_idx)
        return mid_point
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        res=[]
        self.mid_sort(root,res)
        return self.createBST(res,0,len(res)-1)
```
执行用时 :196 ms, 在所有 Python3 提交中击败了100.00%的用户

内存消耗 :18.2 MB, 在所有 Python3 提交中击败了100.00%的用户
