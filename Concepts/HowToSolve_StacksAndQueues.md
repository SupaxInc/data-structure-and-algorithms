# Types of Stack Problems

## Monotonic decreasing stack

https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e

- **Definition**: A stack where each element is less than or equal to the previous element when traversing from top to bottom.
    - The key property of a monotonic decreasing stack is the preservation of a descending order.
- **Properties**:
    - Elements are inserted and removed from the top.
    - Maintains order where each new element pushed onto the stack ensures the stack remains in decreasing order.
- **Use Case**: Frequently used in problems involving next smaller or previous smaller elements, as it allows efficient querying of the next or previous smaller element.
    - Useful in problems involving the next greater element, interval problems, histogram problems, and others where the relative size of elements and their order matter.
- **Appends the index to the stack**

**Example to find the next smaller elements in an array:**

```python
def nextSmallerElements(nums):
    result = [-1] * len(nums)  # Default to -1 for elements with no smaller next element
    stack = []  # Use list as stack; stores indices

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] > num:
            topIndex = stack.pop()
            result[topIndex] = num
        stack.append(i)
    
    return result
```

1. **Iterate Through Array**: Go through each element in the array.
2. **Maintain Decreasing Order**: For the current element, pop elements from the stack as long as the current element is smaller than the stack's top element. This means the current element is the next smaller element for those being popped.
3. **Push Current Element**: Push the current element onto the stack. Due to the pops, the stack remains in decreasing order.

# Types of Queue Problems

## Monotonic decreasing queue

- **Definition**: A queue where each element is less than or equal to the previous element when traversing from front to back.
- **Properties**:
    - Elements are inserted at the back and removed from the front.
    - Maintains order where each new element added to the back ensures the queue remains in decreasing order.
- **Use Case**: Often used in sliding window problems to maintain the maximum element in the current window.
- **Appends index to the queue**

**Example: Sliding Window Maximum**

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()
        start = 0
        for end in range(len(nums)):
            # Remove elements that are not within the current fixed window
                # q[0] is accessing the index NOT the value of the queue
                # It is the index of the first element added to queue
            if q and q[0] < start:
                q.popleft() # Remove first element added to queue
            
            # Maintain descending order in current fixed window
                # Compares last element added to queue with current element
            while q and nums[q[-1]] < nums[end]:
                q.pop() # Remove last element added to queue
            
            q.append(end) # Add the current index to queue after maintaining descending order

            # If the window is of valid size then add to result
            if (end - start + 1) == k:
                # Add the first elemetn in queue (the max since its descending order)
                res.append(nums[q[0]])
                start += 1
        
        return res
```