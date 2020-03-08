---
layout:     post
title:      "数据的读取和操作(Dataset, DataLoader)"
subtitle:   " torch"
date:       2020-1-9 15:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - pytorch
---

> “ 使用pytorch中transforms的常用函数记录，方便自己记忆”

把原始数据处理为模型使用的数据需要3步：torch.utils.data.Dataset 、transforms.Compose、 torch.utils.data.DataLoader 分别可以理解为数据处理格式的定义、数据预处理和数据加载。
其中transforms.Compose已经在前面的内容[torchvision.transforms](https://yuchen-ren.github.io/2019/10/28/torch_transforms/)和[我的另一篇博客](https://yuchen-ren.github.io/2019/10/29/torch_transforms-_normal/)所介绍。


## Dataset
Dataset位于torch.utils.data.Dataset，每当我们自定义类MyDataset必须要继承它并实现其两个成员函数：

* __len__()
* __getitem__()
例如：
```python
import torch
from torch.utils.data import Dataset
import pandas as pd

# 定义自己的类
class MyDataset(Dataset):

    # 初始化
    def __init__(self, file_name):
        # 读入数据
        self.data = pd.read_csv(file_name)

    # 返回df的长度
    def __len__(self):
        return len(self.data)

    # 获取第idx+1列的数据
    def __getitem__(self, idx):
        return self.data[idx].label

# 通过实例化对象来访问该类
# 假设同目录下存在名为median_benchmark.csv的文件
ds = MyDataset('median_benchmark.csv')

'''
len(ds)     返回数据总数
ds[101]     返回索引处的数据
'''
```

## DataLoader
DataLoader位于torch.utils.data.DataLoader, 为我们提供了对Dataset的读取操作
```python
# 仅仅列举了常用的几个参数
torch.nn.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)
```
* dataset : 上面所实现的自定义类Dataset
* batch_size : 默认为1，每次读取的batch的大小
* shuffle : 默认为False， 是否对数据进行shuffle操作(简单理解成将数据集打乱)
* num_works : 默认为0，表示在加载数据的时候每次使用子进程的数量，即简单的多线程预读数据的方法
DataLoader返回的是一个迭代器，我们通过这个迭代器来获取数据
Dataloder的目的是将给定的n nn个数据, 经过Dataloader操作后, 在每一次调用时调用一个小batch, 如:

* 给出的是: (5000,28,28) (5000, 28, 28)(5000,28,28), 表示有5000 50005000个样本,每个样本的size为(28,28) (28, 28)(28,28)
* 经过Dataloader处理后, 一次得到的是(100,28,28) (100, 28, 28)(100,28,28)(假设batch_size大小为100), 表示本次取出100个样本, 每个样本的size为(28,28) (28,28)(28,28)

参考资料
* [1].[https://blog.csdn.net/hacker_Dem_br/article/details/88959443](https://blog.csdn.net/hacker_Dem_br/article/details/88959443)
