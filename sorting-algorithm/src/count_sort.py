#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sort(arr, max):
    # 0-5共6个桶
    buckets = [0]*(max+1)
    # 统计每个桶应该有几个数
    for index in range(len(arr)):
        # 计数
        buckets[arr[index]] += 1
    
    # 累加
    for i in range(1, max + 1):
        buckets[i] = buckets[i] + buckets[i - 1]
    
    sortarr = [0]*len(arr)
    for data in reversed(arr):
        # 桶里存放的是data的个数，算出来的index为在排序后数组里的位置
        index = buckets[data] - 1
        sortarr[index] = data
        buckets[data] -= 1
    
    print(sortarr)


if __name__ == '__main__':
    arr = [2,5,3,0,2,3,0,3]
    sort(arr, 5)
