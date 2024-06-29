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

class LessOptimizedSolution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.res = set() # Set to avoid duplicates
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
        if row > self.ROWS - 1 or col > self.COLS - 1 or row < 0 or col < 0 or self.board[row][col] == "":
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

# MORE OPTIMIZED SOLUTION

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.end = False    # Flag to mark end of a word
        self.parent = None  # Reference to parent node for easier backtracking

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the root of the Trie

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                curr.children[char].parent = curr  # Set parent for backtracking
            curr = curr.children[char]
        curr.end = True  # Mark the end of the word

    def deleteWord(self, word): 
        curr = self.root
        stack = []
        # Traverse to the end of the word
        for char in word:
            if char in curr.children:
                stack.append(curr)
                curr = curr.children[char]
            else:
                return  # Word not in trie, nothing to delete
        
        # Set end of word to False and pop the stack of traversed nodes to remove previous nodes
        curr.end = False
        for char in reversed(word):
            parent = stack.pop()
            if not curr.children and not curr.end:
                del parent.children[char]  # Remove the node if it's a leaf and not end of another word
            curr = parent

class MoreOptimizedSolution:
    def findWords(self, board, words):
        self.res = set()  # Use set to avoid duplicates
        self.board = board
        self.ROWS, self.COLS = len(board), len(board[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Possible directions: right, down, up, left

        self.trie = Trie()
        for word in words:
            self.trie.addWord(word)

        # Iterate through each cell in the board
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.dfs(row, col, self.trie.root, [])
        
        return list(self.res)

    def dfs(self, row, col, node, path):
        # Check if out of bounds or cell already visited
        if row < 0 or col < 0 or row >= self.ROWS or col >= self.COLS or self.board[row][col] == "#":
            return

        char = self.board[row][col]
        if char not in node.children:
            return  # Current character not in Trie path, backtrack

        node = node.children[char]
        path.append(char)
        
        if node.end:
            word = "".join(path)
            self.res.add(word)
            self.trie.deleteWord(word)  # Remove found word from Trie to optimize future searches

        # Temporarily mark the cell as visited
        self.board[row][col] = "#"
        
        # Explore all four directions
        for dx, dy in self.DIRS:
            self.dfs(row + dx, col + dy, node, path)
        
        # Restore the cell's original character for backtracking
        self.board[row][col] = char
        path.pop()  # Remove current character from path for backtracking
