class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary of closed brackets that matches with open brackets
        bracketMap = { ')': '(', '}': '{', ']': '[' }

        stack = [] # Stack to add open brackets

        for currBracket in s:
            # If its not a closed bracket then append to stack
                # Continue the current iteration so we don't pop the stack (remove an open bracket)
            if currBracket not in bracketMap:
                stack.append(currBracket)
                continue
            # It is not a valid parenthesis if:
                # The stack is empty (this means no open bracket was added to stack to match a closing bracket)
                # The end of the stack (what will be popped) does not equal its complementary bracket partner
            elif not stack or stack[-1] != bracketMap[currBracket]:
                return False
            
            # Pop the stack, this means we were able to match it with its complementary bracket
            stack.pop()
        
        return not stack