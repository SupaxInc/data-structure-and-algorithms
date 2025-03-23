"""
- coins array length from 1 to 12
- amount int from 1 to 10^4
- coins[i] consists of 32 bit numbers 
    - assume we have an infinite number of coins[i] that we can use
- RETURN: Fewest number of coins[i]

State: dp[i], i is the amount at that point, and dp[i] represents the amount of coins used at that amount
    - NOTE: dp[i] is the AMOUNT of coins used to reach amount, not the EXACT coins that were used

Recurrence Relation: At each amount i, find the number of coins used to reach the amount i
Transition: min(dp[i], dp[i-coin] + 1)
    - Select the min between:
        - dp[i], represents best solution found so far using other coins with the SAME amount
        - dp[i-coin] + 1, represents best solution for the remaining amount after USING the coin (adding +1 uses the coin)
            * SIMPLIFIED: After using the coin at the current amount, what was the best PREVIOUS solution for the remaining amount? *

Base cases:
1. dp[0] = 0, for an amount of 0, we USE 0 coins
 
Returns: -1 if its not possible, else dp[amount] which is the target amount
"""
class BottomUpSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP state: coinsUsed[i], represents the amount of coins used at amount i
            # Value is infinity since its impossible to actually reach that value
            # Length is amount+1 so that we can account for the base case
        coinsUsed = [float("inf")] * (amount+1)
        
        # Base case: For an amount of 0, use 0 coins
        coinsUsed[0] = 0

        # Recurrence relation: At each amount i, find number of coins used to reach the amount
        for i in range(1, amount+1):

            # Check the amount after trying each coin
            for coin in coins:
                amountAfterUsingCoin = i-coin

                # Check if the current coin can contribute to the amount
                    # If positive number, was able to contribute 
                    # If negative number, coin goes over limit of amount
                if amountAfterUsingCoin >= 0:
                    # Transition: Check min between current amount of remaining amount
                        # coinsUsed[i], represents best solution found so far for SAME amount after trying other coins
                        # coinsUsed[i-coin], represents best solution from REMAINDER amount after using current coin
                        # +1, is using the current coin to add to the amount of coins used
                    coinsUsed[i] = min(coinsUsed[i], coinsUsed[amountAfterUsingCoin] + 1)
        
        # Return the best possibilities for target amount if it was possible
        return coinsUsed[amount] if coinsUsed[amount] != float("inf") else -1

class TopDownSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        # State: amt represents the amount we are trying to achieve with current coin selection
        def change(amt):
            # Base case 1: The best possible solution for the current amount has already been found
            if amt in memo:
                return memo[amt]
            
            # Base case 2: If amount is 0, then we don't have to use a coin
            if amt == 0:
                return 0
            
            # Base case 3: If amount is negative, then the current coin used is not possible
            if amt < 0:
                return -1
            
            # Indicates the min count of used coins for the current amount
                # Infinity b/c it may not be possible
            minCoinsUsed = float('inf')

            # Explore each coin as deep as possible
            for coin in coins:
                # Try to find change for current coin
                remainderAmount = amt-coin
                currentCoinUsages = change(remainderAmount)

                # Check that the coin was able to contribute to the remainder amount
                if currentCoinUsages >= 0:
                    # Transition: Find the min between previous solutions of coins used and current coin usage
                        # minCoinsUsed -> best solution for CURRENT amount using PREVIOUS coin options (for loop)
                        # currentCoinUsage -> best solution from REMAINDER amount using CURRENT coin option
                        # currentCoinUsage+1 -> using the current coin along with best solution from remainder amount
                    minCoinsUsed = min(minCoinsUsed, currentCoinUsages + 1)

            # Return min coins if it was possible else -1
            memo[amt] = minCoinsUsed if minCoinsUsed != float('inf') else -1
            return memo[amt]
        
        return change(amount)
                    

class BruteForceDFS:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case: if amount is 0, we need 0 coins
        if amount == 0:
            return 0
        
        # Initialize result with infinity
        self.min_coins = float('inf')
        
        def dfs(remaining, coin_count):
            # Base cases
            if remaining == 0:
                # Found a valid combination
                self.min_coins = min(self.min_coins, coin_count)
                return
            
            if remaining < 0:
                # Invalid path
                return
            
            # If we've already found a better solution, prune this branch
            if coin_count >= self.min_coins:
                return
            
            # Try using each coin
            for coin in coins:
                # Inclusion: Subtracting the coin from remainder and adding the coin to the count
                # Backtracking: Try the current coin option as deep as possible
                # Exclusion: When current option is explored fully, the stack pops and resets the parameter to previous states
                dfs(remaining - coin, coin_count + 1)
        
        # Start DFS
        dfs(amount, 0)
        
        # Return result, or -1 if no solution was found
        return self.min_coins if self.min_coins != float('inf') else -1
