# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # 队列实现
        # 0.判断是否为空
        if root is None:
            return []
        # 1.初始化变量
        res = []
        q = deque([root])

        # 2.遍历
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        
        # 3.返回结果
        return res

        
class Solution1:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # 双数组实现
        # 0.判断是否为空
        if root is None:
            return []
        # 1.初始化变量
        res = []
        cur = [root]

        # 2.遍历
        while cur:
            nxt = []
            level = []
            for node in cur:
                level.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
            res.append(level)
        
        # 3.返回结果
        return res
