import heapq

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Initialize a heap.
    # The heap keeps track of the earliest end time of all allocated rooms.
    heap = []

    # Sort the intervals by their start time.
    intervals.sort(key=lambda x: x[0])

    # Add the first meeting's end time to the heap
    heapq.heappush(heap, intervals[0][1])

    # Iterate over the remaining intervals
    for i in intervals[1:]:
        # If the room due to free up the earliest is free, assign that room to this meeting.
        if heap[0] <= i[0]:
            heapq.heappop(heap)
        
        # If a new room is needed, or after freeing up, add the current meeting's end time to the heap.
        heapq.heappush(heap, i[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(heap)

# Example usage:
intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))  # Output: 2