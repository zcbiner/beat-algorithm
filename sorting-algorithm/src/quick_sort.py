#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ISort import ISort

class QuickSort(ISort):
    
    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        k = self.partition(arr, left, right)
        self.quickSort(arr, left, k - 1)
        self.quickSort(arr, k + 1, right)

    def partition(self, arr, left, right):
        # 默认取第一个元素为基准
        point = arr[left]
        while left < right:
            while right > left and arr[right] >= point:
                right -= 1
            arr[right], arr[left] = arr[left], arr[right]

            while right > left and arr[left] <= point:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        return left
        
