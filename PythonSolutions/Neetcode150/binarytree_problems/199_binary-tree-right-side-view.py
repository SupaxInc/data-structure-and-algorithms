# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        queue = deque([root])

        while queue:
            queueLength = len(queue)
            # The for loop will only check the the nodes for the current level
                # This is because queue length stays the same and does not change within the for loop
                # It gets recalculate when for loop is done
            for i in range(queueLength):
                curr = queue.popleft()
                # If its at the last node in the level, add to result
                if i == queueLength - 1:
                    res.append(curr.val)
    
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return res