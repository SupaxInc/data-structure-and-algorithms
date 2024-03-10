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
            # If both nodes are greater than the current root node then move to the right
            # We need to find a DEEPER common ancestor
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Vice-versa
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # 1) The nodes could be in split in different subtrees, so can't find deeper common ancestors
                # 2) The curr node can equal the same as one of the nodes
                    # A node can be its own descendant, so it would be the LCA
                return curr
