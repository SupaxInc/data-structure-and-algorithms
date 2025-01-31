# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathMaxSum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            # Comparing with 0 to prune the path with negative values
                # This prevents us from keeping negative paths after call stack pops
                # Essentially cutting the path short and possibly keeping only the root node
            leftPathSum = max(dfs(node.left), 0)
            rightPathSum = max(dfs(node.right), 0)

            self.pathMaxSum = max(node.val + leftPathSum + rightPathSum, self.pathMaxSum)

            # You can only keep the sum of the left or right sub tree
            # This helps create a straight path instead of a U path which is not allowed when call stack pops
            return node.val + max(leftPathSum, rightPathSum)
        
        dfs(root)
        return self.pathMaxSum