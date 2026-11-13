# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # 三指针迭代
        # 1.虚拟头节点
        dummy = pre = ListNode(0,head)

        # 2.遍历，存在两个节点才交换
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next

            # 步骤1: first指向后续链表
            first.next = second.next
            #步骤2: second指向first
            second.next = first
            #步骤3: 前驱节点指向second
            pre.next = second

            # 下一轮交换
            pre = first
        
        # 3.返回结果
        return dummy.next