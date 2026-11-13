# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #快慢指针
        #1.创建虚拟头结点，并将其连接到原链表头部
        dummy = ListNode(0,head)

        #2.初始化快慢指针，均指向虚拟头结点
        fast = slow = dummy

        #3.快指针先走 n 步
        for _ in range(n):
            fast = fast.next

        #4.快慢指针同时移动，直到快指针到达最后一个结点
        while fast.next:
            slow = slow.next
            fast = fast.next

        #5.此时 slow 指向倒数第 n 个结点的前驱结点，执行删除操作
        slow.next = slow.next.next

        #6.返回虚拟头结点的下一个结点，即新链表的头结点
        return dummy.next
