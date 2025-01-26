# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: If one of the arrays are empty then we are at the end of the leaf nodes
        if not preorder or not inorder:
            return None

        # Root node is first value in preorder
        rootVal = preorder[0]
        rootNode = TreeNode(rootVal) # Create the root node so it can be rebuilt with subtrees

        # Find where the root node is in inorder to know where the left and right subtrees are
        mid = inorder.index(rootVal)

        # Since we now know where the left and right subtrees are we can build them out

        # Preorder: Grab the next root node for left sub tree, "mid+1" is needed as the end is exclusive in lists
        # Inorder: Get the nodes that will be all on the left of mid number
        rootNode.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Preorder: Grab the next root node for right sub tree, which are just all nodes to the right of left root node
        # Inorder: Get the nodes that will be all on the right of mid number
        rootNode.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return rootNode
        
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
        