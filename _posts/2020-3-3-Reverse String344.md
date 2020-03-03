---
layout:     post
title:      "Leetcode344"
subtitle:   " 反转字符串"
date:       2020-3-3 22:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。




示例1:
```
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```
示例2:
```
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```

## 双指针法
双指针法是使用两个指针，一个左指针 left，右指针 right，开始工作时 left 指向首元素，right 指向尾元素。
交换两个指针指向的元素，并向中间移动，直到两个指针相遇。

时间复杂度：O(N)。执行了N/2 次的交换。
空间复杂度：O(1)，只使用了常数级空间。
### c++的code如下：

```c
class Solution {
public:
    void reverseString(vector<char>& s) {
        int left=0;
        int right=s.size()-1;
        while(left<right)
        {
            swap(s[left],s[right]);
            left++;
            right--;
        }
    }
};
```
执行用时 :44 ms, 在所有 C++ 提交中击败了90.04%的用户

内存消耗 :15.3 MB, 在所有 C++ 提交中击败了10.60%的用户
### python的code如下：


```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse() #手动狗头
        lens=len(s)
        left,right=0,lens-1
        while left<right    :
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
```
执行用时 :240 ms, 在所有 Python3 提交中击败了50.46%的用户

内存消耗 :17.7 MB, 在所有 Python3 提交中击败了27.01%的用户

