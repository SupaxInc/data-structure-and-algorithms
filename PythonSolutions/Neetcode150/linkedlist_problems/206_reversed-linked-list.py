from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        cur, prv = head, None

        while cur:
            # Create a temp pointer to the next node of the current node
            nxt = cur.next
            # The next node of the current node will point to the previous node e.g 1 -> 2 is now 1 -> None (pointing to new end)
            cur.next = prv
            # The previous node becomes the current node (the current node points to the previous node correctly making a reversal)
            prv = cur
            # The current node is able to grab the reference to the next node which wasn't reversed
            cur = nxt

        # Return the previous node as that is now the new head as it references the curr node last
            # The curr node points to temp which is the null end of the linked list
        return prv