from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Create a sorted search space of (1... max of piles)
        lo, hi = 1, max(piles)
        # The most CURRENT min eating speed would be the highest max of the pile
        minK = hi

        while lo <= hi:
            # Binary search the middle eating speed to divide and conquer
            midK = lo + (hi - lo) // 2

            # The hour amount we have used to eat all the piles based on midK
            currH = 0
            # piles / eating speed = piles can eat / hour
            for p in piles:
                # Need to ceil in the event that we eat a portion of the pile in an hour or eat all of it
                    # e.g. 5/9 = 0.55 -> round to 1 since we are counting by hour
                currH += ceil(p / midK)
            
            # If we were able to eat all piles in the hour limit then create new min
            if currH <= h:
                minK = min(minK, midK)
                hi = midK - 1
            else:
                # If we couldn't eat the piles in the certain K, then check for a higher K limit
                lo = midK + 1
        
        return minK