# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 如何合并 -> 定义一个新结点，依次比较放入
        # 1.构建哨兵结点
        dummy = cur = ListNode()

        # 2.依次比较放入
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        # 3放入剩下未比较部分
        cur.next = list1 or list2
        return dummy.next