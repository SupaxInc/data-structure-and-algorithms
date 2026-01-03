export {};
//! In leetcode interviews for TS, we might be able to be given the library
import { Queue } from '@datastructures-js/queue';

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

const maxDepthDFS = (root: TreeResult): number => {
    if (!root) {
        return 0;
    }

    const postOrderDFS = (node: TreeResult): number => {
        if (!node) {
            return 0;
        }

        const left = postOrderDFS(node.left);
        const right = postOrderDFS(node.right);

        const count = 1 + Math.max(left, right);
        return count;
    }

    return postOrderDFS(root);
};

const maxDepthBFS = (root: TreeResult): number => {
    if (!root) {
        return 0;
    }

    const queue = new Queue<TreeNode>([root]);
    let level = 0;

    while (!queue.isEmpty()) {
        //! Need to assign queue size since it gets re-evaluated PER iteration of a loop
        const levelSize = queue.size();
        level++;
        for (let i = 0; i < levelSize; i++) {
            const curr = queue.dequeue()!;

            if (curr.left) {
                queue.enqueue(curr.left);
            }
            if (curr.right) {
                queue.enqueue(curr.right);
            }
        }
    }

    return level;
};