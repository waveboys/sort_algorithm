#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/9/2 下午5:16
#@Author: guangliang
#@File  : quick_sort.py
"""
快速排序
思路:
1、从数列中挑选出一个元素，称为基准
2、重新排序数列，所有比基准值小的的元素放在基准值前面，比基准值大的元素放在基准值的后面，相同的数放在任一边。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区操作。
3、递归地把小于基准值的子数列和大于基准值的子数列分别排序。
复杂度分析：
时间复杂度：每次划分将数据选到基准值的两边，循环对两边的数据进行划分，类似于二分法。算法的整体性能取决于划分的平均程度，
即基准值的选择，基准值若是能把数据平均划分成两块，划分次数o(logn),每次划分比较一遍o(n),时间复杂度o(nlogn)
空间复杂度：额外空间开销出在暂存基准值,o(logn)次划分需要o(logn)个，空间复杂度为O(logn)
"""
# def quick_sort(arr:list):
#     if not arr:
#         return None
#     n = len(arr)
#     if n<=1:
#         return arr
#     def partition(arr,left,right):
#         """
#         完成分区操作，把大于基准值的放在基准值的右边，把小于基准值的放在基准值的左边
#         :param arr:
#         :param left:
#         :param right:
#         :return:
#         """
#         key = left
#         while left < right:
#             #如果列表后边的数比基准值大或者相等，则往前移动一位，直到找到比基准值小的数
#             while left < right and arr[key] <= arr[right]:
#                 right -= 1
#             # 如果列表前边的数比基准值小或者相等，则往后移动一位，直到找到比基准值大的数
#             while left < right and arr[key] >= arr[left]:
#                 left += 1
#             # 此时，在左边找到一个比基准值大的数和右边一个比基准值小的数，将这两个数交换。
#             # 如果没有找到这样的两个数据，则此时是两个相同的数据进行交换
#             (arr[left],arr[right]) = (arr[right],arr[left])
#         # 当从两边分别逼近，直到两个位置相等时结束，将左边的同基准值进行交换
#         (arr[left],arr[key]) = (arr[key],arr[left])
#         return left
#
#     def quicksort(arr,left,right):
#         if left >= right:
#             return
#         # 从基准开始分析
#         mid = partition(arr,left,right)
#         # 对基准值左边的部分进行排序
#         quicksort(arr,left,mid-1)
#         # 对基准值右边的部分进行排序
#         quicksort(arr,mid+1,right)
#
#     quicksort(arr,0,n-1)
#     return arr
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
nums=[25,19,91,32,6,86,54,103,58,45,102]

print(quick_sort(nums))
