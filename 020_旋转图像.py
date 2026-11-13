class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # 每轮以四个角为基准开始旋转
        # 1.初始化边界
        left = 0
        right = len(matrix) - 1

        # 2.旋转
        while left < right:
            top = left
            bottom = right
            for i in range(right - left):
                temp = matrix[top + i][left]
                matrix[top + i][left] = matrix[bottom][left + i]
                matrix[bottom][left + i] = matrix[bottom - i][right]
                matrix[bottom - i][right] = matrix[top][right - i]
                matrix[top][right - i] = temp
            right -= 1
            left += 1


class Solution1:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # 1. 主对角线翻转 (左下角与右上角对调)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. 左右翻转 (每一行反转)
        for i in range(n):
            matrix[i].reverse()