# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # Get the initial group node (this would be the tail of the group during iteration)

        while True:
            # Step 1: Check if there are Kth nodes left to reverse
            kthNode = self.getKth(groupPrev, k)
            if not kthNode:
                break
            
            # Step 2: Grab pointers to setup for reversal
            groupNext = kthNode.next # Node of the next group
            curr = groupPrev.next    # Current node of the current group
            prev = groupNext         # First node of the next group

            # Step 3: Reverse k amount of current group
            for _ in range(k):
                nextTemp = curr.next 
                curr.next = prev
                prev = curr
                curr = nextTemp
            
            # At this point:
                # - current group is only connected to head of next group at the tail (first reversed node)
                # - prev node is at the end of the current group

            # Step 4: Connect prev group to the new reversed group and prep for possible next kth group
            oldGroupStart = groupPrev.next # Save reference of start of current group (non-reversed)
                                           # Remember start of non-reversed group is now the TAIL of reversed group
            groupPrev.next = prev          # Connect tail of previous group to tail of new reversed group
            groupPrev = oldGroupStart      # Prep the new tail of the current group to be used as prev group node

        return dummy.next
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr