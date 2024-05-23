class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    # Timestamps that are set will be strictly ascending
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeMap[key] or not key:
            return ""
        
        lo, hi = 0, len(self.timeMap[key]) - 1
        # Track for the current value in the case we don't find a time stamp match
        curr_value = ""

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            mid_value = self.timeMap[key][mid][0]
            mid_timestamp = self.timeMap[key][mid][1]
            
            # To find the largest timestamp, continuously search on the right side
            # until we find the largest time stamp or it equals the target timestamp
            if mid_timestamp <= timestamp:
                curr_value = mid_value
                lo = mid + 1
            # If its greater than the time stamp then search on the left
            else:
                hi = mid - 1
        
        return curr_value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)