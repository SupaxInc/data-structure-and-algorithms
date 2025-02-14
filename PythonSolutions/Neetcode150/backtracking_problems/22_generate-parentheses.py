class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_b, close_b, path):
            """
                Args:
                    open_b: # of open brackets
                    close_b: # of closing brackets
                    path: current parentheses combinations
            """
            # Success found: Open and closed brackets create the correct amount of nth pairs
            if open_b == close_b == n:
                res.append(path)
                # Prune the search space when path found
                # Its impossible to find more paths when we already have the most amount of nth brackets
                return
            
            # * The first choice is always adding an open bracket to prevent false parentheses combinations * 
            # Inclusion choice 1: Add an open bracket if we haven't used all n open brackets
            if open_b < n:
                backtrack(open_b + 1, close_b, path + "(")

            # Inclusion choice 2: Add a closing bracket if we have more open than closed brackets
            if close_b < open_b:
                backtrack(open_b, close_b + 1, path + ")")
    
        backtrack(0, 0, "")
        return res
