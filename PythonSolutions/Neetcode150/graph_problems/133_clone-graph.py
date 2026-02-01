
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}

        def dfs(node):
            # Base case: If the node has already been mapped to a new node, then return new node
            if node in oldToNew:
                return oldToNew[node]
            
            # Visit the node
            copyNode = Node(node.val) # Copy the node so it can be mapped
            oldToNew[node] = copyNode # Map the old node to the newly copied node

            # Explore the other neighbors of the old node so they can be copied too
            for nei in node.neighbors:
                copyNode.neighbors.append(dfs(nei))
            
            # Returns the copied node when the recursive traversal of neighbors finishes so that it can be appended in the previous recursion call
            # Eventually the last in the call stack would be the "root" node
            return copyNode
        
        return dfs(node)