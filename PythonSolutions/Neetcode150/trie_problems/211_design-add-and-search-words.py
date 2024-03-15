class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()    

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    # Go through all children trie nodes
                    for child in curr.children.values():
                        # Do a dfs on the next character since were passing all child nodes
                        # This means we've essentially skipped the "." character
                        if dfs(i+1, child):
                            return True
                    # If the DFS fails, it means we couldn't find a match for the whole word
                    return False
                else: 
                    if char not in curr.children:
                        return False

                    # Normal traversal 
                    curr = curr.children[char]

            # Check if the end of search is an inserted word
            return curr.end
        
        return dfs(0, self.root)
                    
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)