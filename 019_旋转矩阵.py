class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # 1.初始化4个方向
        res =[]
        m, n = len(matrix), len(matrix[0])
        top ,bottom = 0, m - 1
        left, right = 0, n - 1

        # 2.遍历
        while top <= bottom and left <= right:
            # 从左到右
            for j in range (left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # 从上到下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # 从右到左
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # 从下到上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        # 3.返回结果
        return res