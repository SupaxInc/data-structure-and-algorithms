class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Low and high pointer will be the range of 1 to max P
        # This creates a K array to iterate through
        lo, hi = 1, max(piles)
        # The max value inside piles allows Koko to eat all the piles within the hour limit
        minK = hi

        while lo <= hi:
            # Get the middle K value between low to high
            # The K value is how much Koko can eat in an hour
            midK = lo + ((hi - lo) // 2)
            hours = 0
            for pile in piles:
                # Calculate how long it takes Koko to eat the pile based on the banana per hour
                # Ceiling the value is needed to round up to the hour
                hours += math.ceil(pile/midK)
            
            # If Koko can eat the piles within the hour limit, lets try and find a smaller K
            if hours <= h:
                minK = min(minK, midK)
                hi = midK - 1
            # If Koko can't eat the piles within the hour limit, then go higher in bananas per hour
            else:
                lo = midK + 1
    
        return minK
