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