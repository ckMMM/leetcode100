# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         length1,length2 =0,0
#         cur1,cur2 = headA,headB
#         while(cur1!=None):
#             cur1 = cur1.next
#             length1+=1
#         while(cur2!=None):
#             cur2 = cur2.next
#             length2+=1
        
#         cur1,cur2 = headA,headB
#         if(length2>length1):
#             length1,length2=length2,length1
#             cur1,cur2 = cur2,cur1
#         gap = length1 - length2
#         while(gap!=0):
#             cur1=cur1.next
#             gap-=1
#         while(cur1!=None):
#             if(cur1==cur2):
#                 return cur1
#             else:
#                 cur1 = cur1.next
#                 cur2 = cur2.next
#         return None




class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # 双指针
        # 0.排除空
        if not headA or not headB:
            return None
        
        # 1.遍历
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        
        # 2.返回结果
        return pa

