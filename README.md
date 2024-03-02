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

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8adfa2cb-f5ca-43f5-a72d-83c09e5a3027/Untitled.png)

**Unique uses:**

- Left and right pointer

## 15 - 3Sum

**Brute Force:**  3 nested loops

- Time Complexity: O(n^3)
- Space Complexity: O(1)

**Optimized Approach:** 2 nested loops, 1 loop to iterate 1st index, another loop to iterate 2nd and 3rd index using two pointers

- Time Complexity: O(nlogn) + O(n^2) = O(n^2)
- Space Complexity: O(1)

**Solution:** Sort the numbers to easily find duplicates together, then use a loop for 1st index and a 2nd loop that has a two pointer approach to help reach target 0.

**Unique uses:**

- Two pointer approach to find if the target equals to 0
    - Uses a while loop to move the other pointers
- Sorting the array to easily find duplicates as neighbors.
    - Only need to find duplicates based on 1st and 2nd index
    - 3rd index is taken care of because at this point the left pointer has moved enough which means moving the right pointer to the same value will make the total too large. So if a duplicate is hit for the 3rd index, it wont matter as the total will still be too large.

# Sliding Window

## 121 - Best Time to Buy and Sell Stock

**Solution 1:**

**Brute Force[O(n^2)]:** Nested for loop  ****

**Optimized Approach[O(n)]:** Two pointers, 1 for loop

**Solution:** Sliding window two-pointer approach to find the maximum profit by buying low and selling high, dynamically updating the pointers based on the current and next day's prices.

**Unique Uses:**

- Uses a dynamic sliding window technique
    - It continues to slide the right side of the window until it hits some sort of parameter then moves the left side of the window

**Solution 2:**

**Brute Force[O(n^2)]:** Nested for loop  ****

**Optimized Approach[O(n)]:** For loop

**Solution:** Iteratively updates the lowest price seen so far and calculates the maximum profit possible at each step by comparing the current price with the lowest price.

## 3 - Longest Substring Without Repeating Characters

**Brute Force:**  Generate all possible substrings in a nested for loop using string[i:j+1] then generate a new set for each new spliced substring.

- Time Complexity: O(n^3), O(n^2) for generating all substrings, O(n) for generating a set for each new substring. Therefore, O(n^2) * O(n) = O(n^3)
- Space Complexity: O(n)

**Optimized Approach:** Use dynamic sized sliding window

- Time Complexity: O(2n), first for loop O(n) goes through all chars in string, second while loop that removes characters from the set could worst case be another O(n) if the entire string is entirely unique until the last character. Therefore, O(2n) = O(n).
- Space Complexity: O(n)

**Solution:** Use a dynamic sized sliding window, shrink it if the next character is already in a set, make it larger if its not in a set.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a41dd81f-fd3f-459d-ad8c-feb58ab095a5/Untitled.png)

**Unique uses:**

- Uses a dynamic sliding window with auxiliary
    - In this case it uses a hash set to check for duplicated characters
    - Uses a while loop with left pointer to shrink the sliding window

## 424 - Longest Repeating Character Replacement

**Brute Force:**  Find all substrings and check the max length of a non repeating character for each susbtring

- Time Complexity: O(n^3)
- Space Complexity: O(1)

**Optimized Approach:** Use a frequency map and keep track of the max count in the map.

- Time Complexity: O(n) for iterating over all chars in string + O(26) checking the max of counts every iteration for a total of 26 letters= O(26n) = O(n)
- Space Complexity: O(1)

**Most Optimized Approach:** Keep track of the max frequency character seen so far and no need to recalculate. If **`maxFreq`** were to be significantly overestimated, it would only temporarily allow a larger window, which is corrected by the while loop condition without needing to explicitly decrease **`maxFreq`**.

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** 

- Solution 1:  Keep track of the most frequent characters in a map, shrink the window if length of the window minus max count of the map is greater than K (the amount of letters we can replace) since max count is classified as the longest repeating character.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f8b86622-dae8-4442-bbb5-820e8f6cb4df/Untitled.png)

- Solution 2: Instead of calculating the max count every iteration, just keep track of the max frequency. All we really care about is which letter has the highest count in a given window since the max count that is first seen will always be the answer with the longest length of a valid window.

**Unique uses:**

- Uses dynamic size window with auxiliary

### Explaining 424 to interviewers to reach most optimal solution

### **Initial Approach Explanation**

1. **Initial Strategy**: Start by explaining your initial approach, emphasizing that you aimed to ensure correctness by dynamically calculating the count of the most frequent character in the window to determine if the window could be valid with at most **`k`** replacements.
2. **Identified Bottleneck**: Acknowledge that while the initial solution correctly solves the problem, you recognized a performance bottleneck. Specifically, recalculating **`max(count.values())`** for each iteration introduces unnecessary computational overhead, especially since this calculation is constant-time per iteration but multiplied across all **`n`** iterations, leading to O(26n) complexity.

### **Transition to Optimized Solution**

1. **Optimization Insight**: Explain that upon reviewing the problem, you realized that the key to optimizing was to reduce the repeated work done in calculating the maximum frequency character in each iteration. By maintaining the maximum frequency seen so far (**`maxFreq`**) as characters are added to the window, you could avoid recalculating the max frequency from scratch.
2. **Maintaining `maxFreq`**: Describe how, instead of finding the max count each time, you opted to update a **`maxFreq`** variable whenever a character's frequency in the current window exceeded the previously recorded maximum. This change means that you only need to calculate the character frequency when it could potentially increase the **`maxFreq`**, significantly reducing the number of operations.
3. **Adjusting the Window Based on `maxFreq`**: Clarify that with the **`maxFreq`** value, you could efficiently determine the window's validity by checking if the current window size minus **`maxFreq`** exceeded **`k`**. This check ensures that you're always working with a window that could potentially be made valid with up to **`k`** replacements.
4. **Window Shrink Logic**: Mention that when shrinking the window (by incrementing the **`start`** pointer), you didn't need to decrement **`maxFreq`** because the window's validity is determined based on the difference between the window size and **`maxFreq`**. This avoids the need for recalculating **`maxFreq`** when shrinking the window, further optimizing the solution.

## 567 - Permutation in String

**Brute Force:**  Use “from itertools import permutations” to generate permutations of the input string. Then check if all permutations are in s2 (O(n) operation).

- Time Complexity: O(n! * m) where m is length of s2 and n! is the possibilities of different permutations for a given string.
- Space Complexity: O(n!) since we may need to store n! strings.

**Optimized Approach:** Use two hashmaps to count frequencies between both strings then compare them.

- Time Complexity: O(26) + O(n) + O(m) = O(m) where m is length of s2. O(26) is comparing 26 keys between both hashmaps every iteration.
- Space Complexity: O(n)

**Most Optimized Approach:** Use 1 hashmap to count s1 letters then use a matches variable. 

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** 

- Solution 1: Use two hashmaps to count the frequency in a fixed window length based on string 1 length. Decrease count for s2 count when we move the window. Compare the two hash maps for a valid permutation if both character frequencies are the same.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/96b15fbb-ae73-4a20-95a4-203862571fd8/Untitled.png)

- Solution 2: Use one hashmap to count string 1 and have a new matches variable, decrease the counts in string 1 if its found in string 2. If the counts in string 1 becomes 0 then it matches, so increment the matches counter. If matches == length of string 1 then its a permutation.

**Unique uses:**

- Uses a matches variable to increment if a frequency count is 0 based on if its found on the valid window length
- Uses fixed sliding window

### What is a permutation?

A string permutation refers to any of the possible arrangements of its characters. For example, if you have the string "abc," its permutations include "abc," "acb," "bac," "bca," "cab," and "cba." In a broader algorithmic or combinatorial context, the term "permutation" can refer to the act of rearranging the elements of a set in all possible ways.

Similar to an anagram.

**Permutation Comparison**: Depending on the context, comparing string permutations might loosely imply checking if both strings contain the same set of characters without regard to order. It might not strictly require that the character frequencies match unless explicitly stated.

# Stacks

## 20 - Valid Parentheses

**Brute Force[O(n^2)]:** Nested for loop and counting open vs closing parentheses

**Optimized Approach[O(n)]:** Use a hashmap and stack

**Solution:** Uses a stack to ensure that each closing bracket correctly matches and properly follows its corresponding opening bracket, returning false if the stack is empty or the top of the stack doesn't match the expected opening bracket for a given closing bracket.

## 155 - Min Stack

**Brute Force:**  Use a min function for the entire stack array every time getMin is called

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach:** Use a second stack to place all the min numbers

- Time Complexity: O(1)
- Space Complexity: O(n)

**Solution:** Use two stacks, 1 for the actual stack, the other for the min numbers for the current position of the actual stack.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/dfa2452c-b65e-44bc-ac48-fcd614cf78dd/Untitled.png)

**Unique uses:**

- Uses a second stack to see what min number is within an array
- Compares with a positive infinite number to find the min number

## 150 - Evaluate Reverse Polish Notation

**Approach:** Use a stack

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Push numbers to the stack, pop the stack when an operator shows and perform the operation on the last 2 numbers (the 2nd popped number should be first in the operation). Push the result to the stack.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a2960a10-46a4-46f9-ab2c-fcb481deac55/Untitled.png)

**Unique uses:**

- Converts a floating point number to an int to truncate to 0
    - Floor division with //, is wrong here as it truncates to -Infinity
- isdigit() cannot be used to check if a string is a number as it only checks for 0-9

## 739 - Daily Temperatures

**Brute Force:** Nested for loop that checks current temperature across all temperatures except for current

- Time Complexity: O(n^2)
- Space Complexity: O(n)

**Optimized Approach:** Use monotonic decreasing stack

- Time Complexity: O(n)
    - While loop simply pops out stack elements one by one and there can’t be more than n elements pushed inside the stack as every element is pushed once. Therefore nested while loop will also not execute more than n times. The inner loop will not be counted as a nested loop until its covers n elements.
- Space Complexity: O(n)

**Solution:** Use a monotonic decreasing 2d array stack to help find the next greatest temp number. Check the top of the stack and pop when you find the next greatest number.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f9a49265-ddef-4476-b90d-9c15927237cb/Untitled.png)

**Unique uses:**

- 2D array helps keep track of what index the previous temp number was
- Monotonic decreasing stack is uses to maintain elements in a decreasing order from the bottom to top
    - In this specific problem, we use it to find the next greatest element of a previous temperature

## 853 - Car Fleets

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/fd8b7178-aeae-4c6e-b228-e6aa32b86a81/Untitled.png)

**Brute Force:**  Calculate the time using a sorted list of position and speed, then iterate through the times and count the new fleets.

- Time Complexity:  O(n), could become more expensive dealing with fleet mergers
- Space Complexity: O(n)

**Optimized Approach:** Use a monotonic decreasing stack 

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Zip the position and speed. Sort it to get cars beside each other to easily find which cars join a fleet. Calculate the time it takes for a car to reach target and push it to a stack if it is a fleet. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/709ef3ff-b3eb-43dd-972b-58461f88b809/Untitled.png)

**Unique uses:**

- Uses sorted and zip
    - Sorted sorts an iterable list like tuples, list, dictionaries, etc.
    - Zip combines two arrays by joining the elements in the same index as a tuple
- Uses reverse=True to reverse an array
- Uses a monotonic decrease stack algorithm to find the next greater element

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