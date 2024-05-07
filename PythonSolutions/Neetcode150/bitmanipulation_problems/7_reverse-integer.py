class Solution:
    def reverse(self, x: int) -> int:
        # Define limits for 32-bit signed integer
        MIN = -2147483648  # Minimum value for a 32-bit signed integer
        MAX = 2147483647   # Maximum value for a 32-bit signed integer

        res = 0
        while x:
            # Extract the last digit of x
            # math.fmod is used to handle negative numbers correctly as opposed to normal % mod
            digit = int(math.fmod(x, 10))
            
            # Reduce x by removing the last digit
            # Using int division to handle negative numbers correctly
            x = int(x / 10)

            # Check for overflow:
            # If res is on the boundary of overflowing on the next multiplication by 10,
            # or exactly at the boundary and the next digit would push it over.
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            
            # Check for underflow:
            # If res is on the boundary of underflowing on the next multiplication by 10,
            # or exactly at the boundary and the next digit would push it below.
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            
            # Update res by appending the digit
                # Multiply by 10 shifts the number to the left
                # E.g 3 * 10 = 30, adding the digit now appends it to the right
            res = (res * 10) + digit

        return res