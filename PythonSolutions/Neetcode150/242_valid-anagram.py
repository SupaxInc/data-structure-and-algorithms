class Solution:
    def countLetters(self, s: str) -> dict:
        letterMap = {}

        for char in s:
            if char not in letterMap:
                letterMap[char] = 1
            else:
                letterMap[char] += 1
        
        return letterMap

    def isAnagram(self, s: str, t: str) -> bool:
        sMap = self.countLetters(s)
        tMap = self.countLetters(t)

        for key in sMap:
            if sMap[key] != tMap[key]:
                return False
        
        return True
    
