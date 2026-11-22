# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        num1 = 0
        num2 = 0
        i = 1
        while curr1 or curr2:
            if curr1:
                num1 += curr1.val * i
                curr1 = curr1.next
            if curr2:
                num2 += curr2.val * i
                curr2 = curr2.next
            i *= 10
        total = num1+num2
        new_node = ListNode(total%10)
        curr3 = new_node
        total = total // 10
        while total != 0:
            node = ListNode(total%10)
            total = total // 10
            curr3.next = node
            curr3 = curr3.next

        
        return new_node
