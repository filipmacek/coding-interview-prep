"""
---
title: Valid parentheses
number: 20
difficulty: easy
tags: ['String','Stack']
solved: true
---
"""


"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

ROUND_BRACKETS = ['(',')']
SQUARE_BRACKETS = ['[',"]"]
CURLY_BRACKETS = ['{','}']

class Solution:
    def isValid(self, s: str) -> bool:
        return self.efficient(s)

    def efficient(self,string:str):
        stack = []
        closed = {
            ")":"(","]":'[',"}":'{'
        }
        for char in string:
            if char in closed:
                if stack and stack[-1] == closed[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False

    def simple(self,string:str):
        types = {
            "(": 0,")":0,
            "[":1,"]":1,
            "{":2,"}":2
        }
        valid = {
            "(": ")",
            "[":"]",
            "{": "}"
        }
        stack = []
        for item in string:
            if len(stack) == 0:
                stack.append(item)
            else:
                last_elem = stack[len(stack)-1]
                last_type = types[last_elem]
                current_type = types[item]
                if last_type != current_type:
                    stack.append(item)
                else:
                    if item == last_elem:
                        stack.append(item)
                    elif last_elem in valid and valid[last_elem] == item:
                        stack.pop()
                    else:
                        stack.append(item)
        if len(stack) ==0:
            return True
        else:
            return False




if __name__ == '__main__':
    test = "()]["
    print(Solution().isValid(test))

