class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # * Partitioning means dividing the array into two halves - a left and right portion *

        # Always make nums1 the shorter array to optimize our binary search
            # Having fewer elements means a smaller search space and nums1 is the only array we are binary searching
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        # x is the length of nums1 (shorter array) - used as boundary for binary search
        # y is the length of nums2 (longer array) - used to calculate partition point in nums2
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Binary search on the smaller array (nums1) to find where to partition it
            # partitionX represents how many elements we take from nums1 for the left half
                # Remember x is used to reference pointer high
            partitionX = low + ((high-low) // 2)

            # Once we know how many elements we're taking from nums1,
            # we can calculate how many we need from nums2 to make the left half complete
                # Essentially, partition X is for binary search and partition Y adjusts accordingly
            # The +1 handles both odd and even total lengths
                # E.g. x = 3, y = 4, 8 // 2 = 4
                # E.g. x = 4, y = 4, 8 + 1 = 9 // 2 = 4.5 = 4
            partitionY = (x + y + 1) // 2 - partitionX

            # Get the elements around the partition point
            # For nums1: maxX is the last element on left side, minX is first element on right side
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            # For nums2: maxY is the last element on left side, minY is first element on right side
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            # Valid partition means:
            # 1. All elements in left half ≤ all elements in right half
            # 2. maxX ≤ minY and maxY ≤ minX
            if maxX <= minY and maxY <= minX:
                # For even total length: median is average of max of left half and min of right half
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                # For odd total length: median is the max element in the left half
                else:
                    return max(maxX, maxY)
                    
            # If partition is wrong, adjust binary search:
            elif maxX > minY:
                # Left side of nums1 is too big, need to take fewer elements from nums1
                high = partitionX - 1
            else:
                # Left side of nums1 is too small, need to take more elements from nums1
                low = partitionX + 1
