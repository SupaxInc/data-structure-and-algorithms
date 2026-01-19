export {};
class Node {
    constructor(
        public key: number = 0,
        public val: number = 0,
        public nxt: Node | null = null,
        public prv: Node | null = null,
    ) {}
}

class LRUCache {
    private cache: Record<number, Node>;
    private head: Node;
    private tail: Node;

    constructor(private capacity: number) {
        this.cache = {};
        this.head = new Node();
        this.tail = new Node();

        this.head.nxt = this.tail;
        this.tail.prv = this.head;
    }

    private add(node: Node) {
        const tempNode = this.head.nxt!;
        this.head.nxt = node;
        node.prv = this.head;
        node.nxt = tempNode;
        tempNode.prv = node;

        this.cache[node.key] = node;
    }

    private remove(key: number) {
        const existingNode = this.cache[key];
        if (!existingNode) return;

        const prevNode = existingNode.prv!;
        const nextNode = existingNode.nxt!;

        prevNode.nxt = nextNode;
        nextNode.prv = prevNode;

        delete this.cache[key];
    }

    private evict() {
        const tailNode = this.tail.prv!;
        this.remove(tailNode.key);
    }

    get(key: number): number {
        if (!this.cache[key]) return -1;

        const existingNode = this.cache[key];
        if(!existingNode) return -1;

        this.remove(key);
        this.add(existingNode);
        
        return this.cache[key].val;
    }

    put(key: number, value: number): void {
        if (!this.cache[key]) {
            if (Object.values(this.cache).length === this.capacity) {
                this.evict();
            }

            const newNode = new Node(key, value);
            this.add(newNode);
        } else {
            const existingNode = this.cache[key];
            existingNode.val = value;
            this.remove(key);
            this.add(existingNode);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */