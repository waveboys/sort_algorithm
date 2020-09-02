#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/2 下午8:26
#@Author: guangliang
#@File  : select_sort.py
"""
选择排序：
每一轮选出最小的值或者最大值，共进行n-1轮
初始状态：无序区为R[1..n]，有序区为空；
第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
n-1趟结束，数组有序化了。
每轮操作O(n)次，共O（n）轮，时间复杂度O(n^2)。

额外空间开销出在交换数据时那一个过渡空间，空间复杂度O(1)
"""
def select_sort(arr:list):
    if not arr:
        return None
    n = len(arr)
    if n<=1:
        return arr
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):       # 每一轮选出最小的值进行交换
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            (arr[i],arr[min_index]) = (arr[min_index],arr[i])
    return arr
print(select_sort([1,3,2,4,6,5,8,7,0,9]))