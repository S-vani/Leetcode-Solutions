# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        length = 1
        while curr.next is not None:
            curr = curr.next
            length += 1

        iterations = length - n
        if iterations == 0:
            head = head.next
            return head
            
        curr = head
        while iterations > 1:
            curr = curr.next
            iterations -= 1
        
        curr.next = curr.next.next
    
        return head
