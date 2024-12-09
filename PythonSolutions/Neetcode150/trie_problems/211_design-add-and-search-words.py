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

            # Similar to backtracking, we will explore the children nodes as deep as possible starting from j
                # j is the index of the word we are currently on, and it will be used to be able to skip the letter
                # If we end up passing the length of word when we skip the letter, it checks if the current node is the end of a word
            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    # Go through all children trie nodes
                    for child in curr.children.values():
                        # Do a dfs on the next character since were passing all child nodes
                        # This means we've essentially skipped the "." character
                        # Example: "d..", on the last . we would be on the last node
                            # So if the last nodes end property is true, it would return true
                            # which lets us return True again breaking the DFS, returning True from the function
                        if dfs(i+1, child):
                            return True
                        
                    # If the DFS fails, it means we couldn't find a match for the whole word
                    return False
                else: 
                    # If the char does not exist, return False so that we can check other children nodes if it contains the letter
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