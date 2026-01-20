# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        # Traverse down the tree (BST) normally without DFS/BFS
        while curr:
            # If both values are smaller than current val then go left
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # If both values are larger than current val then go right
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # Once we split off, it means we found LCA:
                # 1. Both target nodes are in opposite subtrees under current node
                # 2. OR the target node is current node itself AND the other node is in a subtree below
            else:
                return curr
