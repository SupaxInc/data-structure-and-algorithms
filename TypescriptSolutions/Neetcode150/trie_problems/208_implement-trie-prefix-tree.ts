export {};

class TrieNode {
    children: Record<string, TrieNode> = {};
    is_end: boolean = false;

    constructor() {}
}

class Trie {
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