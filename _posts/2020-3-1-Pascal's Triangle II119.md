---
layout:     post
title:      "Leetcode119"
subtitle:   " 杨辉三角II"
date:       2020-3-2 00:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
```
输入: 3
输出: [1,3,3,1]

```
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

## 使用暴力遍历
思想和118题一样，建立二维数组的形式，直接取出索引对应一行。

时间复杂度：O(numRows^2)

空间复杂度：O(numRows^2)
### c++的code如下：


```c
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> res(rowIndex+1);      
        res[0].push_back(1);
        if(rowIndex==0)
        {
            return res[0];
        } 
        for(int i=1;i<rowIndex+1;i++)
        {
            res[i].push_back(1);
            for(int j=1;j<i;j++)
            {
                res[i].push_back(res[i-1][j-1]+res[i-1][j]);
            }
            res[i].push_back(1);
        }
        return res[rowIndex];
    }
};
```
执行用时 :0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗 :9.1 MB, 在所有 C++ 提交中击败了5.13%的用户
### python的code如下：


```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[]
        res.append(1)
        if rowIndex==0:
            return res   
        res.clear()
        res.append([1])    
        for i in range(1,rowIndex+1):
            res.append([])
            res[i].append(1)
            for j in range(1,i):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            res[i].append(1)
        return res[i]

```
执行用时 :
32 ms, 在所有 Python3 提交中击败了77.26%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了36.53%的用户

## 进阶
使用一维数组

假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),

则j-1变为[0,1,3,3,1]，与j行数据数量相同，

然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.

### c++的code如下：


```c
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res;      
        res.push_back(1);
        if(rowIndex==0)
        {
            return res;
        } 
        for(int i=1;i<rowIndex+1;i++)
        {
            res.insert(res.begin(),0);
            for(int j=0;j<i;j++)
            {
                res[j]=res[j]+res[j+1];
            }
        }
        return res;
    }
};
```
执行用时 :0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗 :8.8 MB, 在所有 C++ 提交中击败了17.58%的用户

或者：
```c
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res;      
        for(int i=0;i<rowIndex+1;i++)
        {
            res.push_back(1);
            for(int j=i-1;j>0;j--)
            {
                res[j]=res[j]+res[j-1];
            }
        }
        return res;
    }
};
```

执行用时 :0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗 :8.7 MB, 在所有 C++ 提交中击败了24.36%的用户


### python的code如下：


```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        if rowIndex==0:
            return res   
        for i in range(1,rowIndex+1):
            res.insert(0,0)
            for j in range(i):
                res[j]=res[j]+res[j+1]
        return res

```

执行用时 :40 ms, 在所有 Python3 提交中击败了33.32%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了35.12%的用户

