"""
---
title: Majority Element
number: 169
difficulty: easy
tags: ['Array','Hash Table','Divide and Conquer','Sorting','Counting']
url: https://leetcode.com/problems/majority-element/
solved: true
---
"""
from typing import List

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.simple(nums)

    def simple(self,nums: List[int]):
        ## Solution with hash map is easy
        ## Lets try to figure out with O(1) space
        # This is some algorithm
        res,count = 0,0
        for num in nums:
            if count == 0:
                res = num
            count+= (1 if num == res else -1)
        return res


if __name__ == '__main__':
    nums = [3,2,3]
    nums1 =  [2,2,1,1,1,2,2]
    print(Solution().majorityElement(nums))
