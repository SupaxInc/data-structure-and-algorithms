class _Node {
    val: number
    next: _Node | null
    random: _Node | null

    constructor(val?: number, next?: _Node, random?: _Node) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}


const copyRandomList = (head: _Node | null): _Node | null => {
    if (!head) return head;

    const oldToNew = new Map<_Node, _Node>();

    let curr = head;
    while (curr) {
        oldToNew.set(curr, new _Node(curr.val));
        curr = curr.next!;
    }

    curr = head;
    while(curr) {
        if (curr.next) {
            oldToNew.get(curr)!.next = oldToNew.get(curr.next)!;
        }

        if (curr.random) {
            oldToNew.get(curr)!.random = oldToNew.get(curr.random)!;
        }

        curr = curr.next!;
    }

    return oldToNew.get(head)!;
};