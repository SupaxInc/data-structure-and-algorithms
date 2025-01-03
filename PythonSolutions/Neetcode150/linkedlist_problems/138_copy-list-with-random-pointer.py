"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # * Without an old to new node hash map, we could end up pointing to a random node that does not exist yet. *
        oldToNew = {}
        
        current = head
        # 1st iteration: Create a map of the old node to the new node (only the value of new node)
        while current:
            oldToNew[current] = Node(current.val)
            current = current.next
        
        # 2nd iteration: Start adding next and random pointers to the new node
            # This allows us to actually map random pointers as previously it could point to non-existing nodes
        current = head
        while current:
            # Begin mapping the new nodes for both the next and random pointer
            if current.next:
                # Map the next node of new node to the mapped new next node
                oldToNew[current].next = oldToNew[current.next]
            if current.random:
                # Map the random node of new node to the mapped new random node
                # Previously, without a map, we could point to a random node that does not exist yet
                oldToNew[current].random = oldToNew[current.random]
            current = current.next
        
        # Return the NEW head node (remember it points the old nodes to the new nodes)
        return oldToNew[head]
        