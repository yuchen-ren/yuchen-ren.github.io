---
layout:     post
title:      "Leetcode743"
subtitle:   "网络延迟时间"
date:       2020-6-29 23:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。








示例 1：
```
输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
输出：2
```
注意:

N 的范围在 [1, 100] 之间。
K 的范围在 [1, N] 之间。
times 的长度在 [1, 6000] 之间。
所有的边 times[i] = (u, v, w) 都有 1 <= u, v <= N 且 0 <= w <= 100。




###DFS

dist[node] 记录的是信号最早到达 node 的时间。当我们访问 node 时，若经过了传递时间这个信号是最早到达该节点的，则我们广播这个信号
为了加快速度，在访问每个节点时，若传递该信号的时间比已有信号到达的时间长，则我们退出该信号。

作者：LeetCode
链接：https://leetcode-cn.com/problems/network-delay-time/solution/wang-luo-yan-chi-shi-jian-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

时间复杂度：O(N^N + Elog E)其中 E是 times 的长度。

空间复杂度：O(N+E)，图的大小是 O(E)加上DFS中隐式调用堆栈的大小O(N)。





### python的code如下：


```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist={node:float('inf') for node in range(1,N+1)}
        def dfs(node,t):
            if t>=dist[node]:return 
            dist[node]=t
            for root,time in sorted(graph[node]):
                dfs(root,t+time)        
        dfs(K,0)
        ans=max(dist.values())
        return ans if ans<float('inf') else -1
```
超出时间限制。。。

###分治迭代



时间复杂度：O(nlogn)。

空间复杂度：O(1)。



### python的code如下：


```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right+left) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```
执行用时 :316 ms, 在所有 Python3 提交中击败了47.88%的用户

内存消耗 :15 MB, 在所有 Python3 提交中击败了6.67%的用户