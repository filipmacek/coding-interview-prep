import math
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.simple(nums,target)

    def binary_search(self,nums:List[int],target:int):
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if target < nums[middle]:
                right = middle-1
            elif target > nums[middle]:
                left = middle+1
            else:
                return middle
        return left



    def simple(self,nums:List[int],target:int):
        "easy with you know it O(n) probably need binary search becase its sorted"
        # hashmap = {item:index for (index,item) in enumerate(nums)}
        # if target in hashmap:
        #     return hashmap[target]
        # else:
        # I Dont need hashmap, this is normal binary search
        return self.binary_search(nums,target)



if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    print(Solution().searchInsert(nums,target))
