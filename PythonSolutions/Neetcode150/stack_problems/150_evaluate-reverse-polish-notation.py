class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # If you see a number, push it to the stack
            # Can't use isdigit() as it only checks from 0-9
            if token not in "+-*/":
                stack.append(int(token)) # Convert token string to int
            else:
                # In postfix notation, the LAST number added to stack is the right operand
                right = stack.pop()
                # The second last number added to stack is the left operand
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    # Dividing left and right would create a floating point number
                    # We convert it to an int so that it truncates to 0 (e.g -3.5 to -3)
                    # Using // would not work here as it truncates to -Infinity (e.g -3.5 to -4)
                    stack.append(int(left / right))
                    
        # Final result is the last operation added to stack
        return stack[-1]