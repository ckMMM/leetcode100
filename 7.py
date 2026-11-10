class Solution:
    def trap(self, height: list[int]) -> int:
        #前后缀最大值
        #以示例图为例，想象将水全变为黑色方块
        #此时：高度为3的柱子左边，每个柱子高度和其左边最大高度（含自己）一致
        #同理：高度为3的柱子右边，每个柱子高度和其右边最大高度一致
        #水的面积 = min(前缀填充后柱子高度,后缀填充后柱子高度) - 原高度

        # 1.定义左右指针
        n = len(height)
        l = 0
        r = n - 1

        # 2.创建前缀最大值数组
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1,n):
            pre_max[i] = max(height[i],pre_max[i-1])

        # 3.创建后缀最大值数组
        sur_max = [0] * n
        sur_max[-1] = height[-1]
        for i in range(n-2,-1,-1):
            sur_max[i] = max(height[i],sur_max[i+1])

        # 4.返回计算结果
        res = 0
        for h,pre,sur in zip(height,pre_max,sur_max):
            res += min(pre,sur) - h
        return res

        