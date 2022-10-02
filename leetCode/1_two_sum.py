"""
---
title: Two sum
number: 1
difficulty: easy
tags: ['Array','Hash Table']
solved: true
---
"""


'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.best(nums,target)

    def best(self,nums,target):
        hashmap = {}
        for index,value in enumerate(nums):
            res = target-value
            if res in hashmap:
                return [index,hashmap[res]]
            hashmap[value] = index
        return [-1,-1]

    def hash_map(self,nums,target):
        # 85ms
        hashmap = {}
        # Create hashmap
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hashmap:
                if i != hashmap[res]:
                    return [i,hashmap[res]]
        print("sta sad")

    def brute_force(self,nums,target):
        # Lets try with simple
        # 6583 ms
        sum = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    return [i,j]
                sum = 0



if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    # [0,1]
    print(Solution().twoSum(nums, target))
    nums = [3,2,4]
    target = 6
    # [1,2]
    print(Solution().twoSum(nums,target))
