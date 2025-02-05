class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.DIRS = [(0,1), (1, 0), (-1, 0), (0, -1)]
        self.ROWS, self.COLS = len(board), len(board[0])
        self.trie = Trie()
        self.res = set() # Prevents duplication of answers in result set

        # Add each word to the Trie first so it can be used to search
        for word in words:
            self.trie.addWord(word)
        
        # Do a DFS in each cell in the board
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.dfs(row, col, self.trie.root, [])
        
        return list(self.res)

    def dfs(self, row, col, node, path):
        # Base case 1: Boundary checks
        if row > self.ROWS - 1 or col > self.COLS - 1 or row < 0 or col < 0:
            return
        
        # Base case 2: Visited check
        if self.board[row][col] == "":
            return
        
        char = self.board[row][col] # Keep track of current character
        # Check if character is in the Trie, else prune the search and backtrack
        if char not in node.children:
            return
        
        # Visit the cell if the character exists in the Trie
        self.board[row][col] = ""  # Visit the cell
        node = node.children[char] # Traverse the trie to *CURRENT* char node (all we did was first check if current char is in prev node's children)
        path.append(char)
        # Add the path to result set if we are at the end
        if node.isEnd:
            self.res.add("".join(path))

        # Traverse to the four other directions to find more matches in current Trie node
        for dx, dy in self.DIRS:
            self.dfs(row + dx, col + dy, node, path)
        
        # Unvisit the cell
        self.board[row][col] = char
        path.pop()



# * MORE OPTIMIZED SOLUTION *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.isEnd = True
    
    def removeWord(self, word):
        curr = self.root
        stack = []

        for char in word:
            if char in curr.children:
                stack.append(curr) # Add the parent of the char to the stack so it can be traversed later
                curr = curr.children[char]
            else:
                return # Char does not exist so word was not found, therefore, nothing to delete
        
        # The word we are about to delete is no longer the end of a word
        curr.isEnd = False

        # Begin at the tail end of the word so we can delete without removing leaf nodes
        for char in reversed(word):
            parent = stack.pop()

            # Check if current node we are still on is a leaf node (no children) and is not the end of a word
                # * This prevents removing a node that contains connections to other words
            if not curr.children and not curr.isEnd:
                # Begin removal of the current node using the parent
                del parent.children[char]
            
            # Make the current node the parent node
            curr = parent
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.ROWS, self.COLS = len(board), len(board[0])
        self.DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.res = set()
        self.trie = Trie()

        for word in words:
            self.trie.addWord(word)
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                self.dfs(row, col, self.trie.root, [])
        
        return list(self.res)
    
    def dfs(self, row, col, node, path):
        # Base case 1: Boundary check
        if row > self.ROWS - 1 or col > self.COLS - 1 or row < 0 or col < 0:
            return
        
        # Base case 2: Visited check
        if self.board[row][col] == "":
            return
        
        char = self.board[row][col]
        # Check if character is part of the Trie
        if char not in node.children:
            return
        
        # Visit the cell
        self.board[row][col] = ""
        # Traverse to CURRENT char node, all we did was check if char is in previous node's children
        node = node.children[char]
        path.append(char)

        if node.isEnd:
            word = "".join(path)
            self.res.add(word)
            self.trie.removeWord(word)

        for dx, dy in self.DIRS:
            self.dfs(row + dx, col + dy, node, path)
        
        # Unvisit the cell
        self.board[row][col] = char
        path.pop()
