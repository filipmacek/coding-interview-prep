"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

"""
from typing import List

"""
Largest sum contiguous subarray - Kadane's algorithm
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.simple(nums)
    def simple(self,nums:List[int]):
        max_sum = nums[0]
        current_sum = 0
        for number in nums:
            if current_sum <0:
                current_sum = 0
            current_sum+=number
            max_sum = max(max_sum,current_sum)
        return max_sum






if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))

