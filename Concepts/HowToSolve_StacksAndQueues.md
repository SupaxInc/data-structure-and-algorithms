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

**Example: Sliding Window Maximum**

```python
from collections import deque

def max_sliding_window(nums, k):
    q = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove elements not within the sliding window
	        # q[0] is accessing the index not the value
	        # q[0] is the first one added in window
        if q and q[0] < i - k + 1:
            q.popleft() # Removes the first one added
        
        # Maintain the decreasing order in the queue
	        # q[-1] is the last index in the queue (the last to be added)
        while q and nums[q[-1]] < nums[i]:
            q.pop() # Removes the last one added
        
        q.append(i)
        
        # Start adding the maximum of each window to the result
        if i >= k - 1:
            result.append(nums[q[0]])
    
    return result
```