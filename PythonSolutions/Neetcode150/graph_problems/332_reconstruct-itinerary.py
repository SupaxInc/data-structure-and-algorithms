class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Create adjacency list
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
                    # The backtrack order will be: [C, B, A]
            itinerary.appendleft(src)
        
        # Always starting at JFK
        dfs('JFK')

        return list(itinerary)
