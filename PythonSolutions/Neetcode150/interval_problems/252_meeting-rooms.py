"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start) # Sort by start time in ASC order

        for i in range(1, len(intervals)):
            # If the current start time is less than the previous end time then theres overlap
            # Since the new class starts before the previous class ended
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True