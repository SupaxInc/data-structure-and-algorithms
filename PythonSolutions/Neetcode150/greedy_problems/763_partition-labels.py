class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        
        lastFound = {char: idx for idx, char in enumerate(s)}
        res = []
        
        start, end = 0, 0
        for i in range(len(s)):
            # Greedy choice: Extend the end of partition as far as possible
            end = max(end, lastFound[s[i]])

            # Global optimum is reached since partition the size of partition is
                # as large as possible without splitting characters across different partitions
            if i == end:
                res.append(end + 1 - start)
                start = i + 1

        return res