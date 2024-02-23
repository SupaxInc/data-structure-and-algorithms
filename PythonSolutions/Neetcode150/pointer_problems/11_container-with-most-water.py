class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l <= r:
            # Get min height so water doesn't overflow
            area = min(height[l], height[r]) * (r-l)
            maxArea = max(maxArea, area)

            # If the height on the left is smaller than find a new height for left
            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        
        return maxArea