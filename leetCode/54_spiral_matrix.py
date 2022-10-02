"""
---
title: Spiral matrix
number: 54
difficulty: medium
tags: ['Array','Matrix','Simulation']
solved: true
---
"""


"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List

"""

"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.simple(matrix)

    def simple(self,matrix:List[List[int]])-> List[int]:
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        result = []
        while left < right and top < bottom:
            # EDGE case matrix is has one column
            ## 4 sides
            for k in range(left,right):
                result.append(matrix[top][k])
            top+=1
            # right
            for k in range(top,bottom):
                result.append(matrix[k][right-1])
            right -=1
            if not (left < right and top < bottom):
                break
            for i in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                result.append(matrix[i][left])
            left+=1

        return result


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    test = [[7],[6],[9]]
    test1 = [[1],[2],[3]]
    print(Solution().spiralOrder(matrix))

