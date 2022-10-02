"""
---
title: Longest Substring without repeating characters
number: 3
difficulty: medium
tags: ['Hash table','String','Sliding window']
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
solved: true
---
"""

"""Given a string s, find the length of the longest substring without repeating characters."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        left = 0
        maxLen = 0
        for i in range(len(s)):
            # Shift left
            while s[i] in result:
                result.remove(s[left])
                left+=1
            result.add(s[i])
            maxLen = max(maxLen,i-left+1)
        return maxLen



if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
