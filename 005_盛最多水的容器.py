class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 如何能容纳最多的水 -> 长度和高度尽可能大
        # 长度：可以从最大n - 1开始取
        # 短板效应：一只木桶能装多少水取决于最短的那块木板，而非最长的木板。
        # 高度：由更短的那边决定，因此长度变化时，舍弃短板
        # 1.定义双指针
        i = 0
        j = len(height) - 1

        # 2.寻找最大值
        res = 0
        while i < j:
            temp = (j - i) * min(height[i], height[j])
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            res = max(res, temp)

        # 3.返回结果
        return res
