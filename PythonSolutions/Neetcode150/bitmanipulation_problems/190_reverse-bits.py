class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(0, 32):
            res = res << 1 # Shift result array to the left
            # Grab the right-most bit from n and add it to result array 
            # The earlier shift allows us to replace the right most bit of result to the opposite of the bit from n
            res += n & 1
            # Shift n to the right to remove the right-most bit 
            # Allows us to grab the next right-most bit in next iteration until we exhaust all bits from n
            n = n >> 1 
        
        return res