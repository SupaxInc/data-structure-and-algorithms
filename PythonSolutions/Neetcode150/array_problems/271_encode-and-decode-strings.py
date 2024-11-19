class OptimizedSolution:

    def encode(self, strs: List[str]) -> str:
        # The encoding scheme is "len(s)#s" and it works b/c it prevents from having to escape a character
        # If another same scheme used in the original string, its fine since we are encoding and the scheme will always be first
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Get the index of # so we can slice to get the length
            j = s.find('#', i)
            # Find() could return -1 if we can't find a string with "#"
            if j != -1:
                # The length could be up to 200 so we need to slice
                    # Find the length by slicing up to the #
                length = int(s[i:j])
                # j+1: The decoded string would begin after the "#" 
                # j+1+length: String ends with the length + the delimiters we have
                decodedString = s[j+1:j+1+length]
                decoded.append(decodedString)

                # Move the index to decode next character
                i = j + 1 + length
        
        return decoded

class LessOptimalSolution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        # Create the encode delimiter of "len(str)#"
        
        for string in strs:
            # Created parts of the new encoded string
            parts = []
            # 1st part is the length of string
            parts.append(str(len(string)))
            # 2nd part is delimiter
            parts.append("#")
            # 3rd part is the string itself
            parts.append(string)

            # "".join() is more efficient than string concatenation 
                # It creates a new string leading to O(n^2) unlike join()
            # **This is less optimal as it string concatenates for each part which could become O(n^2)**
            encodedString += "".join(parts)
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Get the index of # so we can slice to get the length
            j = s.find('#', i)
            # Find() could return -1 if we can't find a string with "#"
            if j != -1:
                # The length could be up to 200 so we need to slice
                    # Find the length by slicing up to the #
                length = int(s[i:j])
                # j+1: The decoded string would begin after the "#" 
                # j+1+length: String ends with the length + the delimiters we have
                decodedString = s[j+1:j+1+length]
                decoded.append(decodedString)

                # Move the index to decode next character
                i = j + 1 + length
        
        return decoded