from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        queue = deque([root])
        level = 0

        # Adding a while here will help iterate through the nodes in the next level
        # Allows to re-calculate the len(queue) code in the for loop
        while queue:
            # The code len(queue) is only executed at the START of the for loop
            # Therefore, adding to the queue does not change the range of the for loop
            # This helps only iterate through the current level of the tree
            for i in range(len(queue)):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            level += 1
        
        return level
    
class DFSSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # Traverse as deep as possible to left and right
            # Then get the max of depth between left and right
            # Finally, add 1 to include the current root node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))