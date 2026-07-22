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
        while B is not None or A is not None:
            if A is not None:
                A = A.next
                Alen += 1
            if B is not None:
                B = B.next
                Blen += 1
        A = headA
        B = headB
        diff = Alen-Blen if Alen>Blen else Blen-Alen
        if Alen < Blen:
            while diff > 0:
                B = B.next
                diff -= 1
        else:
            while diff > 0:
                A = A.next
                diff -= 1
        while A is not None:
            if A == B:
                return A
            A = A.next
            B = B.next
        return None
        
        
        