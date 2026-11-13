# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1.快慢指针找中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2.反转后半部分
        pre = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        # 3.前后比较
        left, right = head, pre
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        # 4.返回结果
        return True

if __name__ == '__main__':
    # 测试用例
    # 1.创建链表
    l = [1,2,3,2,1]
    head = ListNode()
    temp = head
    for num in l:
        node = ListNode(num)
        temp.next = node
        temp = temp.next

    # 2.调用函数
    res = Solution().isPalindrome(head.next)
    print(res)