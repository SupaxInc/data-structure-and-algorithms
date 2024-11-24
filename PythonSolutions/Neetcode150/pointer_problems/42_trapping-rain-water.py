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
            if units > 0:
                total += units
        
        return total
    
class MostOptimizedSolution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        total = 0

        while l < r:
            # The pointer with the lower max height moves toward the other pointer
                # This is so that the local height (current pointer height) has a higher chance
                # of trapping water without spilling over.
            if maxL < maxR:
                l += 1 # Moving pointers right away prevents including calculation from beginning pointers
                # Update max height seen right away
                    # This might be unintuitive b/c max height might be current position
                    # Then the total result would be 0 either way
                maxL = max(maxL, height[l]) 
                total += maxL - height[l] # Use left pointer as current height
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total += maxR - height[r] # Use right pointer as current height
        
        return total