export {};

class TrieNode {
    children: Record<string, TrieNode> = {};
    isEnd: boolean = false;

    constructor() {}
}

class WordDictionary {
    root: TrieNode;
    constructor() {
        this.root = new TrieNode();
    }

    addWord(word: string): void {
        let curr = this.root;

        for (const char of word) {
            if (!curr.children[char]) {
                curr.children[char] = new TrieNode();
            }

            curr = curr.children[char];
        }

        curr.isEnd = true;
    }

    search(word: string): boolean {
        const dfs = (i: number, curr: TrieNode): boolean => {
            if (i === word.length) return curr.isEnd;

            const char = word[i];

            if (char === ".") {
                for (const child of Object.values(curr.children)) {
                    if (dfs(i+1, child)) return true;
                }

                return false;
            }

            if (!curr.children[char]) return false

            curr = curr.children[char];

            return dfs(i+1, curr);
        }

        return dfs(0, this.root);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */