"""
---
title: Container with most master
number: 11
difficulty: medium
tags: ['Array','Two Pointers','Greedy']
url: https://leetcode.com/problems/container-with-most-water/
solved: true
---
"""
from typing import List

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.simple(height)
    def simple(self,heights: List[int])->int:
        left = 0
        right = len(heights)-1
        maxVolume = 0
        while left <= right:
            x = right - left
            y = min(heights[left],heights[right])
            maxVolume = max(maxVolume,x*y)
            if heights[left]> heights[right]:
                right-=1
            else:
                left +=1

        return maxVolume


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    test = [1,2,1]
    test1 = [2,3,4,5,18,17,6]
    print(Solution().maxArea(test))
