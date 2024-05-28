# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # Dummy node that points to head of list

        # prev is a pointer to the LAST node of the previous block of reversed k node groups.
        prev = dummy

        while True:
            # tail is used to traverse to the tail of the current k node groups
            tail = prev 

            ## Check if there are atleast 'k' nodes in the group
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next # Return the head of the current modified list
            
            # nex is the head of the next group of k nodes
            nex = tail.next

            # cur is the head of the group of k nodes we just traversed with the tail
            cur = prev.next # this is where we need to begin reversing
            # pre is what will be used as the new 'next' for cur when we are reversing
                # instead of pointing it to a null like in normal reverse linked lists without k groups
                # we need to point it to the head of next group of k nodes (nex)
            pre = nex 

            ## Begin reversing the group of k nodes starting from cur
            for _ in range(k):
                temp = cur.next # Temporarily store the next node so we can reverse it and still have reference
                cur.next = pre  # Reverse the cur nodes pointer
                pre = cur       # Move pre to the cur node as that will be used to be the new 'next'
                cur = temp      # Proceed to next node in the list for next iteration

            ## Connect the tail of the previous reversed group to the start of the just reversed group
            temp = prev.next # Head of the current group before reversal
            prev.next = pre  # Connect head of current group to the head of the just reversed group
            prev = temp      # Prev is now set as the tail of the just reversed group, ready for next iteration