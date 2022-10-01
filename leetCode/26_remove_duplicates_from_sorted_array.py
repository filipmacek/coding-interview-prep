"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.



"""
from typing import List

"""
I think its two pointers problem we basically have sorted array and we must remove all element that are duplicating. THey are right from left index
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.simple(nums)

    def simple(self,nums:List[int])->int:
        left,right = 0,1
        while right < len(nums):
            if nums[left] == nums[right]:
                del nums[left]
            else:
                left+=1
                right+=1

        return len(nums)

if __name__ == '__main__':
    array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(array))

