"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}

        def dfs(node):
            # Base case: If new node is already mapped, return the new node
                # Allows to connect the newly mapped node to the neighbor of a new node
            if node in oldToNew:
                return oldToNew[node]

            # Create a copy of old node with None neighbors
            copyNode = Node(node.val)
            # Map the old node to the new copy node
            oldToNew[node] = copyNode

            # Go through all neighbors of old node so that we can recursively copy 
                # the previously mapped nodes to neighbors of a newly copied node
            for neighbor in node.neighbors:
                copyNode.neighbors.append(dfs(neighbor))

            return copyNode
        
        dfs(node)
        # Return 1 of the newly mapped nodes
        return oldToNew[node]

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class BFSSolution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Map first node and queue it
        oldToNew = { node: Node(node.val) }
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            # Map all neighbors of current vertex
            for neighbor in curr.neighbors:
                # If neighbor is already mapped, then it means its neighbor's neighbors have been mapped already
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Map the current vertex's newly mapped neighbors
                oldToNew[curr].neighbors.append(oldToNew[neighbor])
        
        return oldToNew[node]