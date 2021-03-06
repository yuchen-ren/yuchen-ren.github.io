---
layout:     post
title:      "Leetcode118"
subtitle:   " 杨辉三角"
date:       2020-3-1 22:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
```
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


```
## 使用暴力遍历
建立二维数组，每行开头插入1，中间插入左上加右上，结尾插入1。

时间复杂度：O(numRows^2)

空间复杂度：O(numRows^2)
### c++的code如下：


```c
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res(numRows);//如果不预先指定外层vector的size，那内存是不确定的，是没法直接使用下标来索引的
        if(numRows==0)
        {
            return res;
        } 
        res[0].push_back(1);
        for(int i=1;i<numRows;i++)
        {
            res[i].push_back(1);
            for(int j=1;j<i;j++)
            {
                res[i].push_back(res[i-1][j-1]+res[i-1][j]);
            }
            res[i].push_back(1);
        }
        return res;

    }
};
```

执行用时 :0 ms, 在所有 C++ 提交中击败了100.00%的用户

内存消耗 :9 MB, 在所有 C++ 提交中击败了5.11%的用户
### python的code如下：


```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        
        if numRows==0:
            return res
        res.append([1])
        for i in range(1,numRows):
            res.append([])
            res[i].append(1)
            for j in range(1,i):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            res[i].append(1)
        return res

```
执行用时 :24 ms, 在所有 Python3 提交中击败了97.46%的用户

内存消耗 :13.4 MB, 在所有 Python3 提交中击败了32.88%的用户

