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

torchvision.transforms是pytorch中的图像预处理包，常见的数据预处理和数据增强等操作都通过它来实现。
举个例子：
```python
import torchvision.transforms as transforms

transforms.Compose([
    transforms.CenterCrop(10),
    transforms.ToTensor(),
    ])
```

下面列举transforms的常见类
## Compose
用来管理各个transforms操作，其中__call__方法就是对输入img遍历所有的transforms操作
```python
class Compose(object):
    """Compose several transforms together

    Args:
        transforms (list of"Transform"objects):list of transforms to compose.
    """
    def __init__(self,transforms):
        self.transforms=transforms

    def __call__(self,img):
        for t in self.transforms:
            img=t(img)
        return img

    def __repr__(self):
        format_string=self.__class__.__name__+'('
        for t in self.transforms:
            format_string+='\n'
            format_string+='    {0}.format(t)
        format_string+='\n)'
        return format_strin
```
## Resize
把图片的尺寸resize到给定尺寸。
* 如果输入为单个的int值，则将输入图像中最短的那条边resize到这个int值，长边根据比例进行调整，图像长宽比例不变
* 如果输入为(h,w),且h、w为int值，则将图像resize到(h,w)尺寸
在__call__方法中调用了functional.py脚本中的resize函数来完成resize操作。因为输入是PIL Image，所以resize函数基本是在调用Image的各种方法。
```python
class Resize(object):
    """Resize the input PIL Image to the given size.

    Args:
        size (sequence or int): Desired output size. If size is a sequence like
            (h, w), output size will be matched to this. If size is an int,
            smaller edge of the image will be matched to this number.
            i.e, if height > width, then image will be rescaled to
            (size * height / width, size)
        interpolation (int, optional): Desired interpolation. Default is
            ``PIL.Image.BILINEAR``
    """

    def __init__(self, size, interpolation=Image.BILINEAR):
        assert isinstance(size, int) or (isinstance(size, collections.Iterable) and len(size) == 2)
        self.size = size
        self.interpolation = interpolation

    def __call__(self, img):
        """
        Args:
            img (PIL Image): Image to be scaled.

        Returns:
            PIL Image: Rescaled image.
        """
        return F.resize(img, self.size, self.interpolation)

    def __repr__(self):
        interpolate_str = _pil_interpolation_to_str[self.interpolation]
        return self.__class__.__name__ + '(size={0}, interpolation={1})'.format(self.size, interpolate_str)
```

## ToTensor
把图片转换成张量。
在做数据归一化之前必须要把PIL Image转成Tensor，其它resize或crop操作不需要。
```python
class ToTensor(object):
    """Convert a "PIL Image"or"numpy.ndarray"to tensor.
       Convert a PIL image to tensor (H*W*C) in range [0,255] to a torch.Tensor(C*H*W) in the range [0.0,1.0]
    """

    def__call__(self,pic):
        """
        Args:
            pic(PIL Image or numpy.ndarray):Image to be converted to tensor.

        Returns:
            Tensor:Converted image.
        """
        return F.to_tensor(pic)

    def __repr__(self):
        return self.__class__.__name__+'()'
```
## ToPILImage
ToTensor的反向操作，把张量转换成PIL图片。
Convert a tensor or an ndarray to PIL Image

## Normalize ：Normalized an tensor image with mean and standard deviation
比如原来的tensor是三个维度的，则其作用就是先将输入归一化到(0,1)，再使用公式”(x-mean)/std”，将每个元素分布到(-1,1)
详细请见[我的另一篇博客](https://yuchen-ren.github.io/2019/10/29/torch_transforms-_normal/)

## CenterCrop
以输入图像img的中心作为中心点进行指定size的裁剪操作。
在数据增强中一般不会去使用该方法。因为当size固定时，对于同一张img，N次CenterCrop的结果是一样的。
size可以给单个int值，也可以给(int(size), int(size))
```python
class CenterCrop(object):
    """Crops the given PIL Image at the center.

    Args:
        size (sequence or int): Desired output size of the crop. If size is an
            int instead of sequence like (h, w), a square crop (size, size) is
            made.
    """

    def __init__(self, size):
        if isinstance(size, numbers.Number):
            self.size = (int(size), int(size))
        else:
            self.size = size

    def __call__(self, img):
        """
        Args:
            img (PIL Image): Image to be cropped.

        Returns:
            PIL Image: Cropped image.
        """
        return F.center_crop(img, self.size)

    def __repr__(self):
        return self.__class__.__name__ + '(size={0})'.format(self.size)
```
