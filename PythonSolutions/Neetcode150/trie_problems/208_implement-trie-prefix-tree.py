class TrieNode:
    def __init__(self):
        self.children = {}
        # We need to mark a trie node if it was actually inserted as a word
        # Ex. We insert apple, but search for "app".
            # Searching "app" should not return true since it wasn't inserted as a word
        self.markEndOfWord = False

class NotOptimizedTrie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # If character exists, traverse to it so we can access the other children nodes
            if char in curr.children:
                curr = curr.children[char]
            else:
                # If it doesn't exist insert a new trie node
                curr.children[char] = TrieNode()
                curr = curr.children[char]
    
        # Mark the end of the word as true so it can be searchable
        curr.markEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        
        # Return if the word we searched for was actually inserted as a word
        return curr.markEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False

        return True

class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # Create 26 length for alphabet
        self.isEndOfWord = False    

class OptimizedTrie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # Get the index in 0 based 
            idx = ord(char) - ord("a")

            if curr.children[idx] != None:
                curr = curr.children[idx]
            else:
                curr.children[idx] = TrieNode()
                curr = curr.children[idx]
    
        # Mark the end of the word as true so it can be searchable
        curr.markEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if curr.children[idx] != None:
                curr = curr.children[idx]
            else:
                return False
        
        # Return if the word we searched for was actually inserted as a word
        return curr.markEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord("a")
            if curr.children[idx] != None:
                curr = curr.children[idx]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)