---
layout:     post
title:      "Leetcode1039"
subtitle:   "多边形三角剖分的最低得分"
date:       2020-4-18 09:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

给定 N，想象一个凸 N 边多边形，其顶点按顺时针顺序依次标记为 A[0], A[i], ..., A[N-1]。

假设您将多边形剖分为 N-2 个三角形。对于每个三角形，该三角形的值是顶点标记的乘积，三角剖分的分数是进行三角剖分后所有 N-2 个三角形的值之和。

返回多边形进行三角剖分后可以得到的最低分。





示例 1：
```
输入：[1,2,3]
输出：6
解释：多边形已经三角化，唯一三角形的分数为 6。
```
示例 2：
```
输入：[3,7,4,5]
输出：144
解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。
```
示例 3：
```
输入：[1,3,1,4,1,5]
输出：13
解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。
```

###动态规划

dp[i][j]：表示从第i个到第j个角所形成的三角形的最小面积

dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])

时间复杂度：O(n^2)。

空间复杂度：O(n)。



### python的code如下：


```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        lens=len(nums)
        dp=[1]*lens
        count=[1]*lens
        max_c=0
        for i in range(lens):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[j]+1==dp[i]:
                        count[i]+=count[j]
            max_c=max(max_c,dp[i])
        ans=0
        for i in range(lens):
            if dp[i]==max_c:
                ans+=count[i]
        return ans
```
执行用时 :
1084 ms
, 在所有 Python3 提交中击败了
31.11%
的用户
内存消耗 :
13.7 MB
, 在所有 Python3 提交中击败了
20.00%
的用户
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