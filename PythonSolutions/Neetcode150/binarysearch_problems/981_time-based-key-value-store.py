from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.timeMap = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        # There can be multiple values for 1 key in the time map
        #* Dicts are ordered in python so each key inserted to dict is added in order *
        self.timeMap[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        # No values for a key tells us there's no timemap for the key
        if not self.timeMap[key] or not key:
            return ""

        lo, hi = 0, len(self.timeMap[key]) - 1
        # Keeping track of value allows us to get values of smaller timestamps
        currValue = ""

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # mid gives us the ability to choose a value from the list of timeMap based on key
            midVal = self.timeMap[key][mid][0]
            midTimestamp = self.timeMap[key][mid][1]

            # The timestamp may not exist so we still need a way to find values for smaller time stamps.
            # Therefore, anytime there is a smaller timestamp just grab the value of that time stamp
            if midTimestamp <= timestamp:
                currValue = midVal
                # Moving to the right always allows us to get the smaller timestamp to the timestamp we are searching for
                lo = mid + 1
            else:
                hi = mid - 1

        return currValue

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)