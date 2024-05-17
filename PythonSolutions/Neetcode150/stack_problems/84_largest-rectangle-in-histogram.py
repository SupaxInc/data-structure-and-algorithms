class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Pair of (index, height)

        for currIdx, currHeight in enumerate(heights):
            newStart = currIdx # Keep track of what the new index might be

            # Maintain increasing order
                # Check if current height is less than top of stack (prev max height)
            while stack and currHeight < stack[-1][1]:
                prevMaxHeightIdx, prevMaxHeight = stack.pop()
                # The width of the popped height could have possibly increased
                    # Due to the nature of increasing order
                    # This means that the height in front was larger so it could extend the rectangle
                maxArea = max(maxArea, prevMaxHeight * (currIdx - prevMaxHeightIdx))

                # Since the stack was popped, we extend the new added height
                    # This means that it can extend since the previous heights were larger
                newStart = prevMaxHeightIdx
            
            # Append the possible new starting index
            stack.append((newStart, currHeight))
        
        # There may be heights still in the stack
        for idx, height in stack:
            # So we calculate the area based on the length of heights
                # This means that the rest of the other heights was just extended
                    # Unless it was the last height added
            maxArea = max(maxArea, height * (len(heights) - idx))
        
        return maxArea
