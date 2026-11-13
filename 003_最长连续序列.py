class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 如何找数字连续序列的起始元素x -> x-1不在列表中 -> 使用集合判断
        # 1.使用集合
        st = set(nums)
        res = 0

        # 2.遍历找起始位置
        for num in nums:
            if num - 1 in st:
                continue

            end = num + 1
            while end in st:
                end += 1
            res = max(res, end - num)
            if res * 2 >= len(nums):
                break

        # 3.返回结果
        return res