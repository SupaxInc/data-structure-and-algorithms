class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect if theres a cycle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: Find the cycle entry point
        # - Reset a slow pointer to beginning of list
        # - Keep the slow/fast pointer from where the intersection was met for the cycle
        # - Move them 1 by 1
        # - The distance between cycle intersection and beginning of list is the same (P = C-X)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
