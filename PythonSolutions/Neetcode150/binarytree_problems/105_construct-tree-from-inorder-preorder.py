# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NotOptimizedSolution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If one of the arrays are empty then we have hit the end of the tree
        if not preorder or not inorder:
            return None
        
        # Grab the root node, 1st value in preorder array
        rootVal = preorder[0]
        root = TreeNode(rootVal)

        # Find the mid index of inorder
        # Left side of inorder gives us left sub tree
        # Right side gives us right sub tree
        mid = inorder.index(rootVal)

        # Create the left sub tree
        # Preorder: Grab the next root node for left sub tree, "mid+1" is needed as the end is exclusive in lists
            # It'll use the mid index from inorder to slice 
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
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = 0
        
        # Left and right is the range of the inorder array index
            # We are essentially slicing the inorder array
            # Inorder is what we really need to to know which nodes are on the left or right
        def arrayToTree(left, right):
            nonlocal preorder_index
            # When we end up going pass the range, then we reached end of tree
            if left > right: return None
            
            # Select the preorder_index element as the root and increment it
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            
            # Increment preorder index since we just need the next index as root for next recurse
            preorder_index += 1
            
            # Slice the inorder array from current left to new right
                # Grabbing just the left side of the inorder array
            root.left = arrayToTree(left, inorder_index_map[root_val] - 1)
            # Slice the inorder array from new left to current right
                # Grabs just the right side of the inorder array
            root.right = arrayToTree(inorder_index_map[root_val] + 1, right)
            
            return root
        
        return arrayToTree(0, len(inorder) - 1)
        