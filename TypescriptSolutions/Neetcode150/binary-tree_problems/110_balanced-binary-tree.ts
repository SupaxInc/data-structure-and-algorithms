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


const isBalanced = (root: TreeNode | null): boolean => {
    if (!root) {
        return true;
    }

    const dfs = (node: TreeNode | null): number => {
        if (!node) {
            return 0;
        }

        const left = dfs(node.left);
        if (left === -1) return -1;

        const right = dfs(node.right);
        if (right === -1) return -1;

        if (Math.abs(left-right) > 1) {
            return -1;
        }

        return 1 + Math.max(left, right);
    };

    return dfs(root) !== -1;
};