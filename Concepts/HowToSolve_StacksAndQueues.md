# Types of Stack Problems

## Monotonic decreasing stack

- **Definition**:
    - Elements maintained in descending order (largest → smallest)
    - Pop smaller elements when adding new element
- **Properties**:
    - Elements are inserted and removed from the top.
    - Maintains order where each new element pushed onto the stack ensures the stack remains in decreasing order.
- **Use Case**:
    - **Find the next smaller element** to the left or right in a sequence.
    - **Calculate spans** (like stock span problems).
    - **Optimize time complexity** in algorithms that would otherwise be quadratic.
    - **Handle range queries** where you need to maintain a certain order.
- **Appends the index to the stack**

**Example template code:**

```python
def next_smaller_elements(nums):
    """
    Finds the next smaller element for each element in the list.
    If there is no smaller element to the right, assigns -1.
    """
    n = len(nums)
    result = [-1] * n  # Initialize the result list with -1
    stack = []  # Initialize an empty stack

    for i in range(n - 1, -1, -1):
        # Remove elements from top of stack that are greater or equal to nums[i]
        while stack and stack[-1] >= nums[i]:
            stack.pop()

        # If stack is not empty, the top is the next smaller element
        if stack:
            result[i] = stack[-1]

        # Push the current element onto the stack
        stack.append(nums[i])

    return result
    
Example Usage:
nums = [4, 8, 5, 2, 25]
print(next_smaller_elements(nums))  # Output: [2, 5, 2, -1, -1]
```

### Explanation

- **Initialize** a result list filled with `1`, indicating no smaller element to the right by default.
- **Iterate** through the list from right to left.
- **Use the stack** to keep track of potential next smaller elements.
- **Pop elements** from the stack that are **not smaller** than the current element.
- **Update the result** if the stack isn't empty after popping.
- **Push the current element** onto the stack for future comparisons.

**Explanation of Output:**

- For `4`, the next smaller element is `2`.
- For `8`, it's `5`.
- For `5`, it's `2`.
- For `2`, there's no smaller element to the right, so `1`.
- For `25`, there's no smaller element to the right, so `1`.

## **Monotonic increasing stack**

- **Definition**:
    - Elements maintained in ascending order (smallest→ largest)
    - New elements pushed to the stack is greater than or equal to the element below it
- **Properties**:
    - Elements are inserted and removed from the top.
    - Maintains order where each new element pushed onto the stack ensures the stack remains in increasing order.
- **Use Case**:
    - Frequently used in problems involving next greater or previous greater elements.
    - Useful in histogram problems (like LeetCode #84), interval problems, and others where the relative size of elements and their order matter.
    - **Find the next greater element** to the left or right in a sequence.
    - **Calculate spans** where you need to consider previous larger elements.
    - **Optimize algorithms** that require comparing each element with previous ones efficiently.
    - **Handle range queries** for maximum values.

**Example template code:**

```python
def next_greater_elements(nums):
    """
    Finds the next greater element for each element in the list.
    If there is no greater element to the right, assigns -1.
    """
    n = len(nums)
    result = [-1] * n  # Initialize the result list with -1
    stack = []  # Stack to keep indices of elements

    for i in range(n - 1, -1, -1):
        # Remove elements from the stack that are less than or equal to nums[i]
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        # If stack is not empty, the top is the index of the next greater element
        if stack:
            result[i] = nums[stack[-1]]

        # Push current index onto the stack
        stack.append(i)

    return result

```

### Example Usage

```python
nums = [4, 5, 2, 25]
print(next_greater_elements(nums))  # Output: [5, 25, 25, -1]
```

**Explanation of Output:**

- For `4`, the next greater element is `5`.
- For `5`, it's `25`.
- For `2`, it's `25`.
- For `25`, there's no greater element to the right, so `1`.

# Types of Queue Problems

## Monotonic decreasing queue

- **Definition**:
    - Elements maintained in descending order (largest → smallest)
    - When new elements are added, elements that are greater than the new element are **removed from the back of the queue** to maintain the decreasing order.
- **Properties**:
    - Elements are could be removed from the back or the front of the queue depending on the scenario.
    - Maintains order where each new element added to the back ensures the queue remains in decreasing order.
- **Use Case**:
    - **Sliding window maximum/minimum** problems.
    - **Dynamic programming** where you need to maintain a window of potential candidates.
    - **Optimization problems** where the current state depends on previous states in a monotonic fashion.
- **Appends index to the queue**

**Example: Sliding Window Maximum**

```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    res = []

    q = deque()
    start = 0
    for end in range(len(nums)):
        # Remove elements that are not within the current fixed window
            # **q[0] grabs the value of the first element (in this case the index) added to the queue**
        if q and q[0] < start:
            q.popleft() # Remove first element added to the front of the queue
        
        # Maintain descending order in current fixed window by removing elements that are less than current element
            # **q[-1] grabs the value of the last element (in this case the index) added to the queue**
            # E.g. We want to add 9 to the queue [7, 6] -> current element is 9 -> so [9] will just be left after comparison
        while q and nums[q[-1]] < nums[end]:
            q.pop() # Remove last element that was added to the back of queue
            # After popping, we will have the index of the highest value in the current fixed window
        
        # **Here is where the index is being added to the queue**
        # Adds the current index which is the index of nums array that has the highest value in the current fixed window
        q.append(end)

        # If the window is of valid size then add the highest value of window to result
        if (end - start + 1) == k:
            # Add the first element in front of the queue (the max since its descending order)
            res.append(nums[q[0]])
            start += 1 # Move start forward
    
    return res
```