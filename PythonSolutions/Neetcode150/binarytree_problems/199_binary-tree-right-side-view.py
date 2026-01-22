from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            n = len(queue)

            # Level order traversal
            for i in range(n):
                curr = queue.popleft()
                # In the current level, if we are at the last node add to result (gets right most value)
                if i == n - 1:
                    res.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
    
        return res