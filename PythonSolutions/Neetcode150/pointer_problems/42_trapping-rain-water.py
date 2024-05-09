class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLefts = [0] # Add a 0 for beginning of array
        maxRights = [0] * (n + 1) # Add a 0 for end of array
        total = 0

        # Get all the left max heights for the CURRENT index
        maxLeft = maxLefts[0]
        for i in range(n):
            maxLeft = max(maxLeft, height[i])
            maxLefts.append(maxLeft)
        
        # Get all the right max heights for the CURRENT index
        maxRight = maxRights[-1]
        for i in range(n-1, -1, -1):
            maxRight = max(maxRight, height[i])
            maxRights[i] = maxRight
        
        # Get the units per height
        for i in range(n):
            # Similar to container with most water, we need to get the min of the max heights
                # This is so that the water does not spill over
            units = min(maxLefts[i], maxRights[i]) - height[i] # Formula to get units
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