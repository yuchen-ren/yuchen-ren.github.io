---
layout:     post
title:      "Leetcode104"
subtitle:   " 二叉树的最大深度"
date:       2020-3-4 8:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。




示例:给定二叉树 [3,9,20,null,null,15,7]，
```
    3
   / \
  9  20
    /  \
   15   7
```
返回它的最大深度 3 。

## DFS递归
 DFS（深度优先搜索）策略:对于二叉树而言，它沿着树的深度遍历树的节点，
 尽可能深的搜索树的分支，这一过程一直进行到已发现从源节点可达的所有节点为止。
 
 方法：
```
        a
       / \
     b     c
   /  \   /  \
  d    e  f   g

```
顺序：a-b-d-e-c-f-g

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
    int maxDepth(TreeNode* root) {
        if(root==NULL) return 0;
        int leftdepth=maxDepth(root->left);
        int rightdepth=maxDepth(root->right);
        return (leftdepth>rightdepth?leftdepth:rightdepth)+1;
    }
};
```
执行用时 :12 ms, 在所有 C++ 提交中击败了72.96%的用户

内存消耗 :21.5 MB, 在所有 C++ 提交中击败了5.08%的用户
### python的code如下：


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        leftdepth=self.maxDepth(root.left)
        rightdepth=self.maxDepth(root.right)
        return max(leftdepth,rightdepth)+1
```
执行用时 :52 ms, 在所有 Python3 提交中击败了41.35%的用户

内存消耗 :14.9 MB, 在所有 Python3 提交中击败了28.74%的用户
## DFS迭代
 在递归中，如果层级过深，我们很可能保存过多的临时变量，导致栈溢出。这也是为什么我们一般不在后台代码中使用递归的原因。
 
 事实上，函数调用的参数是通过栈空间来传递的，在调用过程中会占用线程的栈资源。
 而递归调用，只有走到最后的结束点后函数才能依次退出，而未到达最后的结束点之前，
 占用的栈空间一直没有释放，如果递归调用次数过多，就可能导致占用的栈资源超过线程的最大值，
 从而导致栈溢出，导致程序的异常退出。

99%的递归转非递归，都可以通过栈来进行实现。



方法：
```
        a
       / \
     b     c
   /  \   /  \
  d    e  f   g

```
1：首先将a压入栈 
2：a弹栈，将c、b压入栈（注意顺序）
3：b弹栈，将e、d压入栈
4,5：d、e、c弹栈，将g、f压入栈
6：f、g弹栈



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
    int maxDepth(TreeNode* root) {
        if(root==NULL) return 0;
        stack<pair<int,TreeNode*>> st;
        st.push(pair<int,TreeNode*>(1,root));
        int depth=0;
        int cur_depth=0;
        while(!st.empty())
        {
            cur_depth=st.top().first;
            root=st.top().second;
            st.pop();
            depth=depth>cur_depth?depth:cur_depth;
            if (root->right) st.push(pair<int,TreeNode*>(cur_depth+1,root->right));
            if (root->left) st.push(pair<int,TreeNode*>(cur_depth+1,root->left));
        }
        return depth;
    }
};
```
执行用时 :8 ms, 在所有 C++ 提交中击败了93.06%的用户

内存消耗 :21.3 MB, 在所有 C++ 提交中击败了5.08%的用户
### python的code如下：


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        stack=[(1,root)]    #FILO
        depth=0
        while stack:
            cur_depth,root=stack.pop()
            depth=max(depth,cur_depth)
            if root.right:
                stack.append((cur_depth+1,root.right))
            if root.left:
                stack.append((cur_depth+1,root.left)) 
        return depth
```
执行用时 :44 ms, 在所有 Python3 提交中击败了80.74%的用户

内存消耗 :14.6 MB, 在所有 Python3 提交中击败了31.69%的用户

## BFS迭代
 从上到下，先把每一层遍历完之后再遍历一下一层.




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
    int maxDepth(TreeNode* root) {
        if(root==NULL) return 0;
        queue<pair<int,TreeNode*>> q;
        q.push(pair<int,TreeNode*>(1,root));
        int cur_depth=0;
        while(!q.empty())
        {
            cur_depth=q.front().first;
            root=q.front().second;
            q.pop();
            if (root->right) q.push(pair<int,TreeNode*>(cur_depth+1,root->right));
            if (root->left) q.push(pair<int,TreeNode*>(cur_depth+1,root->left));
        }
        return cur_depth;
    }
};
```
执行用时 :8 ms, 在所有 C++ 提交中击败了93.05%的用户

内存消耗 :21.5 MB, 在所有 C++ 提交中击败了5.08%的用户
### python的code如下：


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        queue=[(1,root)]    #FIFO
        while queue:
            cur_depth,root=queue.pop(0)#头部
            if root.left:
                queue.append((cur_depth+1,root.left)) 
            if root.right:
                queue.append((cur_depth+1,root.right))
        return cur_depth
```
执行用时 :40 ms, 在所有 Python3 提交中击败了92.60%的用户

内存消耗 :14.6 MB, 在所有 Python3 提交中击败了32.21%的用户
