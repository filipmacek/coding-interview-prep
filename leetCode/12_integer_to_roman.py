"""
---
title: Integer to Roman
number: 12
difficulty: medium
tags: ['Hash table','Math','String']
url: https://leetcode.com/problems/integer-to-roman/
solved: false
---
"""

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

"""


class Solution:
    def intToRoman(self, num: int) -> str:
        return self.simple(num)
    def simple(self,num:int):
        iter = num
        result = ""
        while iter>0:
            if iter >1000:
                pass
            elif iter >100:
                pass
            elif iter >10:
                digit = iter //10



    def get_left_digit(self,num:int):
        while num >=10:
            num = num//10
        return num


if __name__ == '__main__':
    num = 58
    print(Solution().intToRoman(num))
