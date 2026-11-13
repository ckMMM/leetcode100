# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归dfs
        # 1.边界条件
        if root == None:
            return
        
        # 2.子问题：交换左右子节点
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left ,root.right = root.right, root.left
        return root

if __name__ == '__main__':
    # 测试用例
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    s = Solution()
    print(s.invertTree(root))
