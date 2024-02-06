# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # Goes through the first iteration
        slow, fast = head, head.next

        while fast and fast.next:
            # Check if there's a cycle for the beginning of each iteration
            if slow == fast:
                return True

            slow = slow.next
            # Fast node goes twice as fast as the slow node
            fast = fast.next.next
        
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False