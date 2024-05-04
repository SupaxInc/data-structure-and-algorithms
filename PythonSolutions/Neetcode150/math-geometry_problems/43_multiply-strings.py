class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Create an array to hold the result of each digit multiplication
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Fill the result array by multiplying each digit of num1 by each digit of num2
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # p1 and p2 are positions in the result array
                p1, p2 = i + j, i + j + 1
                # Add mul to the position determined by p2
                sum_ = mul + result[p2]
                
                # Place the current digit and carry over to the next digit left
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        
        # Build the final result string, skipping any initial zeros
        result_str = ''.join(str(x) for x in result)
        return result_str.lstrip('0')