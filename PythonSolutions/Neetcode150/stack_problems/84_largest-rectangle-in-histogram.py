class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        # Stack stores tuples of (index, height)
        # We use this to track increasing heights and their starting positions
        stack = []

        for currIdx, currHeight in enumerate(heights):
            # Start position for current height, may change if we pop items
            newStart = currIdx

            # When we find a smaller height, we need to calculate areas of all taller rectangles
            # that must end at this position
            while stack and currHeight < stack[-1][1]:
                prevIdx, prevHeight = stack.pop()
                
                # Calculate area for the rectangle we're popping:
                # Width = current position - start position of prev height
                # Height = height of rectangle we're popping
                maxArea = max(maxArea, prevHeight * (currIdx - prevIdx))

                # The current height can extend left to where the popped rectangle started
                # This is because all heights in between were taller
                newStart = prevIdx
            
            # Add current height to stack, using the leftmost possible starting point
            stack.append((newStart, currHeight))
        
        # Process remaining rectangles in stack
        # These are rectangles that never found a smaller height to their right,
        # so they extend all the way to the end
        for idx, height in stack:
            # Width = total length - start position
            maxArea = max(maxArea, height * (len(heights) - idx))
        
        return maxArea
