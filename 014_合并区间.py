class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # 思路：按左边界排序后，比较遍历到的左区间与res末尾元素的右区间
        # 1.排序
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]

        # 2.遍历
        for item in intervals[1:]:
            # 小则合并
            if item[0] <= res[-1][1]:
                res[-1][1] = max(item[1],res[-1][1])
            else:
                res.append(item)
                
        # 3.返回结果
        return res
        