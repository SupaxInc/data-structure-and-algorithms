# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            # Find a deeper ancestor on the right since the LCA can be found in deeper subtrees 
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Find a deeper ancestor on the left
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # 1: Could mean p, q nodes are on diff subtrees so we can't go deeper thus making current node the ancestor
                # 2: Could mean the values equal to the current value so the deepest ancestor is current node we are on
                    # The LCA could be a descendant of itself. 
                return curr
        
        return None