class BruteForceSolution:
    def checkValidString(self, s: str) -> bool:
        # Check if the order of paranthesis is valid
        def isValid(newS):
            balance = 0
            for char in newS:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1

                # At any point if there are unclosed brackets, it is no longer valid
                if balance < 0:
                    return False
            
            return balance == 0

        def solve(idx, currentS):
            if idx == len(s):
                return isValid(currentS)
            
            # Explore all combinations when an asterisk is found
            if s[idx] == '*':
                return (solve(idx + 1, currentS + '(') or
                        solve(idx + 1, currentS + '') or
                        solve(idx + 1, currentS + ')'))
            else:
                return solve(idx + 1, currentS + s[idx])
        
        return solve(0, '')