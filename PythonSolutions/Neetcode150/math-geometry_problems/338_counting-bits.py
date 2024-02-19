class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        MSB = 1 # The offset
        dp[0] = 0 # Base case, n = 0 will always be 0 1's

        for i in range(1, len(dp)):
            # When i equals MSB * 2, it means i is itself a power of 2, and we need to update MSB to the next power of 2
            if MSB * 2 == i:
                MSB *= 2
            dp[i] = 1 + dp[i - MSB]
        
        return dp