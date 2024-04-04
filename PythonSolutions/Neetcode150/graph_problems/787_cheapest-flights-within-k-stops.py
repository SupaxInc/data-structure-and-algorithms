class Solution:
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