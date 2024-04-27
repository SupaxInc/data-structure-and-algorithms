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

class MemoizedSolution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
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
            if (idx, currentS) in memo:
                return memo[(idx, currentS)]
            if idx == len(s):
                return isValid(currentS)
            
            # Explore all combinations when an asterisk is found
            if s[idx] == '*':
                result = (solve(idx + 1, currentS + '(') or
                        solve(idx + 1, currentS + '') or
                        solve(idx + 1, currentS + ')'))
            else:
                result = solve(idx + 1, currentS + s[idx])
                
            memo[(idx, currentS)] = result
            return result
        return solve(0, '')
    
class BottomUpSolution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # Create a DP table with (n+1) x (n+1) dimensions
        # dp[i][j] means whether it's possible to have exactly j unmatched '(' after processing i characters.
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        # Initially, no characters processed and no unmatched '(' is definitely possible
        dp[0][0] = True

        # Process each character in the string
        for i in range(1, n + 1):
            char = s[i-1]
            for j in range(n + 1):  # Try every possible count of unmatched '(' up to n
                if char == '(':
                    # A '(' increases the count of unmatched '(' by 1, so check from j-1 (if j-1 >= 0)
                    if j > 0:
                        dp[i][j] = dp[i-1][j-1]
                elif char == ')':
                    # A ')' decreases the count of unmatched '(', so we check from j+1
                    if j < n:
                        dp[i][j] = dp[i-1][j+1]
                else:  # char == '*'
                    # If '*' is treated as '(': need to have had one less unmatched '(' before this character
                    if j > 0:
                        dp[i][j] = dp[i][j] or dp[i-1][j-1]
                    # If '*' is treated as ')': can have one more unmatched '(' before this character
                    if j < n:
                        dp[i][j] = dp[i][j] or dp[i-1][j+1]
                    # If '*' is treated as nothing: the count of unmatched '(' does not change
                    dp[i][j] = dp[i][j] or dp[i-1][j]

        # Check the bottom right value in the DP table; if dp[n][0] is True, it means we can balance all '(' and ')'
        return dp[n][0]
    
class GreedySolution:
    def checkValidString(self, s: str) -> bool:
        # Low represents MINIMUM possible of umatched opening parentheses
        # High represents MAXIMUM possible of unmatching opening parentheses
        low = high = 0
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                # This is where low acts as min possible of unmatched openings
                low -= 1  # worst case, '*' acts as ')'
                # This is where high acts as max possible of unmatched openings
                high += 1  # best case, '*' acts as '('
            
            # Ignore excessive closing parenthesis to find more valid possibilities
                # It is an assumption that '*' will provide balance
            if low < 0: 
                low = 0
            
            # Indicates an irreversible excess closing parenthesis
                # Imagine always getting a ')', there are no longer possibilities
            if high < 0:
                return False

        # If low is 0, it indicates that we were able to balance using '*'
        return low == 0