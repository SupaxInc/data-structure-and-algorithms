class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect if theres a cycle
            # Cycle tells us that there was a duplicate somewhere
            # It does not give us the duplicate value. If you look at the examples, 
            # a duplicate number just brings us to the "linked list" index
            # E.g. Example 1, value "2" brings us to index 2 which is value "4"
        slow = fast = 0 # Begin at index 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # Fast skips a connection each time due to nested checks
            if slow == fast:
                break # Intersection has been found

        # Step 2: Find the cycle entry point
            # Cycle ENTRY point (where cycle begins) is the duplicate value
        # - Reset a NEW slow pointer to beginning of list
        # - Keep the old slow pointer from where the intersection was met for the cycle
        # - The distance between cycle intersection and beginning of list is the same (P = C-X)
            # - Therefore, move the 2 pointers 1 by 1 until distance P meets distance C-X
        slow2 = 0
        while True:
            slow = nums[slow] # Previous slow pointer stays at intersection
            slow2 = nums[slow2] # New slow pointer will try and intersect with first slow pointer
            if slow == slow2:
                return slow
