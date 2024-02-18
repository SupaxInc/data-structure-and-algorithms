class BottomUpSolution:
    def minCostClimbingStairs(cost):
        n = len(cost)
        dp = [0] * (n + 1)  # +1 to accommodate reaching the top past the last step
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # Compare the last two steps to decide the minimum cost to reach the top
        return min(dp[n-1], dp[n-2])