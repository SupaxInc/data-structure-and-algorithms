from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MoreReadableSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # Edge case: Left pointer must begin at dummy pointer so it ends just BEFORE the Nth node
        left, right = dummy, head
        
        # Move right pointer Nth times so that it gives enough between space for left pointer to be BEFORE Nth node
        for _ in range(n):
            right = right.next

        # Move left and right pointer same amount
        while right:
            left = left.next
            right = right.next

        # Connect the left pointer 2 nodes head, thus removing Nth node
        left.next = left.next.next

        # Returns the head we referenced
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # * Edge case: * 
        # Without a dummy node, we wont have a pointer of the previous node from the target
        # Our slow pointer would end up on the target and we wont be able to remove target node
        dummy = ListNode(0, head)

        slow = dummy # Slow pointer starts at dummy node, this is so we don't end up on the target node
        fast = head # Fast pointer starts at head

        # Move fast pointer nth times so we know Nth from end
        for _ in range(0, n):
            fast = fast.next
        
        # Move both pointers 1 step at a time until fast pointer hits end
        while fast:
            slow = slow.next
            fast = fast.next

        # Slow is now at the previous node of the target since it started at the dummy node
        # We can point the next of the previous node to the node in front of target node
        # This effectively removes the target node
        slow.next = slow.next.next

        # Return the next of the dummy to get the list from original head
            # This is because from the start we referenced slow to the dummy node
            # Since we removed the target node from slow pointer, dummy will reference the slow list
        return dummy.next
        #* Returning head here will be wrong since we don't use the fast pointer to remove the target node but use the slow pointer *
        