---
layout:     post
title:      "Leetcode543"
subtitle:   " 二叉树的直径"
date:       2020-3-10 00:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一棵二叉树，你需要计算它的直径长度。
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

例如:
给定二叉树: 


```
          1
         / \
        2   3
       / \     
      4   5    
```
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。



##DFS递归
时间复杂度：O(N)

空间复杂度：O(depth)，由于递归函数在递归过程中需要为每一层递归函数分配栈空间，所以这里需要额外的空间且该空间取决于递归的深度，
而递归的深度显然为二叉树的高度，并且每次递归调用的函数里又只用了常数个变量。


### python的code如下：


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxlens=0
        self.maxdepth(root)
        return self.maxlens
    def maxdepth(self,root):
        if not root:return 0
        left=self.maxdepth(root.left)
        right=self.maxdepth(root.right)
        self.maxlens=max(self.maxlens,left+right)
        return max(left,right)+1


```
执行用时 :52 ms, 在所有 Python3 提交中击败了64.46%的用户

内存消耗 :15.2 MB, 在所有 Python3 提交中击败了13.21%的用户
### c++的code如下：

```c

```

