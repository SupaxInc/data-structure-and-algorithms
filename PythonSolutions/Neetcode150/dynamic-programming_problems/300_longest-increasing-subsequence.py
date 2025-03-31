"""
- NOT A CONTIGUOUS SUBARRAY, can pick and choose any subsequence
- there are negative numbers 
- no integer overflow
- length is 1 to 2500
- Returns the length of the LIS

DP: We will be using a nested for loop to create subsequences from START to END

State: dp[end]
    - end is the "ending" position of the current subsequence array
    - dp[end] represents the LIS at position end
        NOTE: This means ALL combinations of longest increasing subsequences but uses the longest length
            E.g. [10, 9, 2, 5, 3, 7], dp[5] = 3, meaning the longest length is 3, but MULTIPLE COMBINATIONS
                - Length 1: Itself (7)
                - Length 2: 2, 7 | 5, 7 | 3, 7
                - Length 3: 2, 5, 7 | 2, 3, 7
    
Recurrence Relation: max(dp[end], dp[start] + 1)
    - Selecting the max between:
        1. dp[end], Longest length up to the end of current subsequence
        2. dp[start] + 1, Longest length at starting point PLUS new length
            - Since nums[start] has its own MULTIPLE COMBINATIONS, we add 1 more 
                as its smaller than nums[end] which also has its own MULTIPLE COMBINATIONS

Base case: Initial states are ALL 1, the number is the longest subsequence of itself

Returns: The max out of all numbers in the DP array
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Base cases: Initial states are all 1, number itself is the LIS
        LIS = [1] * n

        # Recurrence relation: At every index end, test all possible combinations of LIS up to nums[end]
        for end in range(n):
            # Creates a nested for loop subsequence from index start to end boundary
                # Allows us to test all possible combinations to compare between start and end numbers
            for start in range(end):
                # nums[end] is represented as the largest number in the subsequence we need to compare to
                    # If the starting number is smaller that means there is a valid LIS
                if nums[start] < nums[end]:
                        # Selecting the max between:
                            # 1. dp[end], Longest length up to the end of current subsequence
                            # 2. dp[start] + 1, Longest length at starting point PLUS new length
                    LIS[end] = max(LIS[end], LIS[start] + 1)
        
        return max(LIS)

class BruteForceBacktrackingSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def is_increasing_sub(subsequence):
            for i in range(len(subsequence) - 1):
                if subsequence[i] >= subsequence[i+1]:
                    return False
            return True

        def backtrack(idx, current_subsequence):
            # Base case 1: When we hit end of array, check if the selected subsequence is increasing
            if idx == len(nums):
                # If its increasing return the length
                if is_increasing_sub(current_subsequence):
                    return len(current_subsequence)
                # Else return a length of 0
                return 0

            # The two choices below allow us to check all possible generated subsequences
                # The inclusion and exclusion (backtrack) choices are in the parameters
                # Below calls are the explorations

            # Choice 1: Include the current number as part of the subsequence as deep as possible
                # Uses + [nums[idx]] because .append will pass the param as a None
            take = backtrack(idx + 1, current_subsequence + [nums[idx]])
            # Choice 2: Exclude the current number and try that as deep as possible
            dont_take = backtrack(idx + 1, current_subsequence)
            
            # Returns the max between if you take the current index or don't take
                # The reason is that each options will have different options
            return max(take, dont_take)

class TopDownUnoptimizedSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(index, prev_idx):
            # Base case: reached end of array
            if index == len(nums):
                return 0
            
            # Don't take current element
            length = dfs(index + 1, prev_idx)
            
            # Take current element if it's greater than previous element
            if prev_idx == -1 or nums[index] > nums[prev_idx]:
                length = max(length, 1 + dfs(index + 1, index))
            
            return length
        
        return dfs(0, -1)

class TopDownSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # memo[i][prev_idx] represents the LIS starting at index i with prev_idx as previous element
        memo = {}
        
        def dfs(index, prev_idx):
            if index == n:
                return 0
            
            if (index, prev_idx) in memo:
                return memo[(index, prev_idx)]
            
            # Don't take current element
            length = dfs(index + 1, prev_idx)
            
            # Take current element if it's greater than previous element
            if prev_idx == -1 or nums[index] > nums[prev_idx]:
                length = max(length, 1 + dfs(index + 1, index))
            
            memo[(index, prev_idx)] = length
            return length
        
        return dfs(0, -1)

class MostOptimizedBinarySearchSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(sub, target):
            left, right = 0, len(sub) - 1
            
            # Find leftmost position where target should be inserted
            while left <= right:
                mid = (left + right) // 2
                if sub[mid] == target:
                    return mid
                elif sub[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        sub = []
        
        for num in nums:
            # If sub is empty or num is larger than last element
            if not sub or num > sub[-1]:
                sub.append(num)
            else:
                # Find position to insert num
                pos = binary_search(sub, num)
                sub[pos] = num
        
        return len(sub)