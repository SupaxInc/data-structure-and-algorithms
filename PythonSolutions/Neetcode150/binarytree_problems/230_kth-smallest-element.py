# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RecursiveSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None
        def inorder(node):
            nonlocal count, result
            if not node:
                return
            
            inorder(node.left)
            count += 1
            if count == k:
                result = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return result
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class IterativeSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        count = 0
        stack = []
        curr = root
        while stack or curr:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            # Current should be none at this point
            curr = stack.pop()
            # Inorder case
            count += 1
            if curr and count == k:
                return curr.val
            # Visit left sub tree now go right
            curr = curr.right
