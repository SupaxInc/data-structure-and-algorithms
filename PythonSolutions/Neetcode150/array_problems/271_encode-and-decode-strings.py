class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        # Create the encode delimiter of "len(str)#"
        # "".join() is much more efficient than string concatenation since it creates a new string leading to O(n^2)
        for string in strs:
            parts = []
            parts.append(str(len(string)))
            parts.append("#")
            parts.append(string)
            encodedString += "".join(parts)
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Get the index of #, cleaner than if statements
            j = s.find('#', i)
            # Find() could return -1 if we can't find a string with "#"
            if j != -1:
                # The length could be up to 200 so we need to slice
                length = int(s[i:j])
                # The decoded string would begin after the "#" and ends with the length + the delimiters we have
                decodedString = s[j+1:j+1+length]
                decoded.append(decodedString)
                # Move the index after the decoded characters
                i = j + 1 + length
        
        return decoded