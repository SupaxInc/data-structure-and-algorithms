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
        nums.sort() # Sort the numbers to find duplicate values as neighbours

        # First loop to look for 1st number
        for i in range(0, len(nums)):
            # Check the left neighbour of the 1st index for duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            # Second loop to look for 2nd and 3rd number
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # Move pointers depending if the total is greater than or less than the target
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # If the target is currently at 0, we can move the left or right pointers. Doesn't matter which.
                    l += 1

                    # Check for left neighbour duplicates for the 2nd index.
                    # Loop until it's no longer a duplicate
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                    # Do not need to check for neighbour duplicates for 3rd index
                    # Since we move the right pointer based on if the total is too big
                    # If we move the right pointer and get the same value then it'll just move it again because total is still big
                    # This is the benefits of two pointer, the 2nd pointer will have the larger value preventing a 0
        
        return res
                