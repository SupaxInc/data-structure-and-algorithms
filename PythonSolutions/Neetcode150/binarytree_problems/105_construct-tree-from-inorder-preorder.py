# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NotOptimizedSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Grab the root node, 1st value in preorder array
        rootVal = preorder[0]
        root = TreeNode(rootVal) # Create a the new root node

        # Find the mid index of inorder
        # Left side of inorder gives us left sub tree
        # Right side gives us right sub tree
        mid = inorder.index(rootVal)

        # Create the left sub tree
        # Preorder: Grab the next root node for left sub tree, "mid+1" is needed as the end is exclusive in lists
        # Inorder: Get the nodes that will be all on the left of mid number
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # Create the right sub tree
        # Preorder: Grab the next root node for right sub tree, which are just all nodes to the right
        # Inorder: Get the nodes that will be all on the right of mid number
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class OptimizedSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build a hashmap to store value -> its index mappings for quick look-up
        index_map = {val: idx for idx, val in enumerate(inorder)}
        
        def arrayToTree(left, right):
            nonlocal preorder_index
            if left > right: return None
            
            # Select the preorder_index element as the root and increment it
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            
            preorder_index += 1
            
            # Build left and right subtree excluding root_val from inorder list
            root.left = arrayToTree(left, index_map[root_val] - 1)
            root.right = arrayToTree(index_map[root_val] + 1, right)
            
            return root
        
        preorder_index = 0
        return arrayToTree(0, len(inorder) - 1)
        