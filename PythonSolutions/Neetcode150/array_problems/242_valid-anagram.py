class Solution1:
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

        # In python you can compare sets with another set easily due to built in operators
        if set(sMap.keys()) != set(tMap.keys()):
            return False
        
        for key in sMap:
            if sMap[key] != tMap[key]:
                return False
        
        return True
    
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # You can also compare hashmaps with another hashmap, it compares both keys and values
        return countS == countT

from collections import defaultdict
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        countS = defaultdict(int)
        countT = defaultdict(int)

        for char in s:
            countS[char] += 1
        
        for char in t:
            countT[char] += 1
        
        return countS == countT