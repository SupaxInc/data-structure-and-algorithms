# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # When we reach end of subtrees and both values are None, then no issues were found
        # Which means the subtree is the same
        if not p and not q:
            return True
        
        # Fail 1: If a node still is available but other one is not
        # Fail 2: Values are not the same
        if not p or not q or p.val != q.val:
            return False
        
        # If both left and right subtrees are True then the tree is the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)