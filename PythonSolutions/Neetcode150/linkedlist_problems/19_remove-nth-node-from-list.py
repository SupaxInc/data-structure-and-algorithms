# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Without a dummy node, we wont have a pointer of the previous node from the target
        # Our slow pointer would end up on the target and we wont be able to remove target node
        dummy = ListNode(0, head)
        slow = dummy # Slow pointer starts at dummy node, this is so we don't end up on the target node
        fast = head # Fast pointer starts at head

        # Move fast pointer nth times so we know Nth from end
        for _ in range(0, n):
            fast = fast.next
        
        # Move both pointers just once until we find the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Since we're now at the previous node of the target
        # We can point the next of the previous node to the node in front of target node
        # This effectively remvoes the target node
        slow.next = slow.next.next

        # Return the next of the dummy to get the list from original head
        return dummy.next
        