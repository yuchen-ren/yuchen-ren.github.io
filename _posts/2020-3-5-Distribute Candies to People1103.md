---
layout:     post
title:      "Leetcode1103"
subtitle:   " 分糖果 II"
date:       2020-3-5 14:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
排排坐，分糖果。

我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。

给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。

然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。

重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。
注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。

返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。



 

示例 1：
```
输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。

```
示例 2：
```
输入：candies = 10, num_people = 3
输出：[5,2,3]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0]。
第三次，ans[2] += 3，数组变为 [1,2,3]。
第四次，ans[0] += 4，最终数组变为 [5,2,3]。

```
提示：

1 <= candies <= 10^9
1 <= num_people <= 1000




## 暴力循环
对小朋友们进行遍历，每次都发小朋友们应得数量的糖，直到剩下的糖不足以分发应得数量，就直接给最后那个孩子

时间复杂度O(N)
空间复杂度O(N)
### python的code如下：


```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*num_people
        epoch=0
        while True:
            for i in range(num_people):
                cur_num=num_people*epoch+i+1 #该对i号孩子发的糖的数量
                if candies<cur_num:
                    res[i]+=candies
                    candies=0
                    break;
                res[i]+=(cur_num)
                candies-=(cur_num)
            epoch+=1
            if candies==0 :break
        return res
```

执行用时 :40 ms, 在所有 Python3 提交中击败了77.64%的用户

内存消耗 :13.3 MB, 在所有 Python3 提交中击败了23.58%的用户

### c++的code如下：

```c

```
执行用时 :4 ms, 在所有 C++ 提交中击败了91.53%的用户

内存消耗 :15.1 MB, 在所有 C++ 提交中击败了9.07%的用户

## 通过等差数列
对小朋友们进行遍历，每次都发小朋友们应得数量的糖，直到剩下的糖不足以分发应得数量，就直接给最后那个孩子

时间复杂度O(N)
空间复杂度O(N)
### python的code如下：


```python
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*num_people
        p=int((2*candies+0.25)**0.5-0.5) #正常孩子次数
        r=int(candies-(p+1)*p*0.5) #最后一个孩子拿到糖的个数
        epoch=p//num_people  #轮数
        pos=p%num_people  #最后一个孩子的位置
        for i in range(num_people):
            res[i]=epoch*(i+1)+int(0.5*num_people*epoch*(epoch-1))
            if i<pos:
                res[i]+=(i+1)+num_people*epoch
        res[pos]+=r
        return res

```

执行用时 :32 ms, 在所有 Python3 提交中击败了95.96%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了23.58%的用户

### c++的code如下：

```c

```
执行用时 :4 ms, 在所有 C++ 提交中击败了91.53%的用户

内存消耗 :15.1 MB, 在所有 C++ 提交中击败了9.07%的用户
