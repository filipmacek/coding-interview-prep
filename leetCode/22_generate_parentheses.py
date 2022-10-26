"""
---
title: Generate parentheses
number: 22
difficulty: medium
tags: ['String','Dynamic programming','Backtracking']
url: https://leetcode.com/problems/generate-parentheses/
solved: true
---
"""
from typing import List

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.simple(n)
    def simple(self,n:int):
        # We could use the stack and count number of open and closed parenthesis
        results = []
        stack = []
        def backtrack(openNum:int,closedNum:int):
            if openNum == closedNum == n:
                results.append("".join(stack))
            if openNum < n:
                stack.append("(")
                backtrack(openNum+1,closedNum)
                stack.pop()
            if closedNum < openNum:
                stack.append(")")
                backtrack(openNum,closedNum+1)
                stack.pop()



        backtrack(0,0)
        return results


if __name__ == '__main__':
    n = 2
    print(Solution().generateParenthesis(n))
