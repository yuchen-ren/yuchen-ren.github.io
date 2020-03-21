---
layout:     post
title:      "Leetcode365"
subtitle:   "水壶问题"
date:       2020-3-21 18:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好z升的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的z升水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空


示例1：(From the famous "Die Hard" example)
```
输入: x = 3, y = 5, z = 4
输出: True

装满y，倒进x中，y中剩余2，将x中倒掉，再将y中2L水倒入x中；

再次重复装满y，倒进x中的操作，此时y中剩余4L水了。
```
示例2：
```
输入: x = 2, y = 6, z = 5
输出: False
```


##数学解法（gcd）
首先，从两个水壶里的整体水量来看，每次操作，可分为下列情况：
1.往空壶里加满水，总量加x/y；
2.倒掉一壶水（满），总量减x/y；
3.倒掉一壶水（不满），总量变成x/y/0；
4.往不满的壶里加水，总量变为x/y/x+y；
5.从一个壶往另一个壶里倒水，总量不变；


所以，两个壶里水的总量一定是ax+by（a,b为整数），立即推，当z=ax+by时，返回true。

然后是贝祖定理：若x,y是整数,且gcd(x,y)=d，那么对于任意的整数a,b,ax+by都一定是d的倍数，特别地，一定存在整数a,b，使ax+by=d成立。

由贝祖定理可知，若存在整数a,b，使得ax+by=z成立，则z一定为x.y最大公因数的整数倍。

证明如下：

设x,y的最大公因数为d；
故存在整数i,j,使得x=id,y=jd；
若ax+by=z成立，则
ax+by = a*(id)+b(jd) = (ai+b*j)*d = z；
由此可得，z为d的整数倍。

所以，这道题就变成了判断z是否是x,y最大公因数的整数倍

[参考链接](https://leetcode-cn.com/problems/water-and-jug-problem/solution/cyu-yan-shu-xue-jie-fa-tai-xiu-liao-dai-ma-jian-ji/)



时间复杂度：O(log(min(x,y)))。


空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def gcd(self,x,y):
        max_jug=max(x,y)
        min_jug=min(x,y)
        return min_jug if max_jug%min_jug==0 else self.gcd(min_jug,max_jug%min_jug) 
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y<z:
            return False
        if x==0 or y==0 or x+y==z :
            return z==0 or z==x+y      
        max_com=self.gcd(x,y)
        return True if z%max_com==0 else False
```
执行用时 :36 ms, 在所有 Python3 提交中击败了70.93%的用户

内存消耗 :13.6 MB, 在所有 Python3 提交中击败了14.58%的用户

##DFS
时间复杂度：O(xy)，状态数最多有 (x+1)(y+1)种，对每一种状态进行深度优先搜索的时间复杂度为 O(1)，因此总时间复杂度为 O(xy)。

空间复杂度：O(xy)，由于状态数最多有 (x+1)(y+1)种，哈希集合中最多会有 (x+1)(y+1)项，因此空间复杂度为 O(xy)。

[参考链接](https://leetcode-cn.com/problems/water-and-jug-problem/solution/shui-hu-wen-ti-by-leetcode-solution/)

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        self.seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in self.seen:
                continue
            self.seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False
```