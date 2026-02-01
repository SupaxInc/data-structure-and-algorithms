
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

        def dfs(curr):
            # Base case: If node is already mapped, return the copied node
            if curr in oldToNew:
                return oldToNew[curr]
            
            copyNode = Node(curr.val) # Copy current node
            oldToNew[curr] = copyNode # Map current node to new copy

            # Go through all of neighbours for current node
            for nei in curr.neighbors:
                # Add the current nodes neighbors to the copied node
                copyNode.neighbors.append(dfs(nei))
            
            # Need to return copy node in the event base case is not hit for first time visits
            return copyNode
            
        return dfs(node)