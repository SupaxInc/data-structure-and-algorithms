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
                # For example: 1 -> 2 -> 3
                    # Create new copy node for 1, traverse to 2, 2 has neighbors 1 and 3
                    # From 2, we traverse to 1 first and see that it already has a copy node so it hits base case
                    # Connect copy node 1 to neighbor of 2, traverse to 3 now
                    # From 3, we traverse back to 2 since its a neighbor and see it already has a copy node so it hits base case
                    # Connect copy node 2 to neighbor of 3, etc etc
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

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

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
        # Prevents null errors when mapping the first node
        if not node:
            return None
        
        # Map first node and queue it
        oldToNew = { node: Node(node.val) }
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            # Map all neighbors of current old vertex to copied nodes
            for neighbor in curr.neighbors:
                # If neighbor is already mapped, then it means its neighbor's neighbors have been mapped already
                # If it hasn't been mapped then create a new copy of it
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor) # Append the old node so its own neighbors can be processed later
                
                # Map the current vertex's copy to newly copied mapped neighbor
                    # Essentially creating a new copy connection for the current copied node
                oldToNew[curr].neighbors.append(oldToNew[neighbor])
        
        # Return the first node since it connects to all other nodes
        return oldToNew[node]