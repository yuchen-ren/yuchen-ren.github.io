---
layout:     post
title:      "Leetcode22"
subtitle:   "括号生成"
date:       2020-4-9 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：


```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

```
###动态规划

dp[i]：使用 i 对括号能够生成的组合。

dp[i] = "(" + dp[可能的括号对数] + ")" + dp[剩下的括号对数]

当我们清楚所有 i<n 时括号的可能生成排列后，对与 i=n 的情况，我们考虑整个括号排列中最左边的括号。
它一定是一个左括号，那么它可以和它对应的右括号组成一组完整的括号 "( )"，我们认为这一组是相比 n-1 增加进来的括号。

那么，剩下 n-1 组括号有可能在哪呢？

【这里是重点，请着重理解】

剩下的括号要么在这一组新增的括号内部，要么在这一组新增括号的外部（右侧）。

既然知道了 i<n 的情况，那我们就可以对所有情况进行遍历：

"(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】

其中 p + q = n-1，且 p q 均为非负整数。

事实上，当上述 p 从 0 取到 n-1，q 从 n-1 取到 0 后，所有情况就遍历完了。

注：上述遍历是没有重复情况出现的，即当 (p1,q1)≠(p2,q2) 时，按上述方式取的括号组合一定不同。


[参考链接](https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/)





### python的code如下：


```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        dp=[None]*(n+1)
        dp[0]=[""]
        for i in range(1,n+1):
            cur=[]
            for j in range(i):
                left=dp[j]
                right=dp[i-j-1]
                for s1 in left:
                    for s2 in right:
                        cur.append("("+s1+")"+s2)
            dp[i]=cur
        return dp[n]
```
执行用时 :40 ms, 在所有 Python3 提交中击败了65.73%的用户

内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.03%的用户
###BFS
没办法直接通过位数之和来进行暴力搜索，因为除了不满足位数的非解，还有满足位数但机器人不可到达的不可达解。

所以可以使用BFS和DFS。


时间复杂度：O(m*n）。

空间复杂度：O(m*n）。




### python的code如下：


```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sum_rc(row,col):     
            return row//10+row%10+col//10+col%10
        queue=collections.deque()
        queue.append((0,0))
        marked=set()
        while queue:
            x,y=queue.popleft()
            if sum_rc(x,y)<=k and (x,y) not in marked:
                marked.add((x,y))
                for dx,dy in [(1,0),(0,1)]:
                    i,j=x+dx,y+dy
                    if i>=0 and i<m and j>=0 and j<n:
                        queue.append((i,j))    
        return len(marked)
```
执行用时 :48 ms, 在所有 Python3 提交中击败了95.34%的用户

内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户

###DFS


时间复杂度：O(m*n）。

空间复杂度：O(m*n）。
### python的code如下：


```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sum_rc(row,col):     
            return row//10+row%10+col//10+col%10
        stack=[]
        stack.append((0,0))
        marked=set()
        while stack:
            x,y=stack.pop()
            if sum_rc(x,y)<=k and (x,y) not in marked:
                marked.add((x,y))
                for dx,dy in [(1,0),(0,1)]:
                    i,j=x+dx,y+dy
                    if i>=0 and i<m and j>=0 and j<n:
                        stack.append((i,j))    
        return len(marked)
```
执行用时 :44 ms, 在所有 Python3 提交中击败了98.62%的用户

内存消耗 :14 MB, 在所有 Python3 提交中击败了100.00%的用户