class BellmanFordSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create a map of distances per node
        distances = [float("inf")] * n
        distances[src] = 0 # Set source node distance as 0 as we are starting here

        # Relax the edges k times (a stop PER relaxation)
        for _ in range(k+1): # k+1, since the end is non-inclusive so we need to add 1
            # Deep copy the distance to:
                # - Make sure we don't multi-hop stops in 1 iteration
                # - Happens due to calculating the distances to other nodes so we'll end up cascading to other paths
                # - Ensure that we adhere to the constraint of only K stops (relax once per stop)
            newDistances = distances.copy()

            for source, target, distance in flights:
                # Calculate a new distance only if:
                    # - We have already found a path to the current source node
                    # - The distance from current source to target is less than the PREVIOUS relaxation distance of target
                        # - Compare CURRENT (distances) relaxation with PREVIOUS (newDistances) relaxation distances
                if distances[source] != float("inf") and distances[source] + distance < newDistances[target]:
                    newDistances[target] = distances[source] + distance
            
            # Change the previous new iteration of relaxation distances to the updated distances
            distances = newDistances
        
        # Return the destinations distance if we were able to reach it
        return distances[dst] if distances[dst] < float("inf") else -1


class DjikstraSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create the directed graph
        graph = defaultdict(list)
        for source, target, cost in flights:
            graph[source].append((target, cost)) # Source: (target, cost)
        
        # Setup the priority queue using first source node
        minHeap = [(0, src, 0)] # (cost, current node, stops)

        # Setup the costs dictionary to keep track of costs for every stop in relation to the source node
        costs = {(src, 0): 0} # (Source, Stops): cost
        # Since we have a tuple that keeps track of stops for every cost, we no longer need a traditional visited set

        # Run the BFS starting from source node
        while minHeap:
            currCost, currNode, currStop = heapq.heappop(minHeap)

            # Base case 1: Stop when we get the first occurence of hitting the distance target
                # - The first occurence of hitting distance means we greedily found the smallest cost within k stops
            if currNode == dst:
                return currCost
            
            # Base case 2: Skip current node if current stop went over required K stops
            if currStop > k:
                continue
            
            # Remember: No need for traditional visited set, we can use the costs tuple below (source, stops)

            # Explore the neighbors to try and add more nodes that have not been visited
            for neiNode, neiCost in graph[currNode]:
                newCost = currCost + neiCost

                # Add the new price to heap if:
                    # - We have not visited the node with current stop + 1 yet (replaces traditional visited set)
                    # - OR if we have visited the node with current stop + 1 BUT new price is less than nodes curr price
                if (neiNode, currStop + 1) not in costs or newCost < costs[(neiNode, currStop + 1)]:
                    costs[(neiNode, currStop + 1)] = newCost
                    heapq.heappush(minHeap, (newCost, neiNode, currStop + 1))
        
        # If we were able to reach the distance, return -1
        return -1
        

    
class NonOptimizedBFSSolution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = {}
        for u, v, w in flights:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        # Queue item: (current city, total cost so far, stops made)
        queue = deque([(src, 0, -1)])  # Start with -1 stops since the start doesn't count as a stop
        min_cost = float('inf')
        
        while queue:
            city, cost, stops = queue.popleft()
            if city == dst:
                min_cost = min(min_cost, cost)
                continue
            if stops == K:
                continue
            for next_city, price in graph.get(city, []):
                if cost + price < min_cost:  # Pruning: only consider if not already more expensive
                    queue.append((next_city, cost + price, stops + 1))
                    
        return min_cost if min_cost != float('inf') else -1