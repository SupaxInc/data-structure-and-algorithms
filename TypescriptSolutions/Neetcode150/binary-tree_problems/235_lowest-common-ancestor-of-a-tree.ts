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


const lowestCommonAncestor = (root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode => {
    let curr = root;

    while (curr) {
        if (p!.val < curr.val && q!.val < curr.val) {
            curr = curr.left;
        } else if (p!.val > curr.val && q!.val > curr.val) {
            curr = curr.right;
        } else {
            return curr;
        }
    }

    return curr!;
};