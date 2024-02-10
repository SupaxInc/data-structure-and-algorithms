# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            # Once an imbalance is detected no further work is necessary
            # Propogate up the call stack to return -1
            if left == -1: return -1
            right = dfs(node.right)
            # Propogate up the call stack to return -1
            if right == -1: return -1
        
            # Detect if there an imbalance of levels between left and right subtree
            # If the max depth difference between the two is greater than 1 than theres an imbalance
            # This is because if theres more than 2 edges versus 1 edge that would be an imbalance of height
            # (e.g. 3-1 = 2 (unbalanced), 2-1 = 1 (balanced))
            if abs(left-right) > 1:
                return -1
            
            # Get the max depth for the current subtree
            return 1 + max(left, right)
        
        return dfs(root) != -1
