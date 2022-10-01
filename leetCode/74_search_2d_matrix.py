"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

"""
from typing import List

"""
 So sorted means binary search, but both columns and rows are sorted, so its double binary search.
 First determine target row by binary search then determine right column
 !! Be careful about edge cases in only one colum or row
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## Search target row
        left,right = 0,len(matrix)-1
        ROWS,COLUMNS = len(matrix)-1,len(matrix[0])-1
        TARGET_ROW = 0
        if ROWS == 0:
            TARGET_ROW = 0
        else:
            ## IF LEFT IS RIGHT, WE FOUND OUR ROW, so < not <=
            while left < right:
                middle = (left+right)//2
                value_min = matrix[middle][0]
                value_max = matrix[middle][COLUMNS]
                if target < value_min:
                    right = middle -1
                elif target > value_max:
                    left = middle+1
                else:
                    # We have target row break from loop, we be careful with setting target row to left
                    TARGET_ROW = middle
                    break
            if left >=right:
                # Only if we break naturally from  loop
                TARGET_ROW = left
        ## Search target columns
        left,right = 0,len(matrix[0])-1
        while left <=right:
            middle = (left+right)//2
            value = matrix[TARGET_ROW][middle]
            if target < value:
                right = middle-1
            elif target > value:
                left = middle+1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    matrix1=[[1],[3]]
    target = 10
    print(Solution().searchMatrix(matrix,target))
