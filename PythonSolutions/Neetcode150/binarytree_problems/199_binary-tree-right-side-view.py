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

        queue = deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            for i in range(queueLength):
                curr = queue.popleft()
                # If its at the last node in the level, add to result
                # This is so that the last node cof each level can only be seen
                if i == queueLength -1:
                    res.append(curr.val)
    
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return res