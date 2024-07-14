class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # word[:i], get everything until the index
                # word[i+1:], get everything after index
                # E.g. *ot, h*t, ho*
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word) # Undirected graph
        
        queue = deque([beginWord])
        # Visit begin word right away
            # This is because when we visit the patterns, the neighbours word will be visited right away
            # E.g. after the "if nei not in visit" below
        visit = set([beginWord])
        count = 1 # Begin with 1 since we are visiting beginWord right away
        
        # BFS level order traversal
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                curr = queue.popleft()

                # When we reach the end word, no need to continue
                if curr == endWord:
                    return count
                
                # Create the patterns for the length of current word
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i+1:]
                    for nei in graph[pattern]:
                        # Visit the neighbours of the current word patterns: E.g. *ot, h*t, ho*
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            count += 1
        
        return 0
