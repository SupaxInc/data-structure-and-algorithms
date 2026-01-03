export {};


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

const diameterOfBinaryTree = (root: TreeNode | null): number => {
    if (!root) {
        return 0;
    }

    let maxLength = 0;

    const postOrderDFS = (node:  TreeNode | null): number => {
        if (!node) {
            return 0;
        }

        const left = postOrderDFS(node.left);
        const right = postOrderDFS(node.right);

        maxLength = Math.max(maxLength, left + right);

        return 1 + Math.max(left, right);
    };
    
    postOrderDFS(root);
    return maxLength;
};