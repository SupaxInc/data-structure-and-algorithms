from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    mySet = set()

    for n in nums:
        if n in mySet:
            return True
        
        mySet.add(n)
    
    return False

print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))