class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Low and high pointer will be the range of 1 to max P
        # This creates a K array to iterate through 
            # If max = 8 -> [1, 2, 3, 4, 5, 6, 7, 8]
        lo, hi = 1, max(piles)

        # Current min would be max value inside piles.
            # Allows Koko to eat all the piles within the hour limit
        minK = hi

        while lo <= hi:
            # The K value is how much Koko can eat in an hour
            midK = lo + ((hi - lo) // 2)
            hours = 0

            for pile in piles:
                # Calculate how long it takes Koko to eat the pile based on the banana (K) per hour
                # Ceiling the value is needed to round up to the hour
                hours += math.ceil(pile/midK)
            
            # If Koko can eat the piles within the hour limit before the guards come, it will be new min
                # Lower the higher boundary to try and find a smaller min
            if hours <= h:
                minK = min(minK, midK)
                hi = midK - 1
            # If Koko can't eat the piles within the hour limit, then go higher in bananas (K) per hour
            else:
                lo = midK + 1
    
        return minK
