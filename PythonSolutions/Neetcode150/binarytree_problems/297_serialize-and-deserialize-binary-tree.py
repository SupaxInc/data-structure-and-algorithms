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

        tree = []

        # Encode the tree as a string using preorder traversal
        def dfs(node):
            if not node:
                tree.append("N")
                return tree
            
            tree.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

            return tree
        
        return ','.join(dfs(root))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        # Instead of keeping track of each node in an index and incrementing it
        # Use an iter instead and we can iterate through the list using next()
        data = iter(data.split(','))
        
        # Preorder traversal to reconstruct the tree
        def dfs():
            # No need to pass a node as a param in the dfs
            # Just iterate to the next value (preorder gives us the root nodes in order from left to right)
            rootVal = next(data)

            if rootVal == "N":
                return None
            
            node = TreeNode(rootVal)
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))