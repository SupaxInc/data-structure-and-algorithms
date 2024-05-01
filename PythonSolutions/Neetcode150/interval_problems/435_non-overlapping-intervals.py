class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end times to find which intervals ends the earliest
        intervals.sort(key=lambda x:x[1])

        count = 0
        prevEnd = intervals[0][1]

        for currStart, currEnd in intervals[1:]:
            # Greedy choice: Always select the earliest interval over the interval that ends later
                # So if there's an overlap were removing the interval that is longer
                    # This maximizes less amount of overlaps for future intervals
                # Essentially allowing us to free up our "calendar" a lot more
            if currStart < prevEnd:
                # Theres an overlap, so remove this current longer interval
                count += 1
            else: # No overlap when currStart >= prevEnd 
                # Make the previous end the current interval end so we can compare the end in next iteration
                prevEnd = currEnd 
        
        return count