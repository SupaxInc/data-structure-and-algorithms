# Sorting

1. **Sort by End Time**: When the goal is to find the maximum number of non-overlapping intervals or to minimize removals to avoid overlap, it's typically best to sort by end time. This approach is based on the greedy algorithm principle that by always selecting the interval that ends the earliest (and doesn't overlap with previously selected intervals), you maximize the remaining available time for future intervals. Sorting by the end time ensures that you are always making the optimal choice at each step in terms of leaving as much room as possible for subsequent intervals.
    - **Example**: In a problem where you need to attend as many meetings as possible without any overlap, sorting by end time helps in selecting the meeting that frees up the calendar the soonest, thus maximizing the possibility of attending more meetings.
2. **Sort by Start Time**: Sorting by start time is useful when you need to process intervals based on when they begin, such as merging overlapping intervals. Here, you want to look at intervals from the beginning of their start times, and if an interval overlaps with the previous one (which you know by comparing the start of the current interval with the end of the previous one), you can merge them accordingly.
    - **Example**: In problems where you're merging all overlapping intervals into the fewest number of combined intervals, sorting by start time helps organize the intervals in a sequential order, making it easier to determine overlaps and to merge accordingly.

## **Choosing the Sort Criteria**:

- If the problem is about **maximizing compatibility** (i.e., fitting the most intervals without overlaps), sorting by the **end time** is typically the right choice.
- If the problem involves **managing or modifying intervals based on their sequence or overlaps** (like merging or covering intervals with the fewest resources), sorting by the **start time** might be more appropriate.

# Common Template Codes

## **1. Sorting Intervals**

Most interval problems can be simplified by sorting the intervals, usually by start or end time depending on the problem requirement:

```python
pythonCopy code
# Sort by start time
intervals.sort(key=lambda x: x[0])

# Sort by end time
intervals.sort(key=lambda x: x[1])
```

## **2. Merging Intervals**

For merging overlapping intervals, you first sort the intervals by start time, then merge where necessary:

```python
pythonCopy code
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by the start of each interval
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        if current[0] <= last_merged[1]:  # There is an overlap
            # Merge the current interval with the last one in the list
            merged[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else: # No overlap
            merged.append(current)

    return merged
```

## **3. Finding Non-overlapping Intervals**

To find the maximum number of non-overlapping intervals, sort by the end time and then select intervals greedily:

```python
pythonCopy code
def find_non_overlapping(intervals):
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    count = 1
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            count += 1
            end = intervals[i][1]

    return count

```

## **4. Insert Interval**

For inserting an interval into a list of non-overlapping intervals and then merging if necessary:

```python
pythonCopy code
def insert_interval(intervals, new_interval):
    results = []
    i = 0

   # Add intervals at the beginning where there are NO overlaps
            # No overlaps in beginning: Current interval end time is less than the start time of new interval
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        results.append(intervals[i])
        i += 1

    # Merge intervals where there are overlaps
            # Overlaps: Current interval start time is less than or equal to end time of new interval
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        i += 1
    results.append(new_interval)

    # Add the rest of the intervals, after beginning and merged overla
    while i < len(intervals):
        results.append(intervals[i])
        i += 1

    return results

```

## **5. Interval Intersections**

To find intersections of two lists of intervals:

```python
def interval_intersection(A, B):
    i, j = 0, 0
    result = []

    while i < len(A) and j < len(B):
        # Check if A[i] overlaps B[j]
        # Start point of the overlap
        start_max = max(A[i][0], B[j][0])
        # End point of the overlap
        end_min = min(A[i][1], B[j][1])

        if start_max <= end_min:
            result.append([start_max, end_min])

        # Remove the interval with the smallest endpoint
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return result
```