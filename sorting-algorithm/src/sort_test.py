# 排序算法的测试
from bubble_sort import BubbleSort


def test_bubble_sort(nums):
    BubbleSort().bubble_sort(nums)
    print(nums)

if __name__ == '__main__':
    nums1 = [9,8,7,6,5,4,3,2,1]
    nums2 = [34,32,89,45,2,0,4,66,18,40,5,53,23]
    nums3 = [5,6,32,7,55,1,99,100,345,678,321,0,32,12,34]

    test_bubble_sort(nums1)
    test_bubble_sort(nums2)
    test_bubble_sort(nums3)
