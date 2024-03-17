def subsets(nums):
    result = []
    subset = []

    def backtrack(start):
        # Since we want all subsets, add the current subset at the start of exploration
        result.append(subset.copy())

        for i in range(start, len(nums)):
            # Include the number nums[i]
            subset.append(nums[i])
            # Recurse with the next number
            backtrack(i + 1)
            # Exclude the number nums[i], backtrack
            subset.pop()

    backtrack(0)
    return result

subsets([1,2,3])