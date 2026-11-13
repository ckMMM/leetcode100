from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #哈希表
        #1.定义哈希表，key为元素值，value为数组下标
        dict1 = {}

        #2.遍历数组
        for index,item in enumerate(nums):
            #3.判断哈希表中有无符合要求的另一个数
            if (target-item) in dict1:
                return [index,dict1[target-item]]
            #4.没有则加入哈希表
            else:
                dict1[item] = index

        #5.未找到返回[]
        return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
    