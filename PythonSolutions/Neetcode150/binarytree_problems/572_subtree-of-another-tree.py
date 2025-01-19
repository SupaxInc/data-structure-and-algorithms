# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case 1: If subroot is None then we can always find that subroot in any root
        if not subRoot:
            return True

        # Base case 2: If we ended up traversing to a None root, then that means we couldn't find the subRoot
        if not root:
            return False
        
        # Each recursion, check if a root equals the subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # Check if either the right or left subtree contains the subroot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p, q):
        # If we traversed to both subtrees as empty then that means the tree is the same
        if not p and not q:
            return True
        
        # Fail 1: If a node still is available but other one is not
        # Fail 2: Values are not the same
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)