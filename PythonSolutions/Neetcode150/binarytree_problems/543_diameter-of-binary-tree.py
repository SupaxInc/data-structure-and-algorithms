# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            # When the stack pops for each left and right sub tree
            # We can add the max depth of both sub trees to get the max diameter
            maxDiameter = max(maxDiameter, left + right) 

            # Return the max depth of the current subtree including current root level
            # Adds a 1 to add for the height of the current node continously
            return 1 + max(left, right)  
        
        dfs(root)
        return maxDiameter