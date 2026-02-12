export {};

class TrieNode {
    children: Record<string, TrieNode> = {};
    is_end: boolean = false;

    constructor() {}
}

class NotOptimizedTrie {
    root: TrieNode;

    constructor () {
        this.root = new TrieNode();
    }

    insert(word: string): void {
        let curr = this.root;

        for (const char of word) {
            if (!curr.children[char]) curr.children[char] = new TrieNode();

            curr = curr.children[char];
        }

        curr.is_end = true;
    }

    search(word: string): boolean {
        let curr = this.root;

        for (const char of word) {
            if (!curr.children[char]) return false;

            curr = curr.children[char];
        }

        return curr.is_end;
    }

    startsWith(prefix: string): boolean {
        let curr = this.root;

        for (const char of prefix) {
            if (!curr.children[char]) return false;

            curr = curr.children[char];
        }

        return true;
    }
}

class OptimizedTrieNode {
    children: (OptimizedTrieNode|null)[];
    is_end: boolean = false;

    constructor () {
        this.children = new Array(26).fill(null);
    }
}

class OptimizedTrie {
    root: OptimizedTrieNode;

    constructor() {
        this.root = new OptimizedTrieNode();
    }

    insert(word: string): void {
        let curr = this.root;

        for (const char of word) {
            const idx = char.charCodeAt(0) - "a".charCodeAt(0);

            if (curr.children[idx] === null) {
                curr.children[idx] = new OptimizedTrieNode();
            }

            curr = curr.children[idx];
        }

        curr.is_end = true;
    }

    search(word: string): boolean {
        let curr = this.root;

        for (const char of word) {
            const idx = char.charCodeAt(0) - "a".charCodeAt(0);

            if (curr.children[idx] === null) return false;

            curr = curr.children[idx];
        }

        return curr.is_end;
    }

    startsWith(prefix: string): boolean {
        let curr = this.root;

        for (const char of prefix) {
            const idx = char.charCodeAt(0) - "a".charCodeAt(0);

            if (curr.children[idx] === null) return false;

            curr = curr.children[idx];
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */