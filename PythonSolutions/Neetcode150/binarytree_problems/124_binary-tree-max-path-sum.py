# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(node):
            nonlocal max_path_sum
            if not node:
                return 0
            
            # Calculate the left path and right path as deep as possible
                # Compare it with a 0 since we only want POSITIVE values
                # We are essentially pruning paths that are negative
            left_path = max(dfs(node.left), 0)
            right_path = max(dfs(node.right), 0)

            # Calculate the new path by adding the current node value and the paths
                # So if one path is 0, that means it was negative so we pruned it
                # We need to add current node since it becomes part of the path when it propogates up the tree
            new_path_sum = node.val + left_path + right_path

            # Compare if the new path is the maximum
            max_path_sum = max(max_path_sum, new_path_sum)

            # Return the current node value plus the max between the two paths and propogate this value to the parent node
                # We are creating a new path that does not include one of the paths
                # This is because we can't just go back and forth in a path it has to be a straight path
            return node.val + max(left_path, right_path)
        
        dfs(root)
        return max_path_sum
