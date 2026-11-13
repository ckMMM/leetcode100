# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归实现
        # 1.边界
        if root == None:
            return 0 
        
        # 2.子问题:整棵树最大深度 = max(左子树最大深度，右子树最大深度) + 1
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        return max(l_depth, r_depth) + 1
        