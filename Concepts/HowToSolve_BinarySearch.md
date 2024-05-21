# **What is Binary Search?**

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

# **Best Way to Solve Binary Search Problems**

1. **Understand the Problem**: Ensure the array is sorted or can be treated as sorted.
2. **Identify the Search Space**: Determine the boundaries (low and high) for the search.
3. **Iterative or Recursive Approach**: Decide whether to implement the binary search iteratively or recursively.
4. **Middle Point Calculation**: Compute the middle point to avoid overflow using **`mid = low + (high - low) // 2`**.
5. **Comparison and Narrowing**: Compare the target with the middle element and narrow the search space accordingly.
6. **Edge Cases**: Handle edge cases like empty arrays, single-element arrays, and duplicates if applicable.

## **Use Cases**

- **Finding an Element**: Directly search for an element in a sorted array.
- **Finding Boundaries**: Locate the lower or upper bound of a range of elements.
- **Search Variants**: Problems that involve searching for a peak, finding the minimum/maximum in a rotated array, or other conditions that involve ordered elements.

## **Common Problem Wordings**

- "Find the element..."
- "Search for..."
- "Determine the first/last occurrence..."
- "Find the boundary..."
- "Maximum/minimum value that satisfies..."
- "Peak element..."
- "Rotated sorted array..."

# **Properties of Binary Search**

- **Time Complexity**: *O*(log*n*) for searching.
- **Space Complexity**: *O*(1) for iterative, *O*(log*n*) for recursive due to stack space.
- **Data Structure**: Requires the array (or list) to be sorted.

---

# **Common Binary Search Templates**

## **Iterative Binary Search**

```python
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2 # Prevents arithmetic overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found
```

## **Recursive Binary Search**

```python
def binary_search_recursive(nums, target, low, high):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, high)
    else:
        return binary_search_recursive(nums, target, low, mid - 1)
```

## **Finding the Lower Bound (First Occurrence)**

```python
def lower_bound(nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low if nums[low] == target else -1
```

## **Finding the Upper Bound (Last Occurrence)**

```python
def upper_bound(nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low + 1) // 2
        
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid
    return low if nums[low] == target else -1
```

## **Special Cases and Advanced Binary Search**

### **Rotated Sorted Array**

```python
def search_rotated(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:  # Left part is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right part is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
```

### **Finding Peak Element**

```python
def find_peak_element(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low
```

# Example Problem

```python
Initial array: [2, 4, 7, 10, 13, 18, 21]
Target value: 13

Step 1:
left = 0, right = 6
Calculate mid: mid = 0 + (6 - 0) // 2 = 3
Compare arr[mid] = arr[3] = 10
arr[mid] < target, move left to mid + 1
New left = 4

Step 2:
left = 4, right = 6
Calculate mid: mid = 4 + (6 - 4) // 2 = 5
Compare arr[mid] = arr[5] = 18
arr[mid] > target, move right to mid - 1
New right = 4

Step 3:
left = 4, right = 4
Calculate mid: mid = 4 + (4 - 4) // 2 = 4
Compare arr[mid] = arr[4] = 13
Found target at index 4
```