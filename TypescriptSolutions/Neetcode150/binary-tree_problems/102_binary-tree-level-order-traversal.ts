import { Queue } from "@datastructures-js/queue";

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

const levelOrder = (root: TreeNode): number[][] => {
    if (!root) return [];

    const res: number[][] = [];
    const queue = new Queue([root]);

    while (!queue.isEmpty()) {
        const level: number[] = [];
        const n = queue.size();
        
        for (let i = 0; i < n; i++) {
            const curr = queue.dequeue()!;
            level.push(curr.val);

            if (curr.left) queue.enqueue(curr.left);
            if (curr.right) queue.enqueue(curr.right);
        }

        res.push(level);
    }

    return res;
};