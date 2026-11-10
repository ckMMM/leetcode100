from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 + 哈希
        # 任一子数组nums[i:j] = nums[:j] - nums[:i-1]
        # 默认所有前缀和计数为0，前缀和为0的计数为1
        # 1.初始化前缀和，哈希表，结果变量
        res = 0
        pre = 0
        d = defaultdict(int)
        d[0] = 1

        # 2.遍历
        for num in nums:
            pre += num
            # 判断有无满足条件的前缀和
            if (pre - k) in d:
                res += d[pre - k]
            d[pre] += 1
        
        # 3.返回结果
        return res

        