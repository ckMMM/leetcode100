# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #快慢指针
        #1.定义快慢指针从头结点开始
        fast = slow = head

        #2.快慢指针同步移动，先判断有无环
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

            #3.有环则使用新的双指针确定环的入口
            if(fast == slow):
                temp = head
                while(temp!=slow):
                    temp = temp.next
                    slow = slow.next
                return slow

        #4.无环放回None
        return None
