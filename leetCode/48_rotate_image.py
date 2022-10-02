"""
---
title: Rotate image
number: 48
difficulty: medium
tags: ['Array','Math','Matrix']
solved: true
---
"""


"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

"""
from typing import List

"""
Normal rotation of elements start at exterior then go to the middle/interior
We will have floor(n/2) of this iterations

"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.simple(matrix)

    def simple(self,matrix:List[List[int]]):
        # ROWS,COLUMNS = len(matrix),len(matrix[0]) // squared matrix
        left,right = 0,len(matrix)-1
        while left < right:
            top = left
            bottom = right
            for index in range(right-left):
                saved = matrix[top][left+index]
                matrix[top][left+index] = matrix[bottom-index][left]
                matrix[bottom-index][left] = matrix[bottom][right-index]
                matrix[bottom][right-index] = matrix[top+index][right]
                matrix[top+index][right]=saved
            left+=1
            right-=1
        return matrix




if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result =  [[7,4,1],[8,5,2],[9,6,3]]
    my = Solution().rotate(matrix)
    print(my)
