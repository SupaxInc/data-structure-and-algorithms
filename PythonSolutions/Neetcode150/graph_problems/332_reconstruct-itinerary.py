class OptimizedSolution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Create adjacency list
            # O(E Log E)
        for frm, to in tickets:
            # Using min heap so that the graph neighbours are in lexical order when pop it
            heapq.heappush(graph[frm], to)

        itinerary = deque()

        def dfs(src):
            # Visit (nothing here)

            # Explore as deep as possible
                # Using while loop instead of for loop so we can heap pop and grab lexical order
                # For loop prevents from being able to heappop the next node
            while graph[src]:
                next_node = heapq.heappop(graph[src])
                dfs(next_node)
            
            # Unvisit (backtrack)
                # Add the node to the front of the itinerary (reverse order of visitation completion)
                # E.g. A > B > C -> backtrack so we explore as deep as possible to C
                    # The backtrack order will be: C -> B -> A, which creates array: [A, B, C]
            itinerary.appendleft(src)
        
        # Always starting at JFK
        dfs('JFK')

        return list(itinerary)
    
class LessOptimizedSolution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph as an adjacency list
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        # Sort each adjacency list lexicographically
            # Less Optimized O(V Log V)
        for src in graph:
            graph[src].sort()

        result = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop(0)  # Use pop(0) which is less efficient, takes O(E) time compared to popleft() which is O(1)
                dfs(next_node)
            result.append(node)

        dfs("JFK")
        return result[::-1]
