from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 如何找出0移动到末尾 -> 将非0元素移动到新数组
        # 因为题目要求原地对数组进行操作
        # 所以可以采用双指针，左指针定位到0则不移动
        # 1.定义左指针i
        i = 0

        # 2.遍历数组
        for j in range(len(nums)):
            if nums[j]:
                nums[i] = nums[j]
                i += 1

        # 3.末尾补0
        nums[i:] = [0] * (len(nums) - i)
