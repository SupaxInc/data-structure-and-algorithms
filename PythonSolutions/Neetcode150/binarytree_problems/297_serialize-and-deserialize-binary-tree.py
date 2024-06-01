# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        values = []

        # Preorder traversal as it processes the root node first helps when reconstructing the tree
        def dfs(root):
            if not root:
                values.append("N")
                return values
            
            values.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return values
        
        # Serialize the tree as a string separated with a comma delimiter
        return ','.join(dfs(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Create an iterable object of an array of the each node value
        values = iter(data.split(','))

        # Use preorder traversal to re-construct the tree
        def dfs():
            # Iterate through the next item in the iterable object
            rootVal = next(values)

            # Connect a null if the root val is an N
            if rootVal == "N":
                return None
            
            # Create the new root node with the iterated root value
            rootNode = TreeNode(rootVal)
            # Create all of the subtrees for the root node
                # When it hits a null value it'll propogate up
            rootNode.left = dfs()
            rootNode.right = dfs()

            return rootNode
        
        return dfs()