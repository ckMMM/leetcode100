# Definition for a binary tree node.
from typing import List, Optional


# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 递归实现
        # 中序遍历
        res = []
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代实现
        # 1.初始化栈，结果列表，当前节点
        res = []
        stack = []
        cur = root

        # 2.遍历
        while cur or stack:
            # 左结点入栈与放入结果列表
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)

            # 转向右子树
            cur = cur.right
        
        # 3.返回结果列表
        return res
