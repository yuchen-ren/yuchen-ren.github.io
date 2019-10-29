---
layout:     post
title:      "transforms.Normalize"
subtitle:   " torch"
date:       2019-10-29 22:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - pytorch
---

> “ 使用pytorch中transforms的Normalize记录，方便自己记忆”

比如原来的tensor是三个维度的，则其作用就是先将输入归一化到(0,1)，再使用公式”(x-mean)/std”，将每个元素分布到(-1,1)
```
transforms.Normalize((.5,.5,.5),(.5,.5,.5))
```

transforms的源码中解释：

$$
 input[channel] = (input[channel] - mean[channel]) / std[channel]
$$

假设你图片的数据范围是[0,1],那么如果mean = [.5, .5, .5],std = [.5, .5, .5],根据上述式子计算
(0−0.5)/0.5=−1  ,(1-0.5)/0.5= 1就可将数据归一化到[-1,1]。

# 疑问1
RGB单个通道的像素值不应该是[0, 255]吗？所以一个通道的均值应该在127附近才对。
如果Normalize()函数按照下面的版式去计算 x = (x - mean)/std 因为RGB是[0, 255]，算出来的x就不可能落在[-1, 1]区间了。

# 解答1
有两种情况：
a)就是在加载数据集的时候就已经将图片转换为[0, 1]，例如imageNet数据集就是在加载ImageNet的数据的时候就转换成[0,1]。
b)应用了torchvision.transforms.ToTensor，其作用是
（ Converts a PIL Image or numpy.ndarray (H x W x C) in the range [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0] ）

# 疑问2
在pytorch的官方教程里，经常看到
normalize = transforms.Normalize(mean = [0.485, 0.456, 0.406],
                         std = [0.229, 0.224, 0.225])
这一组值是怎么来的？

# 解答2
这是在ImageNet 100万张图片上计算得到的图片的均值和标准差，可以估算得知这时图片的分布范围大概在(0-0.485)/0.229=-2.1和(1-0.406)/0.225=2.7之间。
尽管这时它的分布在-2.1 ~ 2.7，但是它的均值接近0，标准差接近1，采用ImageNet图片的均值和标准差作为标准化参数的目的是图像的各个像素的分布接近标准分布。


#计算自己的数据集的均值和方差
如果你想要计算自己的数据集的均值和方差，
让其作为你的transforms.Normalize函数的参数的话可以参考[计算图像数据集的均值和方差](https://www.cnblogs.com/wanghui-garcia/p/11448460.html)




tensor.detach()
.clip
tensor.clamp