class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary of closed brackets that matches with open brackets
        bracketMap = { ')': '(', '}': '{', ']': '[' }

        stack = []

        for bracket in s:
            if bracket not in bracketMap:
                stack.append(bracket)
                continue
            # If the stack is empty or if the end of the stack (what will be popped) does not equal its complementary bracket partner
            elif not stack or stack[-1] != bracketMap[bracket]:
                return False
            
            stack.pop()
        
        return not stack