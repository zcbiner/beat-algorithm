#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ISort import ISort

class MergeSort(ISort):
    
    def sort(self, arr):
        left = 0
        right = len(arr) - 1
        self.mergeSort(arr, left, right)
    
    # 将数组从中间分为两部分，然后合并
    def mergeSort(self, arr, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

    # 合并两个数组，合并时要注意排序
    def merge(self, arr, left, mid, right):
        mergeNum = []
        start = left
        end = mid + 1
        while start <= mid and end <= right:
            if arr[start] <= arr[end]:
                mergeNum.append(arr[start])
                start += 1
            else:
                mergeNum.append(arr[end])
                end += 1
        
        while start <= mid:
            mergeNum.append(arr[start])
            start += 1
        while end <= right:
            mergeNum.append(arr[end])
            end += 1
        
        # 将辅助数组的数据拷贝回原数组
        start = left
        while start <= right:
            arr[start] = mergeNum[start - left]
            start += 1