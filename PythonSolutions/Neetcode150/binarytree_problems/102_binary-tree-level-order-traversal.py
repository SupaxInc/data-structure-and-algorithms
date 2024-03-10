# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level = []
            # Traverse through the entire level before moving to next
            # Without a for loop, we would end up looking through next level
            for _ in range(len(queue)):
                curr = queue.popleft() # FIFO
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level)
        
        return result