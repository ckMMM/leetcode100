from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 前后缀分解
        res = []
        n = len(nums)

        pre = [1] * n
        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i-1]

        sur = [1] * n
        for i in range(n-2, -1, -1):
            sur[i] = nums[i+1] * sur[i+1]

        for x,y in zip(pre,sur):
            res.append(x * y)

        return res