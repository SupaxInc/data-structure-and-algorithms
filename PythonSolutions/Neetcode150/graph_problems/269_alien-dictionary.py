class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        # Create the directed graph to order the aliens alphabet
        for i in range(len(words) - 1):
            a, b = words[i], words[i+1]
            minWordLength = min(len(a), len(b))

            # Invalid: length of b is smaller than a AND b is a prefix of a
                # E.g. a = "abc", b = "ab" -> ab == ab, breaks dictionary rules
            if len(b) < len(a) and b == a[:minWordLength]:
                return ""
            
            # Connect the letters in a graph for first words that differ by word prefix length
                # minWordLength is prefix length
                # Covers scenarios:
                    # - Where length of b > a, so we need to use prefix of smaller word
                    # - Both words have same length
            for j in range(minWordLength):
                if a[j] != b[j]:
                    graph[a[j]].append(b[j])

                    # Only 1 letter can be connected
                    break
        
        visited = set()
        completed = set()
        order = deque()
        # Run topographical sort on the created graph to get order of alphabet
        def dfs(node):
            # Base case 1: Node has already been visited, possible cycle detected
            if node in visited:
                return False
            # Base case 2: Node prereq has already been completed
            if node in completed:
                return True
            
            # Visit node
            visited.add(node)
            
            # Explore current node as deep as possible and try other options
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            # Backtrack
            visited.remove(node)
            completed.add(node) # Add the node as completed since we just visited it, "finishing" the ordering
            order.appendleft(node) # Append to the left of array since in backtracking it adds order in reverse

            return True
        
        for word in words:
            for letter in word:
                # DFS on every char to check if prereq was completed for each char
                if not dfs(letter):
                    # Cycle was detected, return empty string
                    return ""
        
        return "".join(list(order))
            
