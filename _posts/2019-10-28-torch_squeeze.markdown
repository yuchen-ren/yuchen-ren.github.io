---
layout:     post
title:      "torch_squeeze"
subtitle:   " torch"
date:       2019-10-28 16:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - pytorch
---

> “ 使用pytorch中squeeze的函数记录，方便自己记忆”

squeeze的用法主要就是对数据的维度进行压缩或者解压。
例如，有：
```python
a=torch.randn(1,3)
print(a)
print(a.shape)
```
```
tensor([[ 0.1661, -0.1637,  0.3711]])
torch.Size([1, 3])
```
## torch.squeeze()
这个函数主要对数据的维度进行压缩，去掉维数为1的的维度，比如是一行或者一列这种，一个一行三列（1,3）的数去掉第一个维数为一的维度之后就变成（3）行。
* squeeze(a)就是将a中所有为1的维度删掉。不为1的维度没有影响。
* a.squeeze(N) 就是去掉a中指定的维数为一的维度。
* 还有一种形式就是b=torch.squeeze(a，N) a中去掉指定的定的维数为一的维度。
例如：
```python
b=torch.squeeze(a)
print(b)
print(b.shape)
```
```
tensor([0.1791, 0.5866, 0.0276])
torch.Size([3])
```


## torch.unsqueeze()
这个函数主要是对数据维度进行扩充。给指定位置加上维数为一的维度，比如原本有个三行的数据（3），在0的位置加了一维就变成一行三列（1,3）。
* squeeze(a)就是将a中加上维度为1的维度。
* a.squeeze(N) 就是在a中指定位置N加上一个维数为1的维度。
* 还有一种形式就是b=torch.squeeze(a，N) a就是在a中指定位置N加上一个维数为1的维度。
```python
c=a.unsqueeze(0)
print(c)
print(c.shape)
d=torch.unsqueeze(a,1)
print(d)
print(d.shape)
```
```
tensor([[[ 0.9096, -0.3957,  1.5550]]])
torch.Size([1, 1, 3])
tensor([[[ 0.9096, -0.3957,  1.5550]]])
torch.Size([1, 1, 3])
```







