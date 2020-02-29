---
layout:     post
title:      "算法题-自传数"
subtitle:   " c++实现"
date:       2020-2-29 17:00:00
author:     "TerryRen"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - algorithm
---
题目要求：
自传数（英语：Autobiographical number）为满足以下定义，不超过10位数的自然数[1]：第一位数（从左到右）是所有数位中“0”的个数第二位数是所有数位中“1”的个数第三位数是所有数位中“2”的个数…… 依此类推。例如1210第1至4位数分别为1、2、1和0，而此数字有1个0，2个1和1个2，恰好对应，因此1210为自传数，也是最小的自传数。

使用暴力遍历，code如下：


```c
#include<iostream>
using namespace std;

void test01()
{


	
	for (long long i = 1000; i<10000000000 ; i++)//不能是int
	{
		long long j = i;
		//cout <<"新的数"<< i << endl;
		int arr[10] = {};  //0-9的个数
		int dig[10] = {};  //存放每一位
		bool flag = true;//判断标志
		int bit = 0;//位数
		int digit = 9;
		while(j)
		{

			int n = j % 10;
			arr[n]++;
			dig[9 - bit] = n;
			//cout << n<<"   "<< arr[n] << endl;
			j/= 10;  //从个位开始循环判断各个位上数字
			bit++;
			//digit++;
		}
		//cout << bit << endl;
		while (bit && flag)
		{
			//cout << "dig[10-bit]" << dig[10 - bit] << endl;
			//cout << "arr[9 - digit]" << arr[9 - digit] << endl;
			if (dig[10-bit] != arr[9 - digit])
			{
				flag=false;
			}
			bit--;
			digit--;

			//cout << "循环+1" << endl;
		}
		//cout << "退出循环" << endl;
		if (flag)
		{
			cout << i << "是自传数" << endl;
		}
		/*if ((i > 100000000) ||(i<10))
		{
			cout << i << endl;
		}

		if (i == 0)
		{
			break;
		}*/
	}
}

int main()
{
	test01();
	system("pause");
	return 0;
}

```


* 注意 : 循环中的数需为long long,C++里int是4字节，最大2^31 -1 = 2147483647，到不了10个9，不然i累加到最大值会从0开始循环，得把int换成long long，long long是8字节。
