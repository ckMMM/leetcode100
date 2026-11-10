class Solution1:
    def rotate(self, nums: list[int], k: int) -> None:
        # 切片
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        # 三步反转
        n = len(nums)
        k = k % n
        def reverse(i,j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)