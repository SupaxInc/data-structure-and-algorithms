# Quick Select

## Key Concept

The algorithm partitions the array into two parts, similarly to quicksort, around a selected "pivot" element. It uses this pivot to divide the data into those less than the pivot and those greater than the pivot. 

However, unlike quicksort, it does not recursively sort both sides; instead, it only sorts the array enough just to know that the left side of the pivot index is smaller and the right side of pivot is larger.

## Use Case

Finding the K-th largest or smallest element in an array.

## Steps

1. **Choose a Pivot:** Select an element from the array as the pivot. The choice of pivot can be random, the first element, the last element, or using more sophisticated methods like the median-of-medians to find a good pivot.
2. **Partitioning:** Rearrange the array so that all elements less than the pivot come before it and all elements greater come after it. This step is similar to the partitioning in quicksort.
3. **Select Side:**
    - If the pivot position is the same as k, return the pivot (because the array is partitioned such that the first k elements are the smallest k elements, making the k-th element the k-th smallest).
    - If the pivot position is greater than k, recursively apply the algorithm to the left part of the array.
    - If the pivot position is less than k, adjust k (`k = k - pivot position - 1`) and recursively apply the algorithm to the right part of the array.

## Example

Suppose you have the array [3, 6, 2, 1, 8, 4, 5] and you want to find the 3rd smallest element:

1. **Choose a Pivot:** Say you pick 4 as the pivot.
2. **Partition:** After partitioning, the array might look like [3, 2, 1, 4, 8, 6, 5], with 4 in the correct position.
3. **Select Side:** Since 4 is the 4th element (position 3, considering 0-based index), and you are looking for the 3rd smallest, you only consider the left part: [3, 2, 1].
4. Repeat the process on the left side. You might pick 2 as the next pivot and partition to get [1, 2, 3]. We see that the 2 is the 2nd smallest element and we need to find a bigger element to find 3rd smallest so we recursively apply the algorithm again on the right side.

### Template Code

To find the Kth smallest, check if the pivot index equals the kth index.

To find the Kth largest, check if the pivot index equals the difference between length of array and the kth index. Helps find the last element in the array which is the largest.

```python
def quick_select(arr, left, right, k):
    # Base case: if the partition size is one, return the element
    if left == right:
        return arr[left]

    # Randomly select a pivot index between left and right
	    # Prevents worst case scenario of sorting an element 
    pivot_index = random.randint(left, right)

    # Rearrange elements so that pivot is in its correct position
    pivot_index = partition(arr, left, right, pivot_index)

    # If pivot position matches k, return its value (k-th smallest found)
    if k == pivot_index:
        return arr[k]
    # If k is less than the pivot index, search in the left partition
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    # If k is greater than the pivot index, search in the right partition
    else:
        return quick_select(arr, pivot_index + 1, right, k)

def partition(arr, left, right, pivot_index):
    # Use the pivot element to compare with others
    pivot_value = arr[pivot_index]

    # Move pivot to the end temporarily
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    # Start moving elements less than pivot to the left side
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    
    # Place the pivot element in its correct sorted position
    arr[store_index], arr[right] = arr[right], arr[store_index]

    # Return the final position of the pivot
    return store_index

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 5]
k = 4  # Find the 4th smallest element
print("The 4th smallest element is:", quick_select(arr, 0, len(arr) - 1, k-1))

# If you want to find the largest element
# Instead of passing just k, you have to pass len(arr) - k
# This helps us find kth last elements which is the largest numbers.
```

## Performance

- **Best and Average Case:** The time complexity of Quick Select is O(n), similar to quicksort on average.
- **Worst Case:** The time complexity can degrade to O(n^2) if the pivot elements are poorly chosen, such as always picking the smallest or largest element as the pivot, which is why randomization or advanced pivot selection techniques can be crucial.

# Quick Sort