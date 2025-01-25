# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RecursiveSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Keep track of count
        # We can't pass it in the parameters since the count will be recursively called during in-order
        self.count = 0 

        def inorder(node):
            # Base case 1: Hit the end leaf node
            if not node:
                return None
            
            # Receives either None or the value of kth smallest element
            leftVal = inorder(node.left)
            # Propagate value up if value was found
            if leftVal is not None:
                return leftVal
            
            self.count += 1
            if self.count == k:
                return node.val
            
            rightVal = inorder(node.right)
            if rightVal is not None:
                return rightVal
            
            # Return a None if kth smallest element was found
            return None
        
        return inorder(root)
            

            

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
                # So we pop the stack, in which is no longer None 
                # Since we now have a new node from the stack
            curr = stack.pop()
            # Inorder case
            count += 1
            if count == k:
                return curr.val
            # Visited left sub tree now go right
            curr = curr.right
