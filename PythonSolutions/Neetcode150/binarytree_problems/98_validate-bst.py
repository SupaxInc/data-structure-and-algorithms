from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # Preorder traversal, uses params to know lowest and highest in current path
        def validate(node, low, high):
            if not node:
                return True
            
            # Fail if current node is not in the range of lowest and highest in path
            if not (low < node.val < high):
                return False
            
            # Going left -> Pass current node value as new high
            # Going right -> Pass current node value as new low
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Lowest and highest in the currernt path at the beginning are infinites
        return validate(root, float("-inf"), float("inf"))