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


const goodNodes = (root: TreeNode | null): number => {
    if (!root) return 0;

    let count = 0;

    const dfs = (node, maxInPath): number => {
        if (!node) return maxInPath;

        if (node.val >= maxInPath) {
            count++;
            maxInPath = node.val;
        }

        dfs(node.left, maxInPath);
        dfs(node.right, maxInPath);

        return maxInPath;
    };

    dfs(root, -Infinity);
    return count;
};