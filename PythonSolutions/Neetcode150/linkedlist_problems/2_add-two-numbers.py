# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode()

        # Carry helps add an extra node of 1 when the end of list has a carry
        carry = 0

        while l1 or l2 or carry:
            # If theres a carry number, add ot total
            total = carry
            
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            # Checks if we have to carry any values to next nodes
            carry = total // 10
            # Grabs the remainder which is the 2nd digit, e.g 19 % 10 = 9 
            total = total % 10
            
            current.next = ListNode(total)
            current = current.next
        
        return dummy.next
            