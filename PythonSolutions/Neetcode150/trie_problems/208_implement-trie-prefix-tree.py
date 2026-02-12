from typing import Dict

class TrieNode:

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        # Begin at root node
        curr = self.root

        # Traverse through each characters in the word
        for char in word:
            # If the char does not exist as child, create it, else traverse
            if char not in curr.children:
                curr.children[char] = TrieNode()

            curr = curr.children[char]
        
        # Mark so we know we were able to create a word
        curr.is_end = True
    
    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.is_end
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]

        return True 

class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # Create 26 length for alphabet
        self.is_end = False    

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
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if curr.children[idx] != None:
                curr = curr.children[idx]
            else:
                return False
        
        # Return if the word we searched for was actually inserted as a word
        return curr.is_end

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