export {};
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

const kthSmallest = (root: TreeNode | null, k: number): number => {
    let count = 0;

    const inorderDFS = (node: TreeNode | null): number => {
        if (!node) return -1;

        const leftVal = inorderDFS(node.left);
        if (leftVal !== -1) return leftVal;

        count++;
        if (count === k) return node.val;

        const rightVal = inorderDFS(node.right);
        if (rightVal !== -1) return rightVal;

        return -1;
    };

    return inorderDFS(root);
 };