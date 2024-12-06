class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        # Stack stores tuples of (index, height)
        # We use this to track increasing heights and their starting positions
        stack = []

        for currIdx, currHeight in enumerate(heights):
            # Start position for current height, may change if we pop items
            newStart = currIdx

            # If current height is smaller than the previous height in our stack,
            # we've found the right boundary for the previous rectangles.
            # We must pop and calculate their areas since they can't extend further right.
            while stack and currHeight < stack[-1][1]:
                # Pop the previous largest height (monotonic increasing stack)
                prevIdx, prevHeight = stack.pop()
                
                # Calculate area for the rectangle we're popping:
                # Width = current position - start position of prev height
                # Height = height of rectangle we're popping
                maxArea = max(maxArea, prevHeight * (currIdx - prevIdx))

                # The current height can extend left to where the popped rectangle started
                # This is because all heights in between the current index and the previous index were taller
                # Allows us to extend rectangle from largest previous height position to the current smaller height position
                newStart = prevIdx
            
            # Add current height to stack, using the leftmost possible starting point
            stack.append((newStart, currHeight))
        
        # Process remaining rectangles in stack
        # Since we maintain a monotonic increasing stack, these rectangles
        # represent heights that can extend all the way to the end of the array
        # because the heights before them were taller thus allowing them to extend their rectangle all the way to the tallest height before them
        for idx, height in stack:
            # Width = total length - start position
            maxArea = max(maxArea, height * (len(heights) - idx))
        
        return maxArea
