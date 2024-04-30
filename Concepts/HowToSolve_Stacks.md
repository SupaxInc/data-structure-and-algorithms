# Types of Stack Problems

## Monotonic decreasing stack

https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e

The key property of a monotonic decreasing stack is the preservation of a descending order. This property is particularly u**seful in problems involving the next greater element, interval problems, histogram problems, and others where the relative size of elements and their order matter**.

Monotonic decreasing stacks are often used in algorithms to **solve problems that require efficiently finding the next smaller element in a sequence or maintaining a history of elements that have not yet found a smaller succeeding value.**

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