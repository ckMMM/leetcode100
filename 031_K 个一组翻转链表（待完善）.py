from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 统计节点个数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # last_tail 是上一组翻转后的尾节点
        last_tail = dummy = ListNode(next=head)

        # k 个一组处理
        while n >= k:
            n -= k

            pre = None
            cur = last_tail.next
            for _ in range(k):  # 同 92 题
                nxt = cur.next
                cur.next = pre  # 每次循环只修改一个 next，方便大家理解
                pre = cur
                cur = nxt

            # 请结合视频中的图理解
            # 翻转后：
            # pre 是当前组的头节点
            # cur 是下一组的起始节点
            # last_tail 是上一组的尾节点
            # last_tail.next 是当前组的尾节点
            tail = last_tail.next
            tail.next = cur  # 当前组的尾节点指向下一组的起始节点
            last_tail.next = pre  # 上一组的尾节点指向当前组的头节点
            last_tail = tail

        return dummy.next
    
#待理解实现
#作者：灵茶山艾府