from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 两数相加 -> 依次相加，用carry记录进位
        # 1.初始化哨兵结点
        dummy = cur = ListNode()
        carry = 0

        # 2.各位置相加
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry = carry//10
        
        # 3.若还有进位则直接加上
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next

        