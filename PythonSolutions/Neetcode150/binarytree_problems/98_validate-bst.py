# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float("-Inf"), high=float("Inf")):
            # Base case 1: No more nodes to traverse to, therefore, no issues finding ranges
            if not node:
                return True
            
            # Base case 2: Check if current node value is in the correct range
            if not (low < node.val < high):
                return False
            
            # Going left -> Pass current node value as new high
                # Since all values to the left of the node should be lower than the ancestor (current node)
            # Going right -> Pass current node value as new low
                # Since all values to the right of the node should be higher than the ancestor (current node)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root)