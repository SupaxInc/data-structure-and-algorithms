# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float("-Inf"), high=float("Inf")):
            # True if we hit a null value since we didn't find any issues with range
            if not node:
                return True
            
            # Check if current node is within correct range
            if not (low < node.val < high):
                return False
            
            # Going left -> change high
            # Going right -> change low
            # Checks if left and right subtrees are valid
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )
        
        return validate(root)