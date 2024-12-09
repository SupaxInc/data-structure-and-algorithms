class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Low and high pointer will be the range of 1 to max amount of bananas in a pile
        # This creates a K array to iterate through to help find the most min amount of bananas to eat per hour
            # If max = 8 -> [1, 2, 3, 4, 5, 6, 7, 8]
        lo, hi = 1, max(piles)

        # Current min would be max value inside piles
        # E.g. Max is 8 bananas Koko can eat per hour, so highest starts at 8 then we can go lower
        minK = hi

        while lo <= hi:
            # The K value is how much Koko can eat in an hour, uses the new 1 to K array
            midK = lo + ((hi - lo) // 2)
            hours = 0

            for pile in piles:
                # Calculate how long it takes Koko to eat the pile based on the banana (K) per hour
                # Ceiling the value is needed to round up to the hour
                # E.g. 4/5 = 0.85 = 1, pile of 4 bananas and Koko can eat 5 in an hour
                hours += math.ceil(pile/midK)
            
            # If Koko can eat the piles within the hour limit before the guards come, it will be new min
                # Lower the higher boundary to try and find a smaller min to find a smaller amount of bananas Koko can eat in an hour
            if hours <= h:
                minK = min(minK, midK)
                hi = midK - 1
            # If Koko can't eat the piles within the hour limit, then go higher in bananas (K) eaten per hour
            else:
                lo = midK + 1
    
        return minK
