"""
---
title: Longest valid parentheses
number: 32
difficulty: hard
tags: ['String','Dynamic Programming','Stack']
url: https://leetcode.com/problems/longest-valid-parentheses/
solved: true
---
"""


OPENED = "("
CLOSED = ")"

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.simple_indexes(s)

    def simple_indexes(self,string:str):
        # we push indexes on stack instead of parentheses
        stack = []
        maxLen = 0
        for i in range(len(string)):
            char = string[i]
            if len(stack)==0 and char == CLOSED:
                stack.append(i)
            elif len(stack) >0 and char == CLOSED and string[stack[len(stack)-1]] == OPENED:
                stack.pop()
            else:
                stack.append(i)
            if len(stack) == 1:
                maxLen = max(maxLen,stack[0])
            elif len(stack)>1:
                maxLen = max(maxLen,stack[len(stack)-1]-stack[len(stack)-2]-1)
        stack.append(len(string))
        maxLen = stack[0] if len(stack) == 1 else max(maxLen, stack[len(stack) - 1] - stack[len(stack) - 2] - 1)
        return maxLen


    def simple_test(self,string:str):
        stack = []
        maxLen = 0
        currentLen = 0
        tempLen = 0

        for i in range(len(string)):
            char = string[i]
            if len(stack) == 0 and char is CLOSED:
                stack.append(i)
            elif len(stack) > 0  and stack[len(stack)-1] == OPENED and char == CLOSED:
                tempLen +=2
                stack.pop()
                if len(stack) == 0:
                    currentLen += tempLen
                    tempLen = 0
            elif len(stack)>0 and stack[len(stack)-1] == CLOSED and char == OPENED:
                stack.pop()
                stack.append(i)
                tempLen = 0
                currentLen = 0
            else:
                if char == OPENED:
                    stack.append(string[i])
                else:
                    ## there is closed bracket
                    currentLen = 0
            maxLen = max(maxLen,tempLen)
        return maxLen


if __name__ == '__main__':
    test1 = "()(()()(()(()"
    test2 = '(()(()())'
    test3 = "()"
    print(Solution().longestValidParentheses(test3))
