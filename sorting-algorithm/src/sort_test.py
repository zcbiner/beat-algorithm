#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 排序算法的测试
from bubble_sort import BubbleSort
from insert_sort import InsertSort
from select_sort import SelectSort
from merge_sort import MergeSort
from quick_sort import QuickSort

# 判断数组是否排序正确
def checkSort(nums):
    size = len(nums)
    if size <= 1:
        return True
    
    for i in range(1, size):
        if nums[i] < nums[i-1]:
            return False
    return True

# 构造测试数据
def getTestData():
    testList = []
    nums0 = [0]
    testList.append(nums0)
    nums1 = [2, 1]
    testList.append(nums1)
    nums2 = [1,2]
    testList.append(nums2)
    nums3 = [1,2,3]
    testList.append(nums3)
    nums4 = [9,8,7,6,5,4,3,2,1]
    testList.append(nums4)
    nums5 = [34,32,89,45,2,0,4,66,18,40,5,53,23]
    testList.append(nums5)
    nums6 = [5,6,32,7,55,1,99,100,345,678,321,0,32,12,34]
    testList.append(nums6)
    return testList

# 通用测试函数
def testSort(iSort, testList):
    isAc = True
    for index, nums in enumerate(testList):
        iSort.sort(nums)
        print(nums)
        if not checkSort(nums):
            isAc = False
            break
    info = type(iSort).__name__ + (' success' if isAc else ' failed')
    print(info)

def testBubbleSort(testList):
    testSort(BubbleSort(), testList)

def testInsertSort(testList):
    testSort(InsertSort(), testList)

def testSelectSort(testList):
    testSort(SelectSort(), testList)

def testMergeSort(testList):
    testSort(MergeSort(), testList)

def testQuickSort(testList):
    testSort(QuickSort(), testList)

if __name__ == '__main__':
    # testBubbleSort(getTestData())
    # testInsertSort(getTestData())
    # testSelectSort(getTestData())
    # testMergeSort(getTestData())
    testQuickSort(getTestData())
