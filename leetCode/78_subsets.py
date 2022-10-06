"""
---
title: Subsets
number: 78
difficulty: medium
tags: ['Array','Backtracking','Bit Manipulation']
url: https://leetcode.com/problems/subsets/
solved: true
---
"""
from typing import List

"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 """

### Backtracking - recursive


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def recursive(index: int):
            print("sa")
            if index >= len(nums):
                res.append(subset.copy())
                return
            # include current item
            subset.append(nums[index])
            recursive(index+1)
            # not include current item
            subset.pop()
            recursive(index+1)
        recursive(0)
        return res





if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))
