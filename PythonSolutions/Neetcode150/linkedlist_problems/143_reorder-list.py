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


        