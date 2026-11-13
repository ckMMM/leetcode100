class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #双指针
        #1.定义结果变量，并对数组排序
        res = []
        nums.sort()

        #2.遍历数组
        for i in range(len(nums)-2):
            #3.元素与下一个元素相等，则进行下一次循环
            if i>0 and nums[i]==nums[i-1]:
                continue
            #4.判断三数和的最大值，最小值，避免无效循环
            if(nums[i] + nums[i+1] + nums[i+2] > 0):
                break
            if(nums[i] + nums[-2] + nums[-1] < 0):
                continue           
            #5.定义左右指针
            l = i+1
            r = len(nums)-1
            #6.计算三数之和，移动双指针，并去重复
            while(l<r):
                temp = nums[i] + nums[l] + nums[r]
                if temp > 0:
                    r-=1
                elif temp < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1

        #7.返回结果
        return res
