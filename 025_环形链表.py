# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 类比操场跑路，跑到快的人总会多跑一圈和跑到慢的人相遇
        # 快慢指针:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True

        return False
        