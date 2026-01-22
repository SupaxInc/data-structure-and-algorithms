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


const isValidBST = (root: TreeNode | null): boolean => {
    if (!root) return true;

    const validate = (node, low, high): boolean => {
        if (!node) return true;

        if (!(low < node.val && high > node.val)) {
            return false;
        }

        return validate(node.left, low, node.val) && validate(node.right, node.val, high);
    }

    return validate(root, -Infinity, Infinity);
}; 