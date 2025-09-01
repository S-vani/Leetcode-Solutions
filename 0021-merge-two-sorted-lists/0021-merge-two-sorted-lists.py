# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        empty_head = ListNode()
        tail = empty_head
        
        current1 = list1
        current2 = list2

        if current2 == None:
            return current1
        elif current1 == None:
            return current2


        while current1 is not None and current2 is not None:
            if current1.val <= current2.val:
                tail.next = current1
                current1 = current1.next
                tail = tail.next
            else:
                tail.next = current2
                current2 = current2.next
                tail = tail.next
        
        if current1 == None:
            while current2 is not None:
                tail.next = current2
                current2 = current2.next
                tail = tail.next
        
        elif current2 == None:
            while current1 is not None:
                tail.next = current1
                current1 = current1.next
                tail = tail.next
        
    
        return empty_head.next