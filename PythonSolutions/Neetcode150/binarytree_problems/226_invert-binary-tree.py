# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Post order traversal, pre order traversal also works
        def traverse(node):
            # Base case is when we hit a null node
            # Pop the recursion stack
            if node is None:
                return node
            
            # Traverse all the way to the left
            left = traverse(node.left)
            # Traverse all the way to the right after we hit a null node
            right = traverse(node.right)

            # Swap the nodes
            node.left = right
            node.right = left

            return node
        
        return traverse(root)