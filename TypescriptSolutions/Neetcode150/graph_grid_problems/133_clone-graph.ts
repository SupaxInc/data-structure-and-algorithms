
class _Node {
    val: number
    neighbors: _Node[]

    constructor(val?: number, neighbors?: _Node[]) {
        this.val = (val===undefined ? 0 : val)
        this.neighbors = (neighbors===undefined ? [] : neighbors)
    }
}



type GraphNode = _Node | null;

const cloneGraph = (node: GraphNode): GraphNode => {
    if (!node) return null;

    const oldToNew = new Map<GraphNode, GraphNode>();

    const dfs = (curr: GraphNode): GraphNode => {
        if (oldToNew.has(curr)) return oldToNew.get(curr)!;

        const copyNode = new _Node(curr!.val);
        oldToNew.set(curr, copyNode);

        for (const nei of curr!.neighbors) {
            copyNode.neighbors.push(dfs(nei)!);
        }

        return copyNode;
    };

    return dfs(node);
};