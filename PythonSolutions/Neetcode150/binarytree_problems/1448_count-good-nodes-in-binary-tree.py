# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0

        # Preorder traversal
        def dfs(node, maxInPath):
            if not node:
                return maxInPath
            
            # Assign the next greater value along the path of DFS
            if node.val >= maxInPath:
                self.count += 1
                maxInPath = node.val
            
            # Pass the current maxInPath (or new maxInPath) along left and right subtrees
            dfs(node.left, maxInPath)
            dfs(node.right, maxInPath)

            # After left and right subtree traversal propagate the CURRENT maxInPath NOT from subtrees
            return maxInPath
        
        dfs(root, float("-inf"))
        return self.count