from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 每次与右上角比较 -> 每次排除一行或一列 -> 时间复杂度O(m + n)
        # 1.初始化开始位置
        startRow = 0
        startCol = len(matrix[0]) - 1

        # 2.循环比较
        while startRow < len(matrix) and startCol >= 0:
            if target > matrix[startRow][startCol]:
                startRow += 1
            elif target < matrix[startRow][startCol]:
                startCol -= 1
            else:
                return True
        
        # 3.没找到
        return False
        