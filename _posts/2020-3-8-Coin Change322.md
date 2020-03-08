---
layout:     post
title:      "Leetcode322"
subtitle:   " 零钱兑换"
date:       2020-3-8 10:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。





示例 1：
```
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1

```
示例 2：
```
输入: coins = [2], amount = 3
输出: -1
```
说明:
你可以认为每种硬币的数量是无限的。




## 贪心 + DFS


参考了大佬的思路，这里有详细介绍[参考来源](https://leetcode-cn.com/problems/coin-change/solution/322-by-ikaruga/)


### python的code如下：


```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lens=len(coins)
        #i=lens-1
        j=lens-1
        flag=0
        coins.sort()     
        while j>=0:
            i=j
            dif=amount
            while i>=0: 
                print(i) 
                print(dif)        
                if dif==coins[i]:
                    return flag+1
                elif dif>coins[i]:
                    dif-=coins[i]
                    flag+=1
                    while dif>=coins[i]:
                        dif-=coins[i] 
                        flag+=1
                i-=1
            print(dif)
            if dif!=0: j-=1
            else: break 
        return flag if dif==0 else -1


```
执行用时 :276 ms, 在所有 Python3 提交中击败了60.77%的用户

内存消耗 :16.9 MB, 在所有 Python3 提交中击败了100.00%的用户

### c++的code如下：

```c

```
## 通过双端队列
通过一个递减的双端队列来记录最大值。

时间复杂度：O(1)（插入，删除，求最大值）
当second中的值用完后，插入操作虽然看起来有循环，做一个插入操作时最多可能会有n次出队操作。
但要由于每个数字只会出队一次，因此对于所有的n个数字的插入过程，对应的所有出队操作也不会大于n次。
因此将出队的时间均摊到每个插入操作上，时间复杂度为 O(1)。

空间复杂度：O(n)


### python的code如下：


```python
import queue
class MaxQueue:

    def __init__(self):
        self.deque=queue.deque()
        self.sortdeque=queue.deque()


    def max_value(self) -> int:
        return self.sortdeque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        self.deque.append(value)
        while self.sortdeque and value>self.sortdeque[-1]:
            self.sortdeque.pop()
        self.sortdeque.append(value)


    def pop_front(self) -> int:
        if not self.deque:
            return -1
        val=self.deque.popleft()
        if val==self.sortdeque[0]:
            self.sortdeque.popleft()
        return val



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
```
执行用时 :256 ms, 在所有 Python3 提交中击败了81.22%的用户

内存消耗 :16.8 MB, 在所有 Python3 提交中击败了100.00%的用户


### c++的code如下：

```c
class Solution {
public:
    void coinChange(vector<int>& coins, int amount, int c_index, int count, int& ans)
    {
        if (amount == 0)
        {
            ans = min(ans, count);
            return;
        }
        if (c_index == coins.size()) return;

        for (int k = amount / coins[c_index]; k >= 0 && k + count < ans; k--)
        {
            coinChange(coins, amount - k * coins[c_index], c_index + 1, count + k, ans);
        }
    }

    int coinChange(vector<int>& coins, int amount)
    {
        if (amount == 0) return 0;
        sort(coins.rbegin(), coins.rend());
        cout<<coins[0]<<endl;
        int ans = INT_MAX;
        coinChange(coins, amount, 0, 0, ans);
        return ans == INT_MAX ? -1 : ans;
    }

};
```
执行用时 :
16 ms
, 在所有 C++ 提交中击败了
97.82%
的用户
内存消耗 :
12.3 MB
, 在所有 C++ 提交中击败了
88.64%
的用户

## 通过双辅助数
用first来保存当前队列中最大的数，用second来保存第二大的，first中的数被弹出后再取second中的数
本意是对上一种方法的优化，减少了一个额外队列的空间，但这样貌似时间不能平均了。

时间复杂度：O(1)（插入，求最大值），O(n)（删除）。

空间复杂度：O(n)


### python的code如下：


```python
import queue
class MaxQueue:

    def __init__(self):
        self.deque=queue.deque()
        self.first=-1
        self.second=-1


    def max_value(self) -> int:
        #print(self.first)
        return self.first


    def push_back(self, value: int) -> None:
        if value>=self.first :
            self.second=self.first
            self.first=value
        #此时second不能无值，不然不知道deque里是否还有第二大比value大的,会影响下一次first的取值
        elif self.second>0 and self.second<value<self.first: 
            self.second=value
        self.deque.append(value)



    def pop_front(self) -> int:
        if not self.deque:
            return -1
        val=self.deque.popleft()
        if val==self.first:
            if self.second==-1 :#first无值，second也无值
                self.first=-1
                for v in self.deque:
                    if v>self.first :
                        self.second=self.first
                        self.first=v
                    elif self.second<v<=self.first:
                        self.second=v
            else:              #first无值，second有值
                self.first=self.second
                self.second=-1
        elif val==self.second : #first有值，second无值
            self.second=-1
        return val



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
```
执行用时 :260 ms, 在所有 Python3 提交中击败了77.62%的用户

内存消耗 :16.9 MB, 在所有 Python3 提交中击败了100.00%的用户


### c++的code如下：

```c

```
