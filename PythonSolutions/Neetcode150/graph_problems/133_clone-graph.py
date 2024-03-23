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