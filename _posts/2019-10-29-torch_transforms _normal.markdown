---
layout:     post
title:      "torchvision.transforms"
subtitle:   " torch"
date:       2019-10-28 12:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - pytorch
---

> “ 使用pytorch中transforms的常用函数记录，方便自己记忆”

比如原来的tensor是三个维度的，值在0到1之间，经过以下变换之后就到了-1到1区间。

transforms.Normalize((.5,.5,.5),(.5,.5,.5))
1
transforms的源码中解释：

input[channel] = (input[channel] - mean[channel]) / std[channel]

假设你数据的范围是图片的数据范围四[0,1],那么如果mean = [.5, .5, .5],std = [.5, .5, .5],根据上述式子计算
(0−0.5)/0.5=−1 (0-0.5)/0.5= -1(0−0.5)/0.5=−1 ,(1−0.5)/0.5=1 (1-0.5)/0.5= 1(1−0.5)/0.5=1就可将数据归一化到[-1,1]。

疑问
在pytorch的官方教程里，经常看到

normalize = T.Normalize(mean = [0.485, 0.456, 0.406],
                         std = [0.229, 0.224, 0.225])
1
2
图片的RGB的范围不是[0,255]吗，那么图片的3个通道的像素值不应该是[0,255]吗？那么用这样的归一化参数怎么能归一化到[-1,1]呢?

解答
第一种情况：就是在加载数据集的时候就已经将图片转换为[0, 1]，例如imageNet数据集就是在加载ImageNet的数据的时候就转换成[0,1]。
第二种情况：
应用了torchvision.transforms.ToTensor，其作用是
（ Converts a PIL Image or numpy.ndarray (H x W x C) in the range [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0] ）

所以我们常常在代码中看到normallize在ToTensor之后

self.transforms = T.Compose([
                   T.Scale(224),
                   T.CenterCrop(224),
                   T.ToTensor(),
                   normalize
               ]


tensor.detach()
.clip
tensor.clamp