from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class MoreReadableSolution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.maxLength = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Re-calculate max length by comparing current max length and the longest paths from left to right
                # Longest path betweeen nodes will always be left + right as it maximizes finding the longest
            self.maxLength = max(self.maxLength, left + right)

            # Return 1 (to add the edge) and longest path of EITHER left or right
                # Gives us current largest path from this root of the tree
            return 1 + max(left, right)
        
        dfs(root)
        return self.maxLength
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node):
            # Use non local to use variables from the parent scope
            nonlocal maxDiameter
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # The diameter of a binary tree is the longest path between any two nodes
            # This path does NOT need to pass through the root
            
            # For each node, we calculate two things:
            # 1. Diameter: left + right
            #    - This is the path going through the current node
            #    - We don't add +1 here because we're counting EDGES not NODES
            #    - Example: For path 4->2->5, diameter = 2 edges, not 3 nodes
            #
            # 2. Height: 1 + max(left, right) 
            #    - This is returned to parent nodes for their calculations
            #    - We add +1 here because we're counting the edge to the current node
            #    - Example: At node 2 with children 4,5: height = 1 + max(1,1) = 2 edges
            
            # We use postorder traversal to ensure we have both heights
            # before calculating diameter at each node
            maxDiameter = max(maxDiameter, left + right) 

            # Return the max depth of the current subtree including current root level
            # Adds a 1 to add for the height of the current node continously
            return 1 + max(left, right)  
        
        dfs(root)
        return maxDiameter