# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # 头插法：双指针迭代
        # 如何反转链表 -> pre记录前一个节点，cur记录当前结点 
        # -> cur指向pre，向后迭代(原先cur后面结点断开，用临时变量temp记录)
        # 1.初始化双指针
        pre = None
        cur = head

        # 2.头插法
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        # 3.返回结果
        return pre