# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # * Reference a variable to a dummy node since we will be traversing using the dummy node *
            # This way we can have a reference to the head of the dummy node that is traversing and creating a new list
        mergedList = dummy = ListNode()

        # Connect the lists till 1 of them are empty
        while list1 and list2:
            # Connect the nodes depending on value
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            # Traverse to the next node we just connected to (either new list1 or list2 node)
            dummy = dummy.next

        # Since there might still be a non-empty list, connect the next ndoe to the rest of that non-empty list
        dummy.next = list1 or list2

        # Since merged list references dummy node at the beginning we can still grab the head of the dummy node
            # using merged list even though the dummy variable has traversed to the tail end already
        return mergedList.next
