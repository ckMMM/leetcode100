from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #1.定义结果列表和单调队列
        res = []
        q = deque()

        #2.遍历数组放入和移出单调队列
        for i,num in enumerate(nums):
            #入（放入队尾）
            while q and num > q[-1]:
                q.pop()
            q.append(num)

            #出（移出队首）
            if i >= k and nums[i-k] == q[0]:
                q.popleft()
            
            #更新（长度为k时开始放入最大值）
            if i >= k - 1:
                res.append(q[0])
        
        #3.返回结果列表
        return res