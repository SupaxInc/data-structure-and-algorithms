# Neetcode 150

**Brute Force:**  

- Time Complexity:
- Space Complexity:

**Optimized Approach:**

- ****Time Complexity
- Space Complexity:

**Solution:**

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