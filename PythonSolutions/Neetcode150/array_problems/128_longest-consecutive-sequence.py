class SomewhatOptimalSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums: # O(n)
            length = 0
            # Check if there's no left neighbour (start of sequence)
            if (num - 1) not in numSet: 
                length += 1
                # Check if there are further consecutive sequences by checking if the next number is in the set

                # While loop does not go through all numbers twice like a nested for loop, only goes through once
                # so it would be O(n) + O(n) = O(2n) = O(n)
                while (num + length) in numSet:
                    length += 1

            longest = max(length, longest)

        return longest 

class MostOptimalSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0

        # **Iterate through numbers in set instead of list to avoid duplicates**
        # E.g. [1,2,2,3] -> [1,2,3], only checks 2 once
        for num in numSet:
            length = 0

            # Check if there's no left neighbour (start of sequence)
            if num - 1 not in numSet:
                length += 1

                # Check if there are further consecutive sequences by checking if the next number sequence is in the set
                # E.g. 1 + 1 = 2, 1 + 2 = 3, 1 + 3 = 4, etc
                while num + length in numSet:
                    length += 1
                
                maxLength = max(maxLength, length)
        
        return maxLength
