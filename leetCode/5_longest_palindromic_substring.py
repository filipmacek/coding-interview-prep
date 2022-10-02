"""
---
title: Longest Palindromic Substring
number: 5
difficulty: medium
tags: ['String','Dynamic Programming']
solved: true
---
"""


"""Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.
"""

"""
- First write function that checks if given string is palindromic
- The is have fixed substring chuck, and scan through string
- Start at length of string then lower the substring length until you find palindromic substring
- edge cases: one words

Interesting case je string aaaaaaaaaaa...bc..aaaaaaaaaaa where bc substring is the middle,so my inital implementation has to go 
through 1000-> 500 lengths scans to get this.
So brute force not good.
Let implement palindrome check by expending from center
Also I think there could be another approach with longest common substring

"""


class Solution:
    ## ->
    def longestPalindrome(self, s: str) -> str:
        return self.check_with_longest_common_substring(s)

    def simple(self,s:str):
        ### This solution is working for short string but
        ### for long string I get time limit error
        length = len(s) - 1
        while length >= 0:
            for index in range(len(s) - length):
                target = s[index:(index + length + 1)]
                if self.is_palindrome(target):
                    return target
            length -= 1
        return None

    def check_with_longest_common_substring(self,string:str):
        ## Not working
        reversed_string = "".join(reversed(string))
        print("sta")
        maxLen = len(string)
        while maxLen >0:
            for i in range(len(string)-maxLen+1):
                sub = string[i:(i+maxLen)]
                if sub in reversed_string:
                    return sub
            maxLen-=1




    def check_with_expanding(self,s:str):
        # working
        result = ""
        resLen = 0

        for i in range(len(s)):
            ## odd length
            left,right = i,i
            while left >=0 and right <len(s) and s[left] ==s[right]:
                if right-left+1 > resLen:
                    result = s[left:right+1]
                    resLen = right-left
                left -=1
                right +=1
            # even length
            left,right = i,i+1
            while left >=0 and right <len(s) and s[left] ==s[right]:
                if right-left+1 > resLen:
                    result = s[left:right+1]
                    resLen = right-left
                left -=1
                right +=1
        return result



    def is_palindrome(self,string:str):
        for index in range(len(string)):
            if string[index]  != string[(len(string)-index-1)]:
                return False
        return True


if __name__ == '__main__':
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    string1 = "abbac"
    res = Solution().longestPalindrome(string1)
    print(res)
