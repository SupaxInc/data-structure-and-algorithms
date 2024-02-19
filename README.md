# Neetcode 150

**Brute Force:**  

- Time Complexity:
- Space Complexity:

**Optimized Approach:**

- ****Time Complexity
- Space Complexity:

**Solution:**

**Unique uses:**

- 

# Arrays

## 217 - Contains Duplicate

**Brute Force[O(n^2)**]**:** Nested For Loop, 

**Optimized Approach:** Using Hashmaps O(n)

**Solution:** Iterate through the list and check if it already exists inside the hashmap

## 242 - Valid Anagrams

**Bruce Force[O(n^2)]:** Nested For Loop

**Somewhat Optimized[O(nlogn)]:** Sorting

**Optimized Approach[O(n)]:** Hashmaps

**Solution:** Count letters in both strings using a hashmap then compare the two hashmaps for both key and value pairs

## 1 - Two Sum

**Brute Force[O(n^2)]:** Nested for loop ****

**Optimized Approach[O(n)]:** Hashmaps

**Solution:** Uses a hashmap to store and look up the complement of each number (target - current number) to find the indices of the two numbers that add up to the target.

# Pointers

## 125 - Valid Palindrome

**Solution 1:**

**Brute Force[O(n^2)]:** Nested for loop  ****

**Optimized Approach[O(n)]:** For loop ****

**Solution:** Create two pointers; one for start of string and another for end of string. Compare the two pointers but make sure you are comparing a string with non-alphanumeric characters lowercased.

**Solution 2:**

**Brute Force[O(n^2)]:** Nested for loop  ****

**Optimized Approach[O(n)]:** For loop ****

**Solution:**  Go through the string and create a new string by filtering out non-alphanumeric characters (is.digit(), is.alpha()). Compare the new string with the reverse of it.

## 121 - Best Time to Buy and Sell Stock

**Solution 1:**

**Brute Force[O(n^2)]:** Nested for loop  ****

**Optimized Approach[O(n)]:** Two pointers, 1 for loop

**Solution:** Two-pointer approach to find the maximum profit by buying low and selling high, dynamically updating the pointers based on the current and next day's prices.

**Solution 2:**

**Brute Force[O(n^2)]:** Nested for loop  ****

**Optimized Approach[O(n)]:** For loop

**Solution:** Iteratively updates the lowest price seen so far and calculates the maximum profit possible at each step by comparing the current price with the lowest price.

# Stacks

## 20 - Valid Parentheses

**Brute Force[O(n^2)]:** Nested for loop and counting open vs closing parentheses

**Optimized Approach[O(n)]:** Use a hashmap and stack

**Solution:** Uses a stack to ensure that each closing bracket correctly matches and properly follows its corresponding opening bracket, returning false if the stack is empty or the top of the stack doesn't match the expected opening bracket for a given closing bracket.

# Binary Search

## 704 - Binary Search

**Brute Force[O(n)]:** For loop

**Optimized Approach[O(log n)]:** Divide and conquer with binary search

**Solution:** Binary search to find the target in a sorted array by repeatedly dividing the search array in half with two low and high pointers. If the target is less than the mid number go right, else vice-versa.

# Linked List

## 206 - Reversed Linked List

**Optimized Approach[O(n)]:** Normal traversal through a linked list

**Solution:** Iteratively reverse a singly-linked list by using a temp pointer of the next current node then using the next node of the current node to point to the previous node effectively creating a reversal. The current node then becomes the temp pointer to restart the process again. 

## 21 - Merged Two Sorted Lists

**Optimized Approach[O(n)]:** Normal traversal through a linked list

**Solution:** Point the merged list to a reference to a dummy node, the dummy node will be used to traverse and create the sorted list by connecting it to the list with the smallest value each iteration.

**Gotchas:**

- Merged list needs to point to a dummy node to reference the head of the new sorted list as it will traverse to the tail end
- Since while loop may exist early with a list still having remaining elements, we need to connect the dummy node to the remaining elements
- Use Chat GPT as a visualization of how the iterative process works:
    - Initialization: mergedList -> [dummy node]
    - Moving dummy node to the next node: mergedList -> [dummy node] -> [1]
    - Moving dummy node to the next node: mergedList -> [dummy node] -> [1] -> [2]
    - Returning the next node of mergedList:  [1] -> [2]
    

## 141 - Linked List Cycle

**Brute Force: Visit each node using a set**

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach: Visit each node using pointers**

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** The solution uses Floyd's Tortoise and Hare algorithm, where two pointers move at different speeds through the list, and a cycle is detected if the slow pointer meets the fast pointer.

# Binary Tree

## 226 - Invert Binary Tree

**Brute Force:** Maybe an iterative approach since we have to use arrays

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach:** Use a recursive approach

- ****Time Complexity: O(n)
- Space Complexity: O(h)

**Solution:** Do a post-order or pre-order traversal, swap the nodes when you visit the node.

## 104 - Maximum Depth of Binary Tree

**BFS Approach:** Maybe an iterative approach since we have to use arrays

- Time Complexity: O(n)
- Space Complexity: O(n)

**DFS Approach:** Use a recursive approach

- ****Time Complexity: O(n)
- Space Complexity: O(h)

**BFS Solution:** Do a level order traversal by using a queue and adding the left and right nodes to the queue. Use a for loop with range length of queue inside a while loop to only traverse through nodes in each level.

**DFS Solution:** Add a 1 for the current level then add with the max between the left and right sub tree.

## 543 - Diameter of Binary Tree

**DFS Approach:** Use a recursive approach

- ****Time Complexity: O(n)
- Space Complexity: O(h)

**DFS Solution:** Find the maximum depth ( 1+ max(..)) of each sub tree and add the left and right sub tree every time the stack pops to get max diameter. 

**Unique uses:**

- Nonlocal keyword to use variables outside of the scope function.

## 110 - Balanced Binary Tree

**DFS Approach:** Use a recursive approach

- ****Time Complexity: O(n)
- Space Complexity: O(h)

**DFS Solution:** Find the maximum depth ( 1+ max(..)) of each sub tree then check for an imbalance between the left and right sub tree by a value of greater than 1. (e.g. 3-1 = 2, unbalanced)

**Unique uses:**

- Continuously return a value up the call stack if no further work is necessary

## 100 - Same Tree

**DFS Approach:** Use a recursive approach

- ****Time Complexity: O(p+q) 2 trees to traverse to
- Space Complexity: O(h)

**DFS Solution:** Traverse through both trees left and right nodes. You know their the same tree if you are able to reach the depths with a None value.

## 572 - Subtree of Another Tree

**DFS Approach:** Use two recursive DFS approaches

- ****Time Complexity: O(m * n)
    - Where m is the nodes of the Root tree and n is the nodes of the sub root
- Space Complexity: O(max(m, n))
    - Depends on the height of the recursion stack for either root or sub root

**DFS Solution:** DFS through the root tree and run another DFS on a node of a root tree if you haven’t hit the end of the root tree. The second DFS runs a check if the root tree or sub root tree are the same trees.

**Unique uses:**

- Uses recursion within a recursion

# Heap/Priority Queues

## 703 - Kth Largest Number

**Brute Force:**  Sort the array each time and return the kth index

- Time Complexity: O(nlogn)
- Space Complexity: O(n)

**Optimized Approach:** Use a min heap

- ****Time Complexity: O(n) → heapify, O(log n) → adding to heap
- Space Complexity: O(k), array will be as large as kth elements

**Solution:** Using a min-heap, maintaining a heap of size k to ensure the kth largest element is always at the top, with adjustments made upon each new addition.

**Unique uses:**

- Uses a heap:
    - Heapify → O(n)
    - Heappop/Heappush → O(logn)

## 1046 - Last Stone Weight

**Brute Force:**  Sort the array in descending and pop values for the stones

- Time Complexity: O(n) → first while loop, O(nlogn) → inside while loop = O(n^2 log n)
- Space Complexity: O(1) → memory is in-place

**Optimized Approach:** Create a max heap 

- ****Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Create a max heap to get the 2 largest stones then just follow the instructions.

**NOTE:** Result array does not have to be in-order because we are just popping values

**Unique uses:**

- Creates a max heap work around by multiplying by -1

# Dynamic Programming

## 70 - Climbing Stairs

**Brute Force:**  Use DFS recursive approach similar to Fibonacci sequence 
**(climb_stairs_dfs(n-1) + climb_stairs_dfs(n-2))**

```markdown
			                   5
                       /   \
                      4     3
                    /  \   / \
                   3    2 2   1
                  / \  /|  |\
                 2  1 1 0 1  0
                /|
               1 0
Basecase: if n <= 1, return 1. So if n is 0 or 1, that is a way of climbing the stairs
Answer: 7 ways
```

- Time Complexity: O(2^n) exponential, we end up repeating the same sub problem every time, e.g. above, starting from 4, how many ways to get from 1 to 0?

Similar to picture below, sub problem 2 is repeated twice. What if we just store it in cache so the calculation doesn’t repeat again?

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5cd80a82-d66a-4c6f-ad9f-0e46932ac8be/Untitled.png)

- Space Complexity: O(h) height of recursive stack

**Optimized Approach:** Bottom-up iterative approach, start at base case and work your way up.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f9480d24-eacb-432e-a725-d5c60826a20b/Untitled.png)

- ****Time Complexity: O(n), only solving each sub problem once using DP
- Space Complexity: O(n)

**Solution:** Building up from the base cases using a list to store results and returning the last calculated value as the number of ways to climb **`n`** stairs. 

**Unique uses:**

- The following two approaches can be vice versa:
    - Bottom up approach: iteratively
    - Top down approach: recursively
- GOTCHA moment: Base case would be 1,1 since there’s also one way of climbing 0 stairs which is doing nothing

## 746 - Min Cost Climbing Stairs

**Brute Force:**  Use recursion to calculate all sub problems for taking one step and taking two steps.

- Time Complexity: O(2^n), exponential since some sub problems repeat
- Space Complexity: O(h)

**Optimized Approach:** Use bottom up DP to find a relationship between sub problems.

See example of how it was solved here: [Example 2: Min Cost Climbing Stairs](https://www.notion.so/Example-2-Min-Cost-Climbing-Stairs-6401f12756914d30bee9c421a718a8a0?pvs=21) 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/31c526eb-11a0-4489-8c4e-107d0b0b7d0a/Untitled.png)

- ****Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Update an array with the cost for each step based on the cheaper cumulative cost of the two previous steps, concluding with the minimum of the last two calculated costs to account for the final step choice.

**Unique uses:**

- **DICTIONARIES DONT NEED TO BE NONLOCALIZED**
    - This is due to the fact that dictionaries are mutable, we are modifying the content rather than reassigning the cache variable itself

# Intervals

## 252 - Meeting Rooms

**Brute Force:**  Compare every interval with each other to see if there are overlaps

- Time Complexity: O(n^2)
- Space Complexity: O(1)

**Optimized Approach:** Sort the intervals by start time in ASC order then iterate

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/922fd683-0956-44c4-b54c-ec5702953c85/Untitled.png)

- ****Time Complexity: O(nlogn)
- Space Complexity: O(n)

**Solution:** Overlap = startTime2 < endTime1, since the 2nd class starts before the previous class ended.

**Unique uses:**

- Using lambda to sort
- Sort the intervals by start time allows us to not compare with every other interval because the next start times will be greater than the previous start times.
    - This means if the previous start time did not overlap, then that means the next start times could never overlap as well.

# Math & Geometry

## 202 - Happy Number

**Brute Force:**  Calculate the next number until it cycles or hits a 1 using a hashmap or set

- Time Complexity: O(n), calculate next digit using list comprehension. Uses math and array
- Space Complexity: O(n), uses sets

**Optimized Approach:** Use linked list cycle

- ****Time Complexity: O(n) calculate next digit using remainders and quotients
- Space Complexity: O(1), uses pointers

**Solution:** Implements the Floyd's Cycle Detection algorithm ("tortoise and hare") to efficiently determine if a number is happy by using a slow and fast pointer to detect cycles in the sequence of squared digit sums, concluding the number is happy if the process reaches 1.

**Unique uses:**

- Uses **divmod** function in python:
    - Divide by 10 → get quotient (last digit in a number)
    - Mod by 10 → get remainder (numbers last digit)