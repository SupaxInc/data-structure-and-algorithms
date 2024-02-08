from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BFSSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level = 0

        # We might accidentally add a None node
        if root:
            queue.append(root)

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