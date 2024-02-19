class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n: # Iterate until we shift all bits and it becomes 0
            if n & 1 == 1: # Check to see if the right-most bit is a 1
                count += 1
            n = n >> 1 # Shift bit's by 1 to remove right most bit
        
        return count