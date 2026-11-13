# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 直径 = 左子树深度 + 右子树深度
        # 1.定义结果变量
        res = 0

        # 2.dfs:最大深度
        def depth(root):
            if root == None:
                return 0
            left = depth(root.left)
            right = depth(root.right)

            nonlocal res  
            res = max(res, left + right)
            
            return max(left, right) + 1
        
        # 3.调用并返回结果变量
        depth(root)
        return res
        