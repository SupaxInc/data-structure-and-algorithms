class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to keep the result within the bounds of a 32-bit integer
        mask = 0xFFFFFFFF
        
        # Repeat the operation until there is no carry left
        while b != 0:
            # Calculate sum without carrying
            sum_without_carry = a ^ b
            # Calculate the carry, and shift left by 1 to add it in the next step
            carry = (a & b) << 1
            
            # Update a and b for the next iteration
            # Apply the mask to simulate 32-bit overflow behavior
            a = sum_without_carry & mask
            b = carry & mask
        
        # If the resulting a is beyond the 32-bit signed integer range, adjust it
        # This adjustment is needed because Python handles integers with more than 32 bits
        if a > 0x7FFFFFFF:  # This checks if a is greater than the maximum 32-bit signed integer
            return ~(a ^ mask)  # This operation converts a into its two's complement within 32 bits
        else:
            return a