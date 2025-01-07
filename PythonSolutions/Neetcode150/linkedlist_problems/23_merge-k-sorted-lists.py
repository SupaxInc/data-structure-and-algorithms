# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class MinHeapSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        # Create a dummy node so we can reference it when we need to return new merged list
        currNode = dummyNode = ListNode()

        # Create the min heap with all first values of each linked lists
        for idx, node in enumerate(lists):
            if node:
                # Add the value as first index and the unique idx as the second index in the tuple
                    # The idx is important because heaps use the 1st value in a tuple to sort
                    # If the node value is the same as other values in the heap then it uses the next element
                    # In this case, idx will be the second element it will use to sort.
                    # If node is the next element, there would be an error as linked list nodes don't have a comparison method
                heapq.heappush(minHeap, (node.val, idx, node))
        
        # Each iteration the min heap will have the first values of all linked lists
            # We need to iterate until its all empty
        while minHeap:
            # Grab the smallest element in the min heap
            val, idx, newNode = heapq.heappop(minHeap)

            # Add the smallest node to the new merged list
            currNode.next = newNode
            # Traverse through the list so its ready for next iteration
            currNode = currNode.next

            # Check if the smallest node has a next available node
                # So we continue to exhaust all nodes for all linked lists
            if newNode.next:
                heapq.heappush(minHeap, (newNode.next.val, idx, newNode.next))
        
        # Return using the reference dummy node to the head of the merged list
        return dummyNode.next
    


class PairWiseSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # Continue merging until all pairs of lists are combined
        while len(lists) > 1:
            mergedLists = []

            # Combine 2 pairs each time by skipping 2 indices
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Check if a second list exists and its not out of bounds
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))

            # Replace the lists to the merged lists
            lists = mergedLists
        
        # Return the only list which is the full merged list
        return lists[0]
            
        
    
    def mergeLists(self, l1, l2):
        """Sort two lists and merge them"""
        current = dummy = ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            
            current = current.next
        
        current.next = l1 or l2

        return dummy.next