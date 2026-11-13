# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 1.定义相等二叉树的方法(此题适当修改为镜像)
    def isSameTree(self, p, q):
        # 为空判断
        if p is None or q is None:
            return p is q
        # 子问题：左右子树节点值相等
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.isSameTree(root.left, root.right)

        