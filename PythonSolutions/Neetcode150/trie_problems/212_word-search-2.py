class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        
        curr.end = True

class EasyNonOptimizedSolution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.res = set()
        self.board = board
        self.ROWS, self.COLS = len(board), len(board[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        trie = Trie()

        for word in words:
            trie.addWord(word)

        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.dfs(row, col, trie.root, [])
        
        return self.res

    def dfs(self, row, col, node, path):
        # Base case: Boundary check
        if row > self.ROWS - 1 or col > self.COLS - 1 or row < 0 or col < 0:
            return
        
        char = self.board[row][col]
        # Prune search: Letter not in current trie path
        if char not in node.children:
            return
        
        # Visit
        self.board[row][col] = ""
        path.append(char)
        node = node.children[char]
        if node.end:
            self.res.add("".join(path))

        # Explore
        for rowDir, colDir in self.DIRS:
            self.dfs(row+rowDir, col+colDir, node, path)
        
        # Unvisit
        self.board[row][col] = char
        path.pop()
