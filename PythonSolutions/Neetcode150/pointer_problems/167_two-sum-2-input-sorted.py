class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        # Move right pointer to left if total is greater
        # Move left pointer to right if total is smaller
        while l <= r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l+1, r+1]
            
        return [l+1, r+1]