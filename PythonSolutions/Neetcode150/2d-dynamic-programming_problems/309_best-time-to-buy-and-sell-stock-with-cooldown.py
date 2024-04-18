class BruteFroceSolution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(index, holding):
            if index >= len(prices):
                return 0
            
            # Ignore choice: Skip to the next day, explore all ignores
            profit = dfs(index + 1, holding)

            # Sell choice: If we are holding stock, we can sell
            if holding:
                # Choose max between ignore profit or sell profit (+2 for cooldown after selling)
                profit = max(profit, prices[index] + dfs(index + 2, False))
            # Buy choice
            else:
                profit = max(profit, -prices[index] + dfs(index + 1, True))
            
            return profit

        return dfs(0, False)

class TopDownSolution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(index, holding):
            if (index, holding) in cache:
                return cache[(index, holding)]
            if index >= len(prices):
                return 0
            
            # Ignore choice: Skip to the next day, explore all ignores
            cache[(index, holding)] = dfs(index + 1, holding)

            # Sell choice: If we are holding stock, we can sell
            if holding:
                # Choose max between ignore profit or sell profit (+2 for cooldown after selling)
                cache[(index, holding)] = max(cache[(index, holding)], prices[index] + dfs(index + 2, False))
            # Buy choice
            else:
                cache[(index, holding)] = max(cache[(index, holding)], -prices[index] + dfs(index + 1, True))
            
            return cache[(index, holding)]

        return dfs(0, False)
    
class BottomUpSolution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0  # Return 0 profit if prices list is empty
        
        n = len(prices)
        # Initialize a 2D DP array with 2 columns: 0 for no stock, 1 for holding stock
        dp = [[0] * 2 for _ in range(n)]

        # Base cases initialization
        dp[0][0] = 0          # No profit as no stock is bought or sold on day 0
        dp[0][1] = -prices[0] # Profit from buying stock on day 0 (investing money, thus negative profit)
        
        for i in range(1, n):
            # dp[i][0]: Maximum profit on day i without holding any stock
            # It can be achieved either by:
            # a) not holding any stock from the previous day (dp[i-1][0]),
            # b) selling the stock held from the previous day (dp[i-1][1] + prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            
            # dp[i][1]: Maximum profit on day i with holding stock
            # It can be achieved either by:
            # a) holding onto the stock from the previous day (dp[i-1][1]),
            # b) buying new stock today. If buying new, we need to ensure we didn't buy the previous day 
            #    (cooldown). Hence we use profit from day i-2 (dp[i-2][0] if i > 1 else 0) and subtract 
            #    today's price.
            dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i > 1 else 0) - prices[i])

        # The result is the maximum profit on the last day, with no stock left in hand.
        return dp[n-1][0]

class MostOptimizedSolution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        if n <= 1:
            return 0
        
        # Variables to keep track of profits on days with different states
        # prev_sold: max profit till day i-1 where the last action was selling the stock
        # prev_hold: max profit till day i-1 where the last action was holding the stock
        # prev_rest: max profit till day i-1 where the last action was resting
        prev_sold = 0
        prev_hold = -prices[0]
        prev_rest = 0

        for i in range(1, n):
            # Update the profits based on today's actions
            curr_sold = prev_hold + prices[i]  # Sell today
            curr_hold = max(prev_hold, prev_rest - prices[i])  # Buy today or keep holding
            curr_rest = max(prev_rest, prev_sold)  # Rest today (no transaction)

            # Update previous day's profits for next iteration
            prev_sold = curr_sold
            prev_hold = curr_hold
            prev_rest = curr_rest

        # The final maximum profit, considering not holding any stock at the end
        return max(prev_rest, prev_sold)
