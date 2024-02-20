class MySolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        countStrs = {}
        
        for string in strs: # O(n)
            # Create an array of 26 0's to denote the alphabet
            # It is a string since we can't join integers in an array in python
            alphabetCount = ['0'] * 26
            # Get the position of ascii character 'a' to help find the position for other chars
            asciiPos = ord("a")
            for char in string: # O(m) -> O(n * m)
                # Get the ascii pos of current char and subtract it by position of a to get 0 index
                # Need to convert the calculation to int then back to str
                alphabetCount[ord(char) - asciiPos] = str(int(alphabetCount[ord(char) - asciiPos]) + 1)

            # The join method does not allow to join integers so we had to convert a lot in the for loop
            alphabetCountStr = ",".join(alphabetCount)
            
            # Check if the character exists in our hashmap, append if it does
            if alphabetCountStr in countStrs:
                countStrs[alphabetCountStr].append(string)
            else:
                countStrs[alphabetCountStr] = [string]
        
        return list(countStrs.values())

class MoreOptimizedSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        # defaultdict removes the need to check if a key exists
        res = defaultdict(list) 

        for string in strs:
            alphabetCount = [0] * 26
            asciiPos = ord("a")
            for char in string:
                alphabetCount[ord(char) - asciiPos] += 1
            
            # Turn into tuple since we can't directly join an integer array to a string
            # default dict allowed us to just append even though we didn't initialize an array before
            res[tuple(alphabetCount)].append(string)
        
        return list(res.values())