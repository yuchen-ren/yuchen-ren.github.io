---
layout:     post
title:      "torchvision.transforms"
date:       2019-10-28 12:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - pytorch
---

> “torchvision.transforms是pytorch中的图像预处理包，常见的数据预处理和数据增强等操作都通过它来实现。 ”

举个例子：
```python
import torchvision.transforms as transforms

transforms.Compose([
    transforms.CenterCrop(10),
    transforms.ToTensor(),
    ])
```

下面列举transforms的常见类

## Resize
把图片的尺寸resize到给定尺寸
#如果输入为单个的int值，则将输入图像中最短的那条边resize到这个int值，长边根据比例进行调整，图像长宽比例不变
#如果输入为(h,w),且h、w为int值，则将图像resize到(h,w)尺寸



ToTensor ：把图片转换成张量convert a PIL image to tensor (H*W*C) in range [0,255] to a torch.Tensor(C*H*W) in the range [0.0,1.0]
Normalize ：Normalized an tensor image with mean and standard deviation


## 记录小白技术上的点点滴滴