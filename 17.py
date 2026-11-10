class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # 计算数组长度为n
        # 如何找最小的正数 -> 转为集合，依次判断[1,n]是否存在(需要O(n)空间)
        # 优化：将范围内的数移动到自己的下标位置，再依次判断[1,n]是否存在
        # 数num对应下标为num - 1
        n = len(nums)

        for i, num in enumerate(nums):
            while 1<= num <= n and num != nums[num - 1]:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
                num = nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 都存在，返回n + 1
        return n + 1