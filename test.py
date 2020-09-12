#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/8 上午11:23
#@Author: guangliang
#@File  : test.py
def quick_sort(nums):
    def partition(nums,left,right):
        key=left
        while left < right:
            while nums[right] >=  nums[key] and left<right:
                right -= 1
            while nums[left] <=  nums[key] and left < right:
                left += 1
            nums[left],nums[right] = nums[right],nums[left]
        nums[key],nums[left] = nums[left],nums[key]
        return left
    def quicksort(nums,left,right):
        if left>=right:
            return
        mid = partition(nums, left, right)
        quicksort(nums, left, mid)
        quicksort(nums, mid+1, right)
    quicksort(nums,0,len(nums)-1)
    return nums


while True:
    try:
        a = int(input())
        s = set()
        for i in range(a):
            num = int(input())
            s.add(num)
        s = quick_sort(list(s))
        # s=sorted(s)
        for i in s:
            print(i)
    except:
    #     print(Exception)
        break
