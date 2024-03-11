class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxInPath):
            # Base case: If the node is None, return a count of 0 because we've reached beyond a leaf node.
            if not node:
                return 0
            
            count = 0  # Initialize count of good nodes seen so far to 0.
            
            # Check if the current node is a "good" node. A node is considered "good"
            if node.val >= maxInPath:
                count += 1

            # Update maxInPath for the path. This ensures that as we traverse deeper,
            # we carry forward the maximum value seen along this particular path.
            maxInPath = max(node.val, maxInPath)
            
            # Recursively call dfs for the left and right children, passing the updated maxInPath.
            # Accumulate the count of good nodes from both subtrees and add them to the current count.
            count += dfs(node.left, maxInPath)
            count += dfs(node.right, maxInPath)

            # Return the total count of good nodes found in the subtree rooted at this node.
            # This will propogate the accumulated count for both left and right subtrees
            # Even though count is initialized back to 0, it is accumulated as it propogates the value
            return count
        
        # Start the DFS traversal from the root, with the root's value as the initial maximum value seen on the path.
        return dfs(root, root.val)