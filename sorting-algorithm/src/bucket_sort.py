#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sort(arr):
    # 将数据分到5个桶中
    buckets = [[],[],[],[],[]]
    for index in range(len(arr)):
        bucket_no = arr[index] // 10
        buckets[bucket_no].append(arr[index])
    
    # 桶内数据排序
    for index in range(len(buckets)):
        buckets[index].sort()
        print(buckets[index])

if __name__ == '__main__':
    arr = [1,7,8,24,19,46,26,38,33,12,42,20,6,35]
    sort(arr)
