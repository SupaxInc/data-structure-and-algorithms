https://www.youtube.com/watch?v=MK-NZ4hN7rs

# What is a sliding window?

Imagine you have a physical window that can expand or contract, sliding along a long track that represents your array or string. The window frame represents the subset of data you're currently focusing on. It can "slide" from the beginning of the data set towards the end, and its size can change based on certain conditions.

## Fixed Sized Windows

 For problems where the window size remains constant, the window slides along the data set, moving one element at a time, maintaining the same size but changing its content.

### Example

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/873faa24-d2b1-4571-b706-6c27b13f8d39/Untitled.png)

Imagine two shapes. The blue square is the first shape. It could represent an array, linked list, pretty much any arbitrary data that could be contiguous or adjacent to one another.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/19ebbf92-beaa-4553-a58a-252ec8a522d4/Untitled.png)

The yellow square is the second shape. We add it onto the first shape. It represents the subset of the data of the full data set. This where we start to ask questions: “**Is this the best I can do?”**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/7f1a3c77-5c89-40f2-9864-6ebf43e66ed5/Untitled.png)

We slide the window again and ask again if this is the best we can do. If its better than the previous, than we add it as some sort of max or add it to a result set.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/9e8481e4-8fc4-42b5-9b67-50ff93eca847/Untitled.png)

We slide the window again and see that the next subset is worst so we just ignore it. In the end, we’ve accumulated the best answer.

It stops when we hit the end of the data set.

### Template Code

```python
def fixedSizeSlidingWindow(arr, k):
    # Initialize variables for the calculation you need (e.g., sum, max, min).
    window_result = 0
    result = []

    # Initialize the starting point of the window.
    start = 0

    for end in range(len(arr)):
        # Update the calculation with the new element added to the window.
        window_result += arr[end]

        # Check if the window has reached its fixed size.
        if end >= k - 1:
            # Update the global result based on the current window's result.
            result.append(window_result)  # Or perform any operation as needed.

            # Subtract the element leaving the window.
            window_result -= arr[start]

            # Slide the window forward.
            start += 1

    return result
```

## Dynamic Sized Windows

For problems where the window size can change, the window expands or contracts based on specific conditions, adjusting its size to meet the problem's requirements.

### Example

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/057ff4cf-fd5e-4c74-b93a-0613091e65c6/Untitled.png)

It begins again with 2 shapes.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/97852d3e-26a5-4757-8580-97c694d46b3d/Untitled.png)

Instead of moving the entire window in a fixed size, we slide the right side until we meet a condition.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/464f9ef8-412e-45fe-9af9-9da1d4872770/Untitled.png)

When we met the previous criteria we move the left side until we meet another criteria to again move the right side. It’s like a caterpillar moving across a tree.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/fc9ceecc-feb7-4381-bb6f-5247d4d1fb03/Untitled.png)

Eventually, it grows to the point until it hits the end of the array. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a430fe18-780c-4077-9c47-90e70ecc14ea/Untitled.png)

Even if it hits the end of the array, we can still shrink it further. 

If we can’t move further, at this point similar to fixed size, we should have accumulated the best possible answer based on our criteria's.

### Template Code

**Without Auxiliary**

```python
def findMaxSubarrayLength(arr):
    start = 0
    maxLength = 0
    # Initialize variables necessary for your condition

    for end in range(len(arr)):
        # Update any needed variables with the new element added to the window

        # While loop to shrink the window if the condition is not met
        while not isValidCondition():
            # Update variables to remove the start element from the window
            start += 1

        # Update maxLength or perform necessary calculations outside the while loop
        maxLength = max(maxLength, end - start + 1)

    return maxLength
```

**With Auxiliary**

```python
def findMaxSubarrayWithAux(arr):
    start = 0
    maxLength = 0
    auxData = {}  # Can be a set or dict based on problem

    for end in range(len(arr)):
        # If using dict, update the count of the new element
        if arr[end] not in auxData:
            auxData[arr[end]] = 0
        auxData[arr[end]] += 1

        # While loop to shrink the window if the condition is not met
        while not isValidCondition(auxData):
            # Update auxData to remove the start element from the window
            auxData[arr[start]] -= 1
            if auxData[arr[start]] == 0:
                del auxData[arr[start]]
            start += 1

        # Update maxLength or perform necessary calculations outside the while loop
        maxLength = max(maxLength, end - start + 1)

    return maxLength
```

**Check out Longest Repeating Character, Leetcode 424**

# Why do we want to even do this technique?

There are alternatives to this technique including a more naïve brute force approach of unnecessary iteration over elements we have already seen.

We end up duplicating work which typically yields a O(n*n) aka O(n^2) time complexity.

This technique prevents duplicated work and instead we are sliding in a more linear time of O(n). We no longer look at values that we’ve already seen thus far.

# How do you implement this technique?

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/08c9109d-b861-4d95-b52e-56b07524bb57/Untitled.png)

To solve this problem, we need to follow the constraints that we have where we need to find the max sum with only a subset of size 3. We can tell already that we can use a fixed sized window to accomplish this.

To keep track of maximum thus far, we need to keep a variable that is initialized with -Infinity since there could be negative numbers.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c9e4713e-bfad-4d41-b647-e13b93b31be7/Untitled.png)

To move the fixed sized window, we just subtract the 4 from the total and add the next element 7.

# How do you recognize these problems?

1. Look for things that need iterating sequentially
    1. Contiguous sequence of elements (strings, arrays, linked lists)
2. Problem needs to find the min, max, longest, shortest, contains.
    1. Maybe we need to calculate something

## Different variants of problems

1. Fixed length sizes
    1. E.g. max sum subarray of size k
2. Dynamic sized
    1. E.g. smallest sum greater than or equal to some value of N
3. Dynamic sized with auxiliary data structure
    1. Auxiliary is a fancy way of saying a hashmap or set or additional array
    2. E.g. longest substring of no more than K distinct characters
4. String permutations
    1. Does the second string as a permutation of the parent string?

## Commonalities

1. Everything grouped sequentially
2. Everything specifies to some sequential criteria: longest, smallest, contains, shortest, etc.