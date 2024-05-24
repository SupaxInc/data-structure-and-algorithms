# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class BetterReadableSolution:
    def reorderList(self, head) -> ListNode:
        if not head or not head.next:
            return
        # Ask if there are constraints (can we maybe just change the values?)
        # PSEUDO CODE
        # find midway point -
        # slow and fast pointer
        # second = slow.next
        # slow.next = None

        # Reverse second list -
        # currnode, prevnode = second, None 
        # temp = curr.next
        # curr.next = prevnode
        # prevnode = curr
        # curr = temp

        # merge two lists - 
        # first, second = head, prev
        # 1 -> 2 -> 3 , 5 -> 4
        # 1 -> 5 -> 2 -> 4 -> 3

        # Find mid point of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Create second list using mid point
        second = slow.next
        # Point the memory on mid point of head to None so it no longer points to new second list
        slow.next = None 

        # Reverse second list
        currNode, prevNode = second, None
        while currNode:
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode # prevNode is now the second list
            currNode = temp
        
        # Merge two lists
        # 1 -> 2 -> 3 , 5 -> 4
        # 1 -> 5 -> 2 -> 4 -> 3
        first, second = head, prevNode # Grab the lists
        while second:
            temp1, temp2 = first.next, second.next # Get temp nodes for next nodes
            first.next = second # First list points to the second list
            second.next = temp1 # Second list points to the next value of first list, creates a 1 -> 5 -> 2
            # The lists will now be the temp nodes ready for next iteration
                # This is because we were able to connect the next nodes
                # Therefore, we traverse to the next nodes and are able to grab the next nodes again in next iteration
            first, second = temp1, temp2 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head) -> ListNode:
        currNode, prevNode = head, None

        while currNode:
            temp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = temp

        return prevNode
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the mid point of the linked list using a fast and slow pointer
        # Slow pointer will be the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Need to go up 1 to get the second half of the list using mid point
        second = slow.next 
        slow.next = None # Terminate second half

        # Reverse the second half
        second = self.reverseList(second)

        # Merge the first half and the second per second node
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


        