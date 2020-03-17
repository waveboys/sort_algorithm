#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/17 下午2:20
#@Author: guangliang
#@File  : buble_sort.py
"""
冒泡排序算法步骤：
1、比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3、针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，完成一轮迭代，一轮迭代之后，当前最大的元素就排到了最后，迭代n(元素个数)轮之后，就形成了从小到大的排序。

时间复杂度分析：
冒泡排序对n个数操作n-1轮，每轮找出最大值或最小值，
每轮操作n-1次，因此时间复杂度为o(n^2)
因为数据交换时需要交换空间，因此空间复杂度为o(1)
"""
def buble_sort(arr:list)->list:
    if not arr:
        return None
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(buble_sort([1,3,2,6,4,8,9,6]))