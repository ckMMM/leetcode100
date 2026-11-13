# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        # 递归
        def build(l, r):
            # 边界条件
            if l > r:
                return None
            
            # 子问题：中间值为根
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)

            return node
        root = build(0, len(nums) - 1)
        return root
        