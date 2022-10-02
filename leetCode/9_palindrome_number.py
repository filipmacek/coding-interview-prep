"""
---
title: Palindrome number
number: 9
difficulty: easy
tags: ['Math']
solved: true
---
"""


"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

"""
import math

"""
As far as I see converting number to string then checking is most naive approach
and its working. But lets try to think about how to check if we only work with number (without converting to string)
 -   be careful for edge cases
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return self.only_number(x)

    def only_number(self,x):
        # Edge cases
        # 1: Negative number are not palindrome
        # 2. number that end in zero and have at least two digits cannot be palindrome
        # 3. one digit numbers are palindrome
        if x<0:return False
        if x<=9: return True
        if x %10 == 0 :return False

        ## We need to get one by one number ( hint: modulus)
        reverted = 0
        temp = x
        half = self.slice_at_half_prefix(num=x)
        while reverted < half:
            # get last digit
            num = temp % 10
            reverted = reverted*10+num
            # use floor division to remove last digit
            temp = temp//10
        return reverted == half

    def slice_at_half_prefix(self,num):
        num_digits = len(str(num))
        return int(num //10**(num_digits/2))

    def simple(self,x):
        # Most naive first implementation
        chr_list = [item for item in str(x)]
        chr_list_reversed = list(reversed(chr_list))
        for index,value in enumerate(chr_list):
            if value != chr_list_reversed[index]:
                return False
        return True

    def simple_one_list(self,x):
        ## lets try use only one list
        chr_list = [item for item in str(x)]
        for index in range(len(chr_list)):
            if chr_list[index] != chr_list[len(chr_list)-index-1]:
                return False
        return True


if __name__ == '__main__':
    input = 0
    print(Solution().isPalindrome(input))

