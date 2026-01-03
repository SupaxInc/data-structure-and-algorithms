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


type TreeResult = TreeNode | null;

const isSameTree = (p: TreeResult, q: TreeResult): boolean => {
    if (!p && !q) {
        return true;
    }

    if ((!p || !q) || (p.val !== q.val)) {
        return false;
    }

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

const isSubtree = (root: TreeResult, subRoot: TreeResult): boolean => {
    if (!subRoot) {
        return true;
    }

    if (!root) {
        return false;
    }

    if (isSameTree(root, subRoot)) {
        return true;
    }

    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};