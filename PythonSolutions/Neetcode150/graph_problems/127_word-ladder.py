class OptimizedSolution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Optmization: Changing word list to a set to prevent duplicates from being added to graph
        wordSet = set(wordList)
        # Add the beginning word to the list so we can add it as an edge in the graph
        wordSet.add(beginWord)

        graph = defaultdict(list)

        # Assemble the graph of wild cards
        for word in wordSet:
            for i in range(len(word)):
                # Create the wildcard pattern
                    # [:i]   -> grab letters in the word before the index
                    # "*"    -> add a wild card for each index
                    # [i+1:] -> grab letters in the word after the index
                # e.g. *ot, h*t, ho*
                pattern = word[:i] + "*" + word[i+1:]

                # Construct the graph
                graph[pattern].append(word)
        
        # Begin the search using the beginning word
        queue = deque([beginWord])
        visited = set()

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
                
                for i in range(len(currWord)):
                    pattern = currWord[:i] + "*" + currWord[i+1:]
                    # Explore each adjacent neighbour for current pattern
                    for neiWord in graph[pattern]:
                        # Optimization: Check if neighbour word is not in visited before processing it, prevents dequeuing same words multiple times
                        if neiWord not in visited:
                            visited.add(neiWord)
                            queue.append(neiWord)
            
            count += 1

        return 0

class NonOptimizedSolution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Optimization: Changing word list to a set to prevent duplicates from being added to graph
        wordSet = set(wordList)
        # Add the beginning word to the list so we can add it as an edge in the graph
        wordSet.add(beginWord)

        graph = defaultdict(list)

        # Assemble the graph of wild cards
        for word in wordSet:
            for i in range(len(word)):
                # Create the wildcard pattern
                    # [:i]   -> grab letters in the word before the index
                    # "*"    -> add a wild card for each index
                    # [i+1:] -> grab letters in the word after the index
                # e.g. *ot, h*t, ho*
                pattern = word[:i] + "*" + word[i+1:]

                # Construct the graph
                graph[pattern].append(word)
        
        # Begin the search using the beginning word
        queue = deque([beginWord])
        visited = set()

        # Start level counting at 1 since we are starting at beginning word
        count = 1

        # Begin the search and jump to nodes that are only different by a single letter
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                currWord = queue.popleft()

                # Base case 1: We have already visited the word
                if currWord in visited:
                    continue

                # Base case 2: We found the ending word, stop searching
                if currWord == endWord:
                    return count
                
                # Visit the current word node
                visited.add(currWord)
                
                for i in range(len(currWord)):
                    pattern = currWord[:i] + "*" + currWord[i+1:]
                    # Explore each adjacent neighbour for current pattern
                    for neiWord in graph[pattern]:
                        queue.append(neiWord)
            
            count += 1

        return 0