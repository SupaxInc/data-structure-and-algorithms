from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode()

        carry = 0

        # Carry is needed as a condition in the while since theres an edge case where both lists are empty
            # Carry may still have a value of 1 when both lists are empty
        while l1 or l2 or carry:
            # If theres a carry number, add to total
            total = carry
            
            # Add the two numbers and traverse them for next iteration
            # *Long addition is done here from left to right rather than right to left due to direction of linked list*
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            # Checks if we have to carry any values to next nodes (if total for current column is > 9), e.g. 16 // 10 = 1.6 = 1 
            carry = total // 10
            # Change total using remainder
                # Grabs the remainder which is the 2nd digit of total for current column, e.g. 19 % 10 = 9 
            total = total % 10
            
            current.next = ListNode(total)
            current = current.next
        
        # Return using the reference as we have traversed current node to end of list
        return dummy.next
            