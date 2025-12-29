class MoreReadableSolution:
    def isValid(s: str) -> bool:
        complement = {
            ']' :  '[',
            ')' : '(',
            '}' : '{'
        }
        stack = []
        
        for p in s:
            # If its a closing bracket
            if p in complement:
                # Option 1: Short circuit if stack is empty, it means nothing can be matched
                # Option 2: Pop the stack and compare last added bracket if it can be matched with current closing bracket
                if not stack or stack.pop() != complement[p]:
                    return False
            else:
                stack.append(p)
        
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        # We need a way to figure out which brackets are closing brackets and what open brackets it matches to
        mapDict = { '}' : '{', ']' : '[', ')' : '(' }
        stack = []

        for char in s:
            # Check if current character is a closing bracket
            if char not in mapDict:
                # Stack is important here to know what the last opening bracket was to match with the first closing bracket
                stack.append(char)
                continue # Skip iteration so we don't pop the stack of closing brackets
            
            # False if:
                # Stack is empty, therefore, the closing bracket cannot be matched to an open bracket
                # LAST opening bracket does not match the FIRST closing bracket
            elif not stack or stack[-1] != mapDict[char]:
                return False
            
            # Pop the stack when a closing bracket has been found (the elif was skipped)
            stack.pop()
        
        # Handle edge case where all opening brackets were added or not all opening brackets were matched
        return not stack