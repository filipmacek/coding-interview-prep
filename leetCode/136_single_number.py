"""
---
title: Single number
number: 136
difficulty: easy
tags: ['Array','Bit Manipulation']
solved: true
---
"""


"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

"""
XOR bit manipulation, I had to lookup this problem. Hashmap was not accepted because of space complexity
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.simple(nums)


    def simple(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^num
        return res


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))

