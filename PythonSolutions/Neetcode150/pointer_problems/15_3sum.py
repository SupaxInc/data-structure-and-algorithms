from typing import List
class MySolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # First loop to use for 1st number
        for i in range(0, len(nums)):
            # Nums are sorted, so we can check for duplicates using previous number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            # Second loop to look for 2nd and 3rd number
            while l < r:
                if l-1 != i and nums[l] == nums[l-1]:
                    l += 1
                    continue
                
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
        
        return res
    
class OptimalSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sorting numbers gives us the ability to:
            # Check for duplicate neighbors
            # Allows for 2-pointer approach
        nums.sort()

        # Loop only until the last 2 index to prevent index out of range
        for i in range(len(nums)-2):
            # Check duplicates for first for loop pointer
                # E.g. For array: [-1, -1, -1, 2] → [-1, -1, 2], [-1, -1, 2]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Once the first number becomes positive in the array, we can stop as we can't create a total of 0
                # E.g. [1, 3, 4], impossible to total to 0
            if nums[i] > 0:
                break
            
            l, r = i + 1, len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # Increment left pointer so we can easily check if next number has duplicates within 2 pointer
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        # Keep moving left pointer until no more duplicates
                        l += 1

                    # No need to check for duplicates for third pointer
                        # 3rd ptr is taken care of because at this point the 2nd pointer has moved enough
                        # Which means moving the right pointer to the same value will make the total too large
            
        return res



                