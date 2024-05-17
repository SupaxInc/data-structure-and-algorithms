class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_n, closed_n, path):
            # Append path if the amount of open and closed parentheses are equal
            if closed_n == open_n == n:
                res.append(path)
                return
            
            # Inclusion choice: Add an open bracket 
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
            
            # Exclusion choice: Don't add an open bracket
                # Add closing brackets instead when there are less amounts of open brackets
            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
        
        backtrack(0, 0, "")
        return res