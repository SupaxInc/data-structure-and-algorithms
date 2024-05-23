class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # If nums1 is longer than nums2, swap them to minimize the binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        
        while low <= high:
            # Find the partition point for nums1
                # **We will be binary searching on partitionX**
            partitionX = (low + high) // 2
            # To get the partition for nums2, we need the total + 1
                # +1 allows us to divide by odd or even numbers
                # E.g. x = 3, y = 4, 8 // 2 = 4
                # E.g. x = 4, y = 4, 8 + 1 = 9 // 2 = 4.5 = 4
            partitionY = (x + y + 1) // 2 - partitionX

            # Elements immediately left of the partition in nums1
            # If partitionX is 0, use negative infinity as there are no elements left
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            # Elements immediately left of the partition in nums2
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            
            # Elements immediately right of the partition in nums1
            # If partitionX is at the end of nums1, use positive infinity as there are no elements right
            minX = float('inf') if partitionX == x else nums1[partitionX]
            # Elements immediately right of the partition in nums2
            minY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if we have found the correct partition
                # Ensure that all elements on the left are less than or equal to those on the right across both arrays
                # If its not valid an example would be: [... 4] [3...], our right partition cannot be greater than left
            if maxX <= minY and maxY <= minX:
                # If the total number of elements is even, return the average of the two middle elements
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    # If the total number of elements is odd, return the maximum of the two elements left of the partition
                    return max(maxX, maxY)
            elif maxX > minY:
                # If elements on the left of nums1 are too big, move the partition left
                high = partitionX - 1
            else:
                # If elements on the left of nums1 are too small, move the partition right
                low = partitionX + 1
