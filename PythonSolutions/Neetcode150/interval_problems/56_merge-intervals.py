class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # Sort the start time of intervals
        intervals.sort(key=lambda interval: interval[0])

        res = [intervals[0]]

        # Skip first interval
        for i in range(1, len(intervals)):
            prev = res[-1]
            curr = intervals[i]
            if curr[0] <= prev[1]: # Overlap
                # Merge by finding the max between prev and current last
                    # No need to change start time, 
                    # since start time is sorted, prev start time is always less
                prev[1] = max(prev[1], curr[1])
            else: # No overlap
                res.append(curr)
                
        return res