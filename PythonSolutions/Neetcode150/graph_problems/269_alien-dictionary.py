class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        # Create directed graph
        for i in range(len(words) - 1):
            a, b = words[i], words[i+1]
            minLength = min(len(a), len(b))

            # Invalid: Second word is smaller than first word and a is prefix of b
                # (E.g. "abc" and "ab") breaks alien dictionary rules 
            if len(b) < len(a) and a[:minLength] == b:
                return ""
            
            # Find the first occurence of different letters between string a and b
            for j in range(minLength):
                if a[j] != b[j]:
                    # Vertex is the first string a
                    # Edge would be the second string b
                    graph[a[j]].append(b[j])
                    break
        
        cycle = set()
        completed = set()
        order = []

        # Topological sort
        def dfs(char):
            if char in cycle:
                return False
            
            if char in completed:
                return True
            
            cycle.add(char)
            for neiChar in graph[char]:
                # Cycle detected
                    # There is no valid order for the result from the given rules
                if not dfs(neiChar):
                    return False

            cycle.remove(char)
            completed.add(char)
            order.append(char)

            return True
        
        for word in words:
            for char in word:
                if not dfs(char):
                    return "" # Return no result if there is no valid order
        
        # Order will be in reverse order b/c of backtracking
        return "".join(order)[::-1]
