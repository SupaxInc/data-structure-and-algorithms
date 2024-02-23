# Neetcode 150

**Brute Force:**  

- Time Complexity:
- Space Complexity:

**Optimized Approach:**

- Time Complexity:
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

## 49 - Group Anagrams

**Brute Force:**  Sort the strings then compare each character in a string with all the other characters of other strings

- Time Complexity: O(n ^ 2 * nlogn)
- Space Complexity: O(n)

**Optimized Approach:** Sort the string and add the sorted string into a hashmap

- Time Complexity: O(n * m log m)
- Space Complexity: O(n)

**Most Optimized Approach:** Use a tuple of 26 length for alphabet characters as a key in the hashmap

- Time Complexity: O(n * m)
- Space Complexity: O(n)

**Solution:** Create an array of 26 length to represent the alphabet and use the ascii code of letter a to get the index position of the character you are on. Convert the array to tuple as a key to a hashmap.

**Unique uses:**

- Uses defaultdict
    - Helps optimize checking for existing keys
    - It’ll automatically create a new key for you without check if it exists
- Uses tuples as a key in a hashmap
- Uses sorted: sorted_string_case_insensitive = ''.join(sorted(my_string, key=str.lower))
    - Sorts characters in a string lexicographically

## 347 - Top K Frequent Elements

**Brute Force:**  Create a frequency map then sort the map

- Time Complexity:  O(n log n)
- Space Complexity: O(n)

**Optimized Approach:** Use a max heap to sort a key value pair of tuples or array

- Time Complexity: O(k * logn), mostly better than brute force IF k < n
- Space Complexity: O(n)

**Most Optimized Approach:** Use an array to bucket sort

- Time Complexity: O(k + n) → O(n) since we are doing more n operations and only adding k amount
- Space Complexity: O(n)

**Solution:** Use an array to bucket sort (index→count, value→[elements]), the length of the array will be the length of elements we need to count since the element can only show up length amount of times.

**Unique uses:**

- 1st approach:
    - Use a max heap to heapify the first value of tuple or array
- 2nd approach
    - A bucket sort is when you use the index of an array as the key and the value is the element of the index
        - In this case, you can use the key (index) as the frequency count then place an array in the index filled with elements that has the count
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/86e71971-75fe-4af2-b74a-4e46a3b5a639/Untitled.png)
        

## 238 - Product of Array Except Self

**Brute Force:**  Nested for loop

- Time Complexity: O(n^2)
- Space Complexity: O(n)

**Optimized Approach:** Calculate the product of all elements then divide by the element we are on. 

- Time Complexity: O(n)
- Space Complexity: O(n)

**Another Optimized Approach (w/o division):** We make two lists: one has the product of all numbers before each element, and the other has the product of all numbers after each element. Multiply the prefix and postfix for any element we are on, we get the product of all other numbers except the one we are on.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/69a6aabc-6ae9-4ad4-bdfb-cd45e159a16b/Untitled.png)

- Time Complexity: O(n)
- Space Complexity: O(n)

**A more optimized approach with better extra space complexity:** No need for prefix and product arrays, just calculate it within output array itself.

- Time Complexity: O(n)
- Space Complexity: O(1) since output array doesn’t count as extra space

**Solution:**  First calculate the prefix product into the result array then calculate the postfix product into the already calculated prefix result array.

**Unique uses:**

- Uses concept of prefix, postfix, and infix notation:
    
    ```python
    infix:    a + b
    prefix:   + a b
    postfix:  a b +
    ```
    

### Explaining 238 to interviewers

### **Understand the Problem**

Start by summarizing the problem to show you understand what's being asked:

- "The problem requires finding the product of all elements in an array except the current element, for each element, without using division. This means we need a way to 'exclude' the current element from the product calculation efficiently."

### **Identify the Constraints**

Highlight the constraints and why they guide your solution:

- "Since division is not allowed, we can't use the straightforward approach of calculating the total product and then dividing by the current element for each element in the array."
- "The need for O(n) time complexity suggests we can't afford nested loops, implying a single pass or linear solution."

### **Conceptualize the Core Idea**

Explain the core idea that led to your solution:

- "To 'exclude' the current element from the product, I thought about how we can accumulate products from both sides—left and right—of each element. **This way, for any given element, we can multiply the accumulated product from its left with the accumulated product from its right, effectively skipping the element itself."**
- "This approach is inspired by how prefix sums are used to calculate cumulative sums up to a point in an array. Similarly, we can calculate 'prefix products' and 'postfix products'."
    - **Prefix Sums**: This is a technique used in arrays to calculate the cumulative sum of elements up to a certain index. For example, given an array **`[a, b, c, d]`**, the prefix sum array would be **`[a, a+b, a+b+c, a+b+c+d]`**. This allows for efficient calculations of sums over a range of elements in an array.
        - **It is a useful strategy for various algorithmic problems that require efficient aggregate value calculations.**

### **Break Down the Solution**

Detail the steps of your solution:

1. **Prefix Products**: "First, we calculate the prefix product for each element, which is the product of all elements to its left. This can be done in a single pass from the beginning of the array."
2. **Postfix Products**: "Similarly, we calculate the postfix product for each element, which is the product of all elements to its right. This requires another pass, but from the end of the array backward."
3. **Combining Prefix and Postfix Products**: "Finally, for each element, we multiply its prefix product with its postfix product to get the desired result. This skips the product of the element itself, as neither the prefix nor postfix products include it."

### **Justify the Efficiency**

Explain why this solution is efficient and meets the constraints:

- "This solution requires only two linear passes through the array (one for prefix products and one for postfix products), plus an additional pass to calculate the final results, making it O(n) in time complexity. It meets the problem's constraints by not using division and efficiently calculating the result for each element."
- "While it uses extra space for the prefix and postfix product arrays, this trade-off is necessary to achieve the desired time complexity and avoid division."

### **Final Thoughts**

Conclude with any final insights or alternative considerations:

- "This solution demonstrates a balance between space and time complexity, leveraging the idea of cumulative products. It's a common strategy in problems where direct computation isn't feasible due to constraints like the prohibition of division."
- "Exploring variations of this problem could involve optimizing space usage further or considering edge cases, such as arrays with zeros, which this approach naturally handles well."

## 36 - Valid Sudoku

**Optimized Approach: Use a set to check if a value already exists**

- Time Complexity: O(9^2)
- Space Complexity: O(1)

**Solution:** Check duplicates for each rule by: Add values to a row using index of row were on as key, add values to a column using index of column were on as key, use integer division for each row and column to identify the 3x3 square (key = (r//3, c//3) we are on.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/05ecacab-086e-4894-bab3-002331ac6c93/Untitled.png)

**Unique uses:**

- Uses integer division to round down to nearest whole number,  effectively grouping a range of numbers into discrete buckets. In this case, 3x3 squares.
- Uses a tuple as coordinate keys

## 271 - Encode and Decode Strings

**Harder Approach:** Use a string delimiter such as “#” and if you see one in the original string just escape it.

**Issue:** Escape character may appear in original string, so we also have to escape the escape character

- Time Complexity: O(n)
- Space Complexity: O(n)

**Easier Approach:** Use the length of a string plus a string delimiter

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/57c9ef07-e57b-4299-8fa8-af5ba9ad8553/Untitled.png)

- Time Complexity: O(n)
    - Integer conversion from a string is generally O(m) where m is the number of digits, and since the lengths of strings being encoded/decoded are likely small relative to the total length of the input, their impact is minimal on the overall time complexity.
- Space Complexity: O(n)

**Solution:** “len(str)#” delimiter allows us to know the length of the string to slice the string that needs to be decoded.

**Unique uses:**

- Better than escaping characters “\#” which is more complex as we have to figure out a solution to escape escape characters
- Uses string.find(’#’, i) to get the index of a character in a string
- Uses string splicing

## 128 - Longest Consecutive Sequence

**Brute Force:**  Sort the array then check if each value is greater

- Time Complexity: O(nlogn)
- Space Complexity: O(1)

**Optimized Approach:** Use a hash set to check sequences

- Time Complexity: O(n)
- Space Complexity: O(2n) → O(n)
    - If a number is part of a sequence, it’ll be visited at most twice
    - But if its a sequence itself, then visited once

**Solution:** Using a hash set helps find left neighbors, if there aren’t it is the start of a sequence then we can loop to begin the consecutive sequence.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/577030d0-e93b-4132-b03e-b4f6eb467503/Untitled.png)

**Unique uses:**

- Uses a hash set

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

## 167 - Two Sum II, Input Array is Sorted

**Brute Force:**  Nested for loop, compare each number

- Time Complexity: O(n^2)
- Space Complexity: O(1)

**Optimized Approach:** Use left and right pointer

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Use a left and right pointer and compare the sum of both pointers to the target, right goes down if total is greater, left goes up if total is smaller.

**Unique uses:**

- Left and right pointer

## 11 - Container with Most Water

**Brute Force:**  Nested for loop, compare each number

- Time Complexity: O(n^2)
- Space Complexity: O(1)

**Optimized Approach:** Use left and right pointer

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Use a left and right pointer and find the area using min height to prevent water overflow. Move pointers based on which has smaller height

**Unique uses:**

- Left and right pointer

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

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c127af6e-5783-40bc-b948-294f031b0f9a/Untitled.png)

## 66 - Plus One

**Brute Force:**  Convert digits list to integer then add one then convert back to array (**not a very good way to solve problems and show off to interviewers**)

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach:** Reverse through an array to “carry a one” to digits with 9 value

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/e6181743-b45c-4ec5-adec-7751a48950cd/Untitled.png)

- ****Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Reverse the digits array to handle the carry operation, directly modifying the array when a digit is less than 9 or resetting digits to 0 when carrying over. Prepend a 1 to the array if all digits were 9.

**Unique uses:**

- Reversing an array from n to 0: **for i in range(len(digits)-1, -1, -1)**
- List concatenation since python doesn’t have a built in unshift method:
    - [1] + digits
    

# Bit Manipulation

**Guide: [How to Solve: Bit Manipulation](https://www.notion.so/How-to-Solve-Bit-Manipulation-8f8e50b940144e84b5eb6925ce4f4c7a?pvs=21)** 

## 136 - Single Number

**Brute Force:**  Use a hash set and remove the value if it shows twice. Check hash set at the end to see if there are dupes

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach:** Use bit manipulation

- ****Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Finds the single non-duplicate number in a list by XOR-ing all numbers, utilizing the property that a number XORed with itself cancels out, leaving only the unique number as the result.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/ff5b9543-20ce-4956-a3d4-084479c39fd5/Untitled.png)

**Unique uses:**

- Using XOR to manipulate all numbers in an array
    - **The XOR operation is commutative and associative, which means that the order in which you XOR the numbers does not matter.**
    - This allows you to XOR a set of numbers in any order and still get the same result.
1. **Pair Disappearance**: If you have two of the same number and you XOR them, they cancel out and give you 0. It's like they vanish!
2. **Lonely Number Stays**: Since pairs cancel each other out, if there's a number without a pair (a unique number), it won't disappear because there's nothing to cancel it out. So, after XORing everything together, this unique number is the only one left.
    
    

## 191 - Number of 1 Bits

**Brute Force:**  Iterate through the array and just count the 1’s

- Time Complexity: O(32) → O(1)
- Space Complexity: O(32) → O(1)

**Optimized Approach:** Use AND operator to check if right most bit is a 1

- Time Complexity: O(32) → O(1)
- Space Complexity: O(32)

**A more bit manipulation approach:** Use n = n & (n - 1)

- Subtracting value by 1 removes the right-most bit
    - Then AND operator filters it out from original value
- If subtracting by 1 does not remove right-most bit then it moves the 1’s over creating multiple 1’s since we subtracted the most significant bit
    - Then AND operator filters out the other 1 from the original value because it compares with the complement of 0s and 1s
- Each iteration we count

**Solution:** Use AND operator of the value with “1” → “0001”, checks if right most bit of a digit is a 1 then we shift >> the number by 1, to filter out the right-most digit. Cycle until 32 but is complete.

**Unique uses:**

- Uses shift operator and AND operator

## 338 - Counting Bits

**Brute Force:**  Create a list of n + 1 then convert to binary each iteration. Count the 1’s by doing 
n = n & n -1 similar to Leetcode 191. This will check if right most bit is a 1, if it is increment count then shift the bits to check the next right most bit.

- Time Complexity: O(nlogn), for every integer how many times can you divide it (or AND) it by 2?
- Space Complexity: O(n)

**Optimized Approach:** Use DP to find a sub problem that repeats for increasing digits.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d999c4d2-9030-4ba1-88b9-c5ade336322f/Untitled.png)

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** DP solution to count the number of 1 bits for all numbers up to **`n`**, leveraging the pattern that each number's 1 bits count is 1 plus the count of a previous number, determined by subtracting the most recent power of 2 (MSB) from the current number.

**Unique uses:**

- Uses DP to solve a bit manipulation problem using **most significant bit** as an offset

## 190 - Reverse Bits

**Brute Force:**  Manipulate it as a string and just reverse the string

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach:** Use shifts and bitwise operators to manipulate a new result array

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/90952219-5da7-4b62-9ad6-770760f1ab3e/Untitled.png)

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Reverses the bits of an integer by shifting the result leftward to accumulate each rightmost bit of the input number.

## 268 - Missing Number

**Brute Force:  Loop over 0 to n, use (if i not in nums) check which is an O(n) operation**

- Time Complexity: O(n^2) due to the check inside the for loop
- Space Complexity: O(1)

**Optimized Approach:** Use bit manipulation

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d480ec6a-bab5-4434-977e-9ab7f46b3c4c/Untitled.png)

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** 

- You can XOR all indices and values, including **`n`** (since the array is from **`0`** to **`n-1`**), and the result will be the missing number because the missing number will not be cancelled out.

**Unique uses:**

- Uses XOR
    - A number XOR itself gives 0.
    - A number XOR 0 gives the number itself.
    - XOR is commutative and associative.
- Use arithmetic series formula for summation optimized approach