from collections import defaultdict
from typing import List

class MostReadableSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Create alphabet sized count array
            count = [0] * 26
            
            # For each character in string find what 0-index it lands on based on unicode (e.g. 97(a)-99(c) = 2)
            for char in s:
                idx = ord(char) - ord('a')
                count[idx] += 1
            
            # Convert the count array to a tuple key = (0, 2, 2, ...)
                # Or could use join as well BUT tuple = O(1), join() = O(26)
                # countStr = ','.join([str(x) for x in count])
            groups[tuple(count)].append(s)

        # List each value as a group creating a 2D array
        return list(groups.values())

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
    
class LessOptimizedSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        res = defaultdict(list)

        for string in strs:
            sortedStr = ''.join(sorted(string, key=str.lower))

            res[sortedStr].append(string)
        
        return list(res.values())


class MoreOptimizedSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        # defaultdict removes the need to check if a key exists
        res = defaultdict(list) 

        for string in strs: # O(n)
            alphabetCount = [0] * 26 # O(26)
            asciiPos = ord("a") # Value is 97
            for char in string: # O(m)
                # Subtracting current char ascii code with 97 will give the 0-index based in the char count array
                alphabetCount[ord(char) - asciiPos] += 1
            
            # Turn into tuple since we can't directly join an integer array to a string
            # default dict allowed us to just append even though we didn't initialize an array before
            res[tuple(alphabetCount)].append(string)
        
        return list(res.values())