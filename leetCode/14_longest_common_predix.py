"""
---
title: Longest Common Prefix
number: 14
difficulty: easy
tags: ['String']
url: https://leetcode.com/problems/longest-common-prefix/
solved: true
---
"""
from typing import List

"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.simple(strs)
    def simple(self,list:List[str]):
        minLen = min([len(item) for item in list])
        counter = 0
        ch = None
        for index in range(minLen):
            ch = list[0][index]
            haveAllSameChar  = all([item[index] == ch for item in list])
            if haveAllSameChar:
                counter +=1
            else:
                break
        return list[0][0:counter]




if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
