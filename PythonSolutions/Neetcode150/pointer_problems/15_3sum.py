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
        nums.sort()

        for i in range(len(nums)-2):
            # Check duplicates for index 0
            # If we don't it may result in a duplicate unique triplet result set
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
                    l += 1

                    # Check duplicates for index 1
                    # Loop the next left pointer until we do not find an answer with duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    # No need to check for duplicates for index 2
                    # 3rd index is taken care of because at this point the left pointer has moved enough
                    # Which means moving the right pointer to the same value will make the total too large
                    # So if a duplicate is hit for the 3rd index, it wont matter as the total will still be too large.
            
        return res



                