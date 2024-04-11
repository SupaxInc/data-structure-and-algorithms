class BottomUpSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Amount + 1, since its an upper boundary limit
            # We will never need more coins than the amount + 1
            # Helps figure out if we went over the amount
        dp = [amount + 1] * (amount + 1)

        # Base case: Takes 0 coins to get amount of 0
        dp[0] = 0 

        for i in range(1, amount + 1):
            for coin in coins:
                # If the current coin can contribute to the current amount i
                    # then we check if using current coin would reduce the number of coins needed.
                # Essentially prunes the search for the coin if it becomes negative
                if i - coin >= 0:
                    # Update to min of its current value
                        # Or the number of coins needed for (i - coin) plus one (for the current coin)
                        # E.g. i = 4, coin = 2, i-coin = 2, dp[2] + 1 (1 more coin 2) = 1 + 1 = 2 
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        # Return latest cached amount if it changed, else - 1
        return dp[amount] if dp[amount] != amount + 1 else -1

class TopDownSolution:
    def coinChange(coins, amount):
        # Memoization cache, initialized with None values
        memo = [None] * (amount + 1)
        
        def dp(n):
            # Base case: When amount is 0, no coins are needed
            if n == 0: return 0
            # If the amount is negative, return -1 indicating it's not possible to form this amount
            if n < 0: return -1
            # If we have already solved this subproblem, return the answer from cache
            if memo[n] is not None: return memo[n]
            
            # Initialize the minimum count to a large value
            min_coins = float('inf')
            # Try every coin and take the best option
            for coin in coins:
                res = dp(n - coin)
                # If it's possible to form the amount n - coin, update min_coins
                if res >= 0:
                    min_coins = min(min_coins, 1 + res)
            
            # Update the memo cache with the result for this amount
            memo[n] = min_coins if min_coins != float('inf') else -1
            return memo[n]
        
        return dp(amount)
