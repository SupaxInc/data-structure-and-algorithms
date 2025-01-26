# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NonOptimizedSolution:
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
        inorderIdxMap = { val: idx for idx, val in enumerate(inorder) }
        self.preorderIndex = 0

        # Left idx and right idx is the range of the inorder array index
        def createTree(leftIdx, rightIdx):
            # Base case: When left slice gets bigger than right slice of inorder then were at end of leaf node
            if leftIdx > rightIdx:
                return None

            # Root node is first value in preorder
            rootVal = preorder[self.preorderIndex]
            rootNode = TreeNode(rootVal)

            # Increase preorder index used for next function call
            self.preorderIndex += 1

            # Find mid index in inorder to delinneate between left and right subtrees
            mid = inorderIdxMap[rootVal]

            # Build the left and right subtrees using inorder splicing

            # Slice left side of mid index for left subtree
            rootNode.left = createTree(leftIdx, mid - 1)

            # Slice right side of mid index for right subtree
            rootNode.right = createTree(mid + 1, rightIdx)

            return rootNode
        
        return createTree(0, len(inorder) - 1)
        