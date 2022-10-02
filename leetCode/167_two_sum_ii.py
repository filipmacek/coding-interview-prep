"""
---
title: Two Sum II - Input Array Is Sorted
number: 167
difficulty: medium
tags: ['Array','Two Pointers','Binary Search']
solved: true
---
"""


"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

"""

### two pointers - sorted array and sum is target

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.simple(numbers,target)

    def simple(self,numbers:List[int],target:int)->List[int]:
        # Two pointer - right could be next to left or at the end, depends on problem
        # Here its right at the end and we are shifting it to the left
        left,right = 0,len(numbers)-1
        while left < len(numbers):
            sum = numbers[left]+numbers[right]
            if sum < target:
                left +=1
            elif sum > target:
                right -=1
            elif sum == target:
                break

        return [left+1,right+1]


if __name__ == '__main__':
    numbers = [3, 24, 50, 79, 88, 150, 345]
    target = 200
    print(Solution().twoSum( numbers,target))
