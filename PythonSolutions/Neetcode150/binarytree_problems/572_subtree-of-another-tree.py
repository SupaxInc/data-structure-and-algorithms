# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the sub root is empty it means that its true b/c you can get an empty subtree of root
        if not subRoot:
            return True
        # First run: Empty root means we can't compare it with an existing subroot so theres no subtree of root
        # Recursive run: Propagate the False value when we couldn't find a subroot for root
        if not root:
            return False

        # Compare root and subRoot every traversal of root, allows us to use the same subRoot all the time
        if self.isSameTree(root, subRoot):
            return True
        
        # Checks to see if the subroot exists in the left or right sub trees
        # Continuously traverses through all the root nodes
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def isSameTree(self, node, subNode):
        # When we reach the end of the traversal (we're at leaf nodes) that means we had no issue comparing with subRoot
        if not node and not subNode:
            return True
        # Continously compare the root and subroot when the values and nodes are the same
        if node and subNode and node.val == subNode.val:
            return self.isSameTree(node.left, subNode.left) and self.isSameTree(node.right, subNode.right)
        
        # Propogate False value when the sub root compared with root is not the same tree
        return False
            
            
