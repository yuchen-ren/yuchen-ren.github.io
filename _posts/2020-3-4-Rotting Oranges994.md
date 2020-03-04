---
layout:     post
title:      "Leetcode994"
subtitle:   " 腐烂的橘子"
date:       2020-3-4 14:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

 

示例 1：
```
输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
```
示例 1：
```
输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
```
示例 1：
```
输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
```




## 借助stack进行BFS迭代
 先找出腐烂的橘子，添加进 stack 中。
队列 stack 只让腐烂的橘子入队；
出队时，让当前腐烂橘子四周的新鲜橘子都变为腐烂，即 grid[newX][newY] = 2。
用 minute 记录腐烂的持续时间，每一层的橘子在内一层的橘子的腐烂时间基础之上自增 1，代表时间过了 1 分钟。
最后检查网格中是否还有新鲜的橘子：
有，返回 -1 代表 impossible。
没有则返回 minute。




### python的code如下：


```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 网格的长，宽
        m, n = len(grid), len(grid[0])
        # 找出最开始时，网格中所有坏橘子的坐标
        stack = [[y,x] for y in range(m) for x in range(n) if grid[y][x]==2]
        # 坏橘子传染好橘子的四个方向，上下左右
        direction = [[-1,0], [1,0], [0,-1], [0,1]]
        # 初始时间
        minute = 0
        
        # 开始坏橘子传染好橘子的循环，直到没有好橘子可以被传染
        while True:
            # 初始化一个stack_next，把这一轮变坏的橘子装进里面
            stack_next = []
            # 开始对坏橘子进行审查，主要是看上下左右有没有好橘子
            while stack:
                # 拿出坏橘子的坐标点
                y, x = stack.pop()
                # 再看坏橘子上下左右的坐标对应的坐标
                for d in direction:
                    y_new, x_new = y + d[0], x + d[1]
                    # 如果坐标在网格范围内，而且坐标没有被访问过，且这个坐标确实有个好橘子
                    if -1 < y_new < m and -1 < x_new < n and  grid[y_new][x_new] == 1:
                        # 告诉这个好橘子，你已被隔壁的坏橘子感染，现在你也是坏橘子了
                        grid[y_new][x_new] = 2
                        # 放进stack_next里面，集中管理，精准隔离，方便排查下一轮会变坏的橘子
                        stack_next.append([y_new, x_new])
            # 如果橘子们都检查完了发现再无其他坏橘子，终止循环，宣布疫情结束
            if not stack_next: break
            # 把这一轮感染的坏橘子放进stack里，因为我们每一轮都是从stack开始搜索的
            stack = stack_next
            # 看来橘子们还没凉透，来，给橘子们续一秒，哦不，续一分钟
            minute += 1
        
        # 经过传染，审查，隔离的循环后，如果还有好橘子幸存，返回-1宣布胜利，否则返回橘子们的存活时间
        return -1 if ['survive' for y in range(m) for x in range(n) if grid[y][x]==1] else minute



```
参考来自作者：quantumdriver
链接：https://leetcode-cn.com/problems/rotting-oranges/solution/python-bfs-jie-fa-dai-ma-fu-xiang-xi-jie-shi-by-qu/

执行用时 :52 ms, 在所有 Python3 提交中击败了87.76%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了17.24%的用户

### c++的code如下：

```c
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        queue<pair<int,int>> st;
        //st.reserve(m*n);
        //vector<pair<int,int>> st_new;
        //st_new.reserve(m*n);
        int x,y,x_new,y_new=0;        
        vector<pair<int,int>> dir;
        dir.push_back(make_pair(-1,0));
        dir.push_back(make_pair(1,0));
        dir.push_back(make_pair(0,-1));
        dir.push_back(make_pair(0,1));
        int minute=0;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]==2) 
                {
                    st.push(make_pair(i,j));
                }
                
            }
        }
        while(1)
        {
            int lens=st.size();
            for(int i=0;i<lens;i++)
            {
                y=st.front().first;
                x=st.front().second;
                st.pop();
                for(int i=0;i<4;i++)
                {
                    y_new=y+dir[i].first;
                    x_new=x+dir[i].second;
                    if (y>-1 && y_new<m && x>-1 && x_new<n && grid[y_new][x_new]==1)
                    {
                        grid[y_new][x_new]==2;
                        st.push(make_pair(y_new,x_new));
                    }
                }
                
            }
            if(st.empty()) break;
            //st=st_new;
            minute++;  
        }
        for(int i=0;i<m;i++)
            {
                for(int j=0;j<n;j++)
                {
                    if(grid[i][j]==1) 
                    {
                        return -1;
                    }
                }
            }
        return minute;
    }
};
```
执行用时 :4 ms, 在所有 C++ 提交中击败了91.53%的用户

内存消耗 :15.1 MB, 在所有 C++ 提交中击败了9.07%的用户
