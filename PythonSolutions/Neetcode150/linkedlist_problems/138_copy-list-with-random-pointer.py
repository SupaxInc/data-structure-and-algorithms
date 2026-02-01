from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head
        
        # * Without an old to new node hash map, we could end up pointing to a random node that does not exist yet. *
        oldToNew = {}

        curr = head
        # Traverse through head and create a dict of the nodes (old -> new)
        while curr:
            # Does not map new node's random or next ptr yet
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        #  Traverse through head again, now all new nodes are mapped
        while curr:
            # Map new node's random ptr using oldToNew map
            if curr.next:
                oldToNew[curr].next = oldToNew[curr.next]

            if curr.random:
                oldToNew[curr].random = oldToNew[curr.random]
            
            
            curr = curr.next