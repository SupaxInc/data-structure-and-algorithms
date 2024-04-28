class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        
        # Add intervals at the beginning where there are NO overlaps
            # No overlaps in beginning: Current interval end time is less than the start time of new interval
        while (i < len(intervals) and intervals[i][1] < newInterval[0]):
            res.append(intervals[i])
            i += 1
        
        # Merge intervals where there are overlaps
            # Overlaps: Current interval start time is less than or equal to end time of new interval
        while (i < len(intervals) and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval) # Add new interval outside of while loop incase there are no overlaps

        # Add the rest of the intervals, after beginning and merged overlap
        while (i < len(intervals)):
            res.append(intervals[i])
            i += 1
        
        return res