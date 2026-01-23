from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        # Inorder traversal gives us numbers in order in a BST
        def inorderDFS(node):
            if not node:
                return -1

            leftVal = inorderDFS(node.left)
            # At some point when we travel to left subtree, it'll return the actual value
            # during the inorder traversal
            if leftVal != -1:
                return leftVal 

            self.count += 1
            # Hitting Kth, just return current node value and propagate it up the tree
            if self.count == k:
                return node.val
            
            # During in order traversal of right subtree, the Kth may be hit
            rightVal = inorderDFS(node.right)
            if rightVal != -1:
                return rightVal

            # Return -1 if we don't find anything after traversing through all subtrees
            return -1
        
        return inorderDFS(root)
            
