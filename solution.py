from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if endWord is in wordList - early return if not
        if endWord not in wordList:
            return 0
            
        # Create a set of words for the graph construction
        # This removes duplicates and allows us to add beginWord without modifying the original list
        word_set = set(wordList)
        word_set.add(beginWord)

        # Build the graph of wildcard patterns
        graph = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                # Create the wildcard pattern
                pattern = word[:i] + "*" + word[i+1:]
                # Construct the graph
                graph[pattern].append(word)
        
        # Begin the search using the beginning word
        queue = deque([beginWord])
        visited = set([beginWord])  # Mark beginWord as visited immediately

        # Start level counting at 1 since we are starting at beginning word
        count = 1

        # Begin the search and jump to nodes that are only different by a single letter
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                currWord = queue.popleft()

                # Base case: We found the ending word, stop searching
                if currWord == endWord:
                    return count
                
                # Generate all possible patterns for the current word
                for i in range(len(currWord)):
                    pattern = currWord[:i] + "*" + currWord[i+1:]
                    
                    # Explore each adjacent neighbor for current pattern
                    for neiWord in graph[pattern]:
                        if neiWord not in visited:  # This is where we use O(1) lookup with the visited set
                            visited.add(neiWord)
                            queue.append(neiWord)
            
            count += 1

        return 0  # If we can't reach endWord 