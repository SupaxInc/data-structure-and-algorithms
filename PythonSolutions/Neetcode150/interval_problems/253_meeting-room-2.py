class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        heap = []
        
        # Sort by start times, allows us to process the meetings in the order they begin
        intervals.sort(key=lambda x:x.start)

        # Create a room with the earliest meeting time
            # Add the end time so we can compare with new meetings if it overlaps
        heapq.heappush(heap, intervals[0].end)

        for meeting in intervals[1:]:
            # Remove the room if it does not overlap with the new meeting
            if heap[0] <= meeting.start:
                heapq.heappop(heap)
            
            # Two choices:
                # 1) If a room was removed, replace it with a new room.
                    # Makes it so that there are only one room for all meetings
                # 2) If a room was not removed, assign a new room for the new meeting
            heapq.heappush(heap, meeting.end)
        
        # The length of heap lets us know how many unique meeting rooms there are with no overlaps
        return len(heap)