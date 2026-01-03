
// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}


type TreeResult = TreeNode | null;

 const invertTree = (root: TreeResult): TreeResult => {
    if (!root) {
        return root;
    }

    const postOrderDFS = (node: TreeResult): TreeResult => {
        if (!node) {
            return node;
        }

        const left = postOrderDFS(node.left);
        const right = postOrderDFS(node.right);
        
        node.left = right;
        node.right = left;
        
        return node;
    };

    return postOrderDFS(root);
 };