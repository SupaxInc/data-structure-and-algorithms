# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # When it reaches the end of the subtrees, both should be a None
            # Since it hasn't hit the False base cases, this means the sub trees are the same
            if not p and not q:
                return True
            # False base cases
            if not p or not q or p.val != q.val:
                return False
            
            # Traverses all of the left and right leaf nodes
            # Then propagates the value to the parent node
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p, q)
            