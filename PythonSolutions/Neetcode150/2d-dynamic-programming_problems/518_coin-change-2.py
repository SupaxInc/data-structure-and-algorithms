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