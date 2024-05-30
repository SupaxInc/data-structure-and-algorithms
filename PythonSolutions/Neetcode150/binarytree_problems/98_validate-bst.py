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
            
            # The highest and lowest values changes as we move left or right so we need a way to keep track of it
            # Going left -> change high value as the current node value
                # Allows us to compare the next nodes range with the newest highest value
            # Going right -> change low value as the current node value
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root)