#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/2 下午6:27
#@Author: guangliang
#@File  : insert_sort.py
"""
插入排序：
插入排序默认前面的数据都排好顺序了，然后从后往前依次比较，直到找到合适的位置插入
1、从第一个元素开始，该元素可以被认为是排好序的
2、取出下一个元素，在已经排好顺序的数列中依次从后往前扫描
3、如果该元素(已排序)大于新元素，将该元素移到下一个位置
4、重复步骤3，直到找到小于或者等于新元素的位置
5、将新元素插入该位置。
"""
def insert_sort(arr:list):
    if not arr:
        return None
    n = len(arr)
    if n<=1:
        return arr
    for i in range(1,n):
        j = i
        target = arr[j]
        while j>0 and target < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = target
    return arr


print(insert_sort([4,3,5,1,6,7,8]))