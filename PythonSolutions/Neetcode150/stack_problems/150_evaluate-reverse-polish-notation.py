class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # Can't use isdigit() as it only checks from 0-9
            if token not in "+-*/":
                stack.append(int(token))
            else:
                right = stack.pop()
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
        return stack[0]