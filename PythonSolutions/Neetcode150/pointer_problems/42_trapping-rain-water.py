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
            units = min(maxLefts[i], maxRights[i]) - height[i] # Formula to get units
            if units > 0:
                total += units
        
        return total