---
layout:     post
title:      "Leetcode208"
subtitle:   "实现 Trie (前缀树)"
date:       2020-3-28 21:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
    - leetcode
---
题目要求：

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。




示例1：
```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true

```
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

##字典树
###键插入
时间复杂度：O(m)，其中m为键长。在算法的每次迭代中，我们要么检查要么创建一个节点，直到到达键尾。只需要m次操作。

空间复杂度：O(m)。最坏的情况下，新插入的键和Trie树中已有的键没有公共前缀。此时需要添加m个结点，使用O(m)空间。
###键查找

时间复杂度:O(m)。算法的每一步均搜索下一个键字符。最坏的情况下需要m次操作。

空间复杂度:O(1)。
###键前缀查找

时间复杂度:O(m)。

空间复杂度:O(1)。

### python的code如下：


```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup={}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree=self.lookup
        for a in word:
            if a not in tree:
                tree[a]={}
            tree=tree[a]           
        tree["#"]="#"


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree=self.lookup
        for a in word:
            if a not in tree:
                return False
            tree=tree[a]
        if "#"in tree:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree=self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree=tree[a]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
执行用时 :140 ms, 在所有 Python3 提交中击败了82.03%的用户

内存消耗 :26.5 MB, 在所有 Python3 提交中击败了28.77%的用户