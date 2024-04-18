class BruteForceSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(index, amount):
            # Base case 1: Amount became 0 so its a valid combination
            if amount == 0:
                return 1
            # Base case 2: Not a valid combination
            if amount < 0 or index == len(coins):
                return 0
            
            # Choice 1: Use the current index coin
            useCoin = dfs(index, amount - coins[index])
            # Choice 2: Skip the current index coin
            skipCoin = dfs(index + 1, amount)
            
            # Add both to see possible combinations for both choices
            return useCoin + skipCoin
        
        return dfs(0, amount)
    
class TopDownSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(index, amount):
            # Already in cache
            if (index, amount) in cache:
                return cache[(index, amount)]
            # Base case 1: Amount became 0 so its a valid combination
            if amount == 0:
                return 1
            # Base case 2: Not a valid combination
            if amount < 0 or index == len(coins):
                return 0
            
            # Choice 1: Use the current index coin
            useCoin = dfs(index, amount - coins[index])
            # Choice 2: Skip the current index coin
            skipCoin = dfs(index + 1, amount)
            
            cache[(index, amount)] = useCoin + skipCoin
            # Add both to see possible combinations for both choices
            return cache[(index, amount)]
        
        return dfs(0, amount)


class BottomUpSolution:
    def change(self, amount, coins):
        # dp[i][j] will hold the number of ways to make amount j using the first i coins.
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # There's one way to make amount 0 with any number of coins: use no coins
        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                # Don't use the current coin
                    # Use the previous coins
                    # Captures all combinations that don't use current coin.
                    # E.g. coins = [1, 2, 3], i = 2 (coin 3), which means all combinations from 1 and 2 coins
                dp[i][j] = dp[i - 1][j]
                
                # If we use at least one of the current coin
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        # The bottom right cell of the dp table will contain the answer
        return dp[len(coins)][amount]