class BellmanFordSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Map nth prices (vertices) to infinity then initialize the source vertex as 0
            # Source is 0 since price to source is 0
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k+1):
            # Copy current prices to next_prices to prepare for the next iteration
            next_prices = prices.copy()

            for s, t, p in flights: # (source, target, price)
                # If a cheaper price is found from current prices source compared to target 
                    # Replace the next iterations target vertex price to the current source price
                if prices[s] + p < next_prices[t]:
                    next_prices[t] = prices[s] + p
            
            # Update the current prices to the next prices for next iteration
            prices = next_prices
        
        # If the price of distance is still infinity then that means we didn't have enough stops to reach distance
        return prices[dst] if prices[dst] != float("inf") else -1

class DijkstraSolution:
    def findCheapestPrice(n, flights, src, dst, K):
        # Build the graph
        graph = {}
        for start, end, cost in flights:
            if start not in graph:
                graph[start] = []
            graph[start].append((end, cost))
        
        # Min heap priority queue: (cost, current city, stops made)
        pq = [(0, src, 0)]
        
        while pq:
            cost, city, stops = heapq.heappop(pq)
            
            # Check if the current city is the destination
            if city == dst:
                return cost
            
            # If stops are within the allowed K stops, explore further
            if stops <= K:
                for next_city, next_cost in graph.get(city, []):
                    heapq.heappush(pq, (cost + next_cost, next_city, stops + 1))
                    
        # If destination cannot be reached within K stops
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