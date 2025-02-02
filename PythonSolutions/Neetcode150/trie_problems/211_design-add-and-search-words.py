class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

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
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            """
            Args:
                index: Current position in the word
                node: Current TrieNode we're examining
            """
            curr = node

            # Process the entire length of word that is being searched
            # This helps us know when to stop searching if we end up at a length too long due to usage of wildcards
            for i in range(j, len(word)):
                char = word[i]

                # If char is a wild card, use DFS to search all possibilities in the current node
                if char == ".":
                    # Go through all children in current node
                    for child in curr.children.values():
                        # Increment the index, essentially skipping the current character
                        # However, we still need to look if the next character is another wildcard or not
                        if dfs(i+1, child):
                            # If path was found return True, this breaks the DFS
                            return True
                    
                    # No path could be found
                    return False
                else:
                    # If char was not found in children, return False so we can backtrack and check other paths
                    if char not in curr.children:
                        return False
                    
                    # If char was found, traverse to it
                    curr = curr.children[char]
            
            # When the loop ends, either when length breaks or we have searched all possible paths
            # Check if were at the end of the word
            return curr.isEnd

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)