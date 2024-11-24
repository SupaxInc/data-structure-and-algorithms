class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLefts = []
        maxRights = [0] * n
        total = 0

        # Get all the left max heights for the CURRENT index
        # Begin at 0, we are comparing the tallest height to left of current index (currently the left of index 0 has no height)
        # **Allows us to check if the current index we are on could be filled with rain water trapped between the heights to left and right.**
        maxLeft = 0 
        for i in range(n):
            maxLefts.append(maxLeft)
            maxLeft = max(maxLeft, height[i])
        
        # Get all the right max heights for the CURRENT index
        # Begin at 0 at the end of array, the right of the last index has no height
        maxRight = maxRights[-1]
        for i in range(n-1, -1, -1):
            maxRights[i] = maxRight
            maxRight = max(maxRight, height[i])
        
        # Get the units per height
        for i in range(n):
            # Similar to container with most water, we need to get the min of the max heights, so water does not spill over
            # Subtract it by current height to see how much water can be trapped between the two max heights to left and right
            units = min(maxLefts[i], maxRights[i]) - height[i]

            # If units are negative then it means the current height is taller than the max heights to left and right
            if units > 0:
                total += units
        
        return total
    
class MostOptimizedSolution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0

        maxL, maxR = height[0], height[-1]
        total = 0

        l, r = 0, len(height)-1

        while l < r:
            # Find out which heights to left or right of current index is taller
            # Use the smaller height to calculate with current height
                # Similar to container most water, use the smaller height so water does not overflow
            if maxL < maxR:
                # Move left pointer by 1 instantly since we already have the previous height saved as maxL
                # This allows us to use l as the current index and calculate it against the max height to left
                l += 1 # l will now be current index (current height)

                # Get max of current height and the height to left to prevent NEGATIVE units
                    # If negative, it means water could not fill the current height since the current height is taller
                maxL = max(maxL, height[l])
                
                # Essentially subtracting the highest height to the left to current height
                    # If the current height is taller from previous max calculation then it will total to just 0
                    # preventing a negative unit answer.
                total += maxL - height[l]
            else:
                r -= 1

                maxR = max(maxR, height[r])
                total += maxR - height[r]
        
        return total