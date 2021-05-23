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

# 优化：减少元素交换。  
class QuickSort1(ISort):

    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        k = self.partition(arr, left, right)
        self.quickSort(arr, left, k - 1)
        self.quickSort(arr, k + 1, right)

    def partition(self, arr, left, right):
        # 默认取第一个元素为基准(注意这里记录的是基准的索引)
        point = left
        while left < right:
            while right > left and arr[right] >= arr[point]:
                right -= 1

            while right > left and arr[left] <= arr[point]:
                left += 1
            
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        # 此时left=right，并且是基准值的合适位置，将基准值赋予arr[left]
        arr[left], arr[point] = arr[point], arr[left]
        return left

import random

# 优化：随机选取基准值。 
class QuickSort2(ISort):

    def sort(self, arr):
        self.quickSort(arr, 0, len(arr) - 1)
    
    def quickSort(self, arr, left, right):
        if left >= right:
            return
        k = self.partition(arr, left, right)
        self.quickSort(arr, left, k - 1)
        self.quickSort(arr, k + 1, right)

    def partition(self, arr, left, right):
        # 随机选取基准值
        randInt = random.randint(left, right)
        # 将选取的基准值与left交换
        arr[left], arr[randInt] = arr[randInt], arr[left]
        # 交换完后，基准值还是left
        point = left
        while left < right:
            while right > left and arr[right] >= arr[point]:
                right -= 1

            while right > left and arr[left] <= arr[point]:
                left += 1
            
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
        # 此时left=right，并且是基准值的合适位置，将基准值赋予arr[left]
        arr[left], arr[point] = arr[point], arr[left]
        return left