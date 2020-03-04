---
layout:     post
title:      "Leetcode102"
subtitle:   " 二叉树的层次遍历"
date:       2020-3-4 14:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],


```
    3
   / \
  9  20
    /  \
   15   7
```
返回其层次遍历结果：
```
[
  [3],
  [9,20],
  [15,7]
]
```



## 借助queue进行BFS迭代
 从上到下，先把每一层遍历完之后再遍历一下一层.

需要借助一个queue来记录当前的root。


方法：
```
        a
       / \
     b     c
   /  \   /  \
  d    e  f   g

```
我们可以使用Queue的数据结构。我们将root节点初始化进队列，通过消耗尾部，插入头部的方式来完成BFS。

 a->b->c->d->e->f->g

一句话来说就是将当前结点弹出栈并推入子结点，每一步都会更新深度。

时间复杂度：O(N)。

空间复杂度：O(N)。
### c++的code如下：

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root==NULL) return res;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty())
        {
            int width=q.size();          
            vector<int> v;          
            for(int i=0;i<width;i++)
            {
                root=q.front();
                q.pop();
                v.push_back(root->val);
                if (root->left) q.push(root->left);
                if (root->right) q.push(root->right);
            }
            res.push_back(v);
        }
        return res;
    }
};
```
执行用时 :4 ms, 在所有 C++ 提交中击败了91.53%的用户

内存消耗 :15.1 MB, 在所有 C++ 提交中击败了9.07%的用户
### python的code如下：


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        queue=[(0,root)]
        depth=0
        res=[[]]
        while(queue):
            cur_depth,root=queue.pop(0)
            if cur_depth!=depth:              
                res.append([])           
                depth=cur_depth
            res[depth].append(root.val)
            if root.left:
                queue.append((cur_depth+1,root.left))
            if root.right:
                queue.append((cur_depth+1,root.right))
        return res
```
执行用时 :
36 ms, 在所有 Python3 提交中击败了78.65%的用户

内存消耗 :13.6 MB, 在所有 Python3 提交中击败了20.82%的用户
