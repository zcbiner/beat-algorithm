#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sort(arr, max):
    
    for i in range(max):
        # 0-9共10个桶
        buckets = [-1]*10
        for j in range(len(arr)):
            data = arr[j]
            if i > 0:
                data = data // 10
            index = data % 10
            if buckets[index] == -1:
                buckets[index] = [arr[j]]
            else :
                buckets[index].append(arr[j])
        # 从桶里取出数据排序
        print(buckets)
        k = 0
        for j in range(len(buckets)):
            temp_list = buckets[j]
            if temp_list != -1:
                for l in range(len(temp_list)):
                    arr[k] = temp_list[l]
                    k += 1
        print(arr)

if __name__ == '__main__':
    arr = [26,3,49,556,81,9,863,0]
    sort(arr, 3)
