# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        Alen = 0
        Blen = 0
        while A:
            Alen += 1
            A = A.next
        while B:
            Blen += 1
            B = B.next

        A = headA
        B = headB
        diff = 0
        if Alen < Blen:
            diff = Blen-Alen
            while diff > 0:
                B = B.next
                diff -= 1
        else:
            diff = Alen-Blen
            while diff > 0:
                A = A.next
                diff -= 1
        while A:
            if A == B:
                return A
            A = A.next
            B = B.next
        return None
        
        
        