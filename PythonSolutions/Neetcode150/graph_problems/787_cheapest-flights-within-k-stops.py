class BellmanFordSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Map nth prices (vertices) to infinity then initialize the source vertex as 0
            # Source is 0 since price to source is 0
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            # Need to copy the previous price
                # Ensures that within each iteration, we are not mixing updates from the same iteration
                # Also helps adhere to the 'at most k stops' constraints
            new_prices = prices.copy()

            for s, t, p in flights: # (source, target, price)
                # If a cheaper price is found from current prices source compared to target 
                    # Replace the next iterations target vertex price to the current source price

                # You can see the importance of copying the previous price iteration here
                    # We are comparing PREVIOUS iteration price of source flight 
                    # Againsts NEW iteration price of target flight
                    # Helps prevent calculating cycles too
                if prices[s] != float('inf') and prices[s] + p < new_prices[t]:
                    new_prices[t] = prices[s] + p
            
            prices = new_prices
        
        return prices[dst] if prices[dst] != float('inf') else -1


class DjikstraSolution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Create the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # Priority queue to store (cost, current_node, stops)
        # Initialize with the starting node, with cost 0 and 0 stops
        pq = [(0, src, 0)]
        
        # Dictionary to store the minimum cost to reach each node with at most k stops
        # The key is a tuple (node, stops), and the value is the minimum cost to reach that node
        costs = {(src, 0): 0}

        while pq:
            # Pop the node with the smallest cost
            cost, node, stops = heapq.heappop(pq)
            
            # If we reached the destination within k stops, return the cost
            if node == dst:
                return cost
            
            # If the number of stops exceeds k, continue to the next iteration
            if stops > k:
                continue
            
            # Explore the neighbors of the current node
            for neighbor, price in graph[node]:
                new_cost = cost + price
                # If the cost to reach the neighbor with stops + 1 is less than any previously known cost
                # for the same number of stops, update the cost and push it to the priority queue
                    # (neighbor, stops + 1) prevents redundant checking of already visited nodes at k stop
                if (neighbor, stops + 1) not in costs or new_cost < costs[(neighbor, stops + 1)]:
                    costs[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        # If we exhaust the priority queue without finding a valid path, return -1
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