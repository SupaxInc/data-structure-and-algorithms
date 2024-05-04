class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # Base case: Any number to the power of 0 is 1
            if n == 0:
                return 1
            # Special case: x^0 is always 0 for any x except 0^0 which is not handled here
            if x == 0:
                return 0

            # Reduce the problem by squaring x and halving n
            # This reduces the multiplication operations needed
            res = helper(x * x, n // 2)
            
            # If n is odd, multiply by x once more (as n // 2 would have ignored one x due to integer division)
            # This adjusts for the floor division used when halving n
            # Example: if n is 5, n // 2 is 2, we compute x^2^2, but we need an extra multiplication by x to account for x^5
            return x * res if n % 2 else res

        # Handle negative powers by doing x^-n = 1/x^n
        # First compute the absolute power, then invert to 1/x^n if original n was negative
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
