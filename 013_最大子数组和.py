class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Kadane算法：今天的决策取决于之前的结果和今天的表现，而之前的结果就是最优子问题
        # 1.定义今天的决策和最大值
        cur = max_sum = nums[0]

        # 2.更新
        for num in nums[1:]:
            cur = max((cur + num),num)
            if cur > max_sum:
                max_sum = cur

        # 3.返回结果
        return max_sum