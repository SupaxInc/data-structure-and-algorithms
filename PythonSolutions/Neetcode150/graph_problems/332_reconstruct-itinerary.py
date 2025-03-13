class OptimizedSolution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create graph adjacent list (min heap)
        graph = defaultdict(list)
        for frm, to in tickets:
            # graph[frm] which is initially a list is treated as a min heap
                # Adds to min heap so that cities are in lexical order
            heapq.heappush(graph[frm], to)
        
        # Keep track of itinerary using a queue
        itinerary = deque()

        # Post-order DFS, backtrack
        def dfs(node):
            # Visit (do nothing)

            # Explore current option (node) as deep as possible
                # Hard to empty a heap with for loop, while loop is better here
            while graph[node]:
                newNode = heapq.heappop(graph[node]) # O(E log E) instead of O(E) for pop(0)
                dfs(newNode)
            
            # Backtrack (visit node during backtracking after exploring all child nodes)
                # appendleft() allows us to add to beginning of list
                # during backtracking, the order gets reversed and using appendleft prevents that
                # this is also a small optimization without having to reverse list at the end
                    # normal append still works, this is a minimal optimization
            itinerary.appendleft(node) # O(1)

        dfs("JFK")
        return list(itinerary)
    
class LessOptimizedSolution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create adjacent list graph
        graph = defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        
        # Sort each neighbor list in the graph in lexical order (alphabetical)
        for src in graph: # O(E log E)
            graph[src].sort()
        
        # Keep track of the order of visited cities in lexical order
        itinerary = []

        # Postorder DFS, backtracking
        def dfs(node):
            # Visit (do nothing)

            # Explore current option (node) as deep as possible
                # Uses while loop over for loop since we can't pop from list properly
            while graph[node]:
                # Use pop(0) to pop from the beginning of list to get first city in lexical order
                    # O(n) operation in normal lists
                newNode = graph[node].pop(0) # O(E) -> becomes O(E^2) since we visit all edges
                dfs(newNode)
            
            # Backtrack
            itinerary.append(node) # Append will add the cities in reverse order

        # Always begin at JFK
        dfs("JFK")
        # Reverse the itinerary so it is in reversed order
        return itinerary[::-1]
