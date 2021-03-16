#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        out = []
        for i, value in enumerate(nums):
            while dq and nums[dq[-1]] < value:
                dq.pop()
            dq += i,
            if dq[0] == i - k:
                dq.popleft()
            if  i >= k - 1:
                out += nums[dq[0]],
        return out
# @lc code=end