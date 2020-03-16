---
layout:     post
title:      "Leetcode754"
subtitle:   "到达终点数字"
date:       2020-3-15 23:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

在一根无限长的数轴上，你站在0的位置。终点在target的位置。

每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。

返回到达终点需要的最小移动次数。



示例 1：
```
输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
```


示例 2：
```
输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。
```
注意:

target是在[-10^9, 10^9]范围中的非零整数。

##数学规律
1、由于对称性 target是正或负不影响，实现时候取绝对值。

2、从0到n都取正步数才容易得最优解，于是先假设步数都取正，直到sum>=target，sum=target刚好。

3、当sum-target为偶数时，在前面已走的（sum-target）/2处取负即可，1+...-（sum-target）/2+...+k=target，那么答案依然是k。
比如sum-target=4，那么我们把2变成-2，那么sum减小了4。这是由于（1+2+3+...k）-（1-2+3...k）=4。

4、当sum-target为奇数时，情况比较复杂，所以可以直接让sum取值是满足sum-target为偶数。

时间复杂度：O($\sqrt{target}$)，求sum的过程等价于求等差数列的根，因此 为target的平方根级别。

空间复杂度：O(1)。


### python的code如下：


```python
class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)
        summ=0
        n=0
        while summ<target or (summ-target)%2!=0:
            n+=1
            summ+=n            
        return n
```
执行用时 :124 ms, 在所有 Python3 提交中击败了36.00%的用户

内存消耗 :13.5 MB, 在所有 Python3 提交中击败了8.33%的用户
### c++的code如下：

```c

```
