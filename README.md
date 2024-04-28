**Intuition:** 

- Solutions
    
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

**Unique uses:**

- Mid number uses lo + ((hi+lo)//2) to prevent arithmetic overflow
    - Normal lo + hi // 2, could go over 32 bit integer limits

## 74 - Search a 2D Matrix

**Brute Force:**  Check if the highest value in each row is greater than the target, so we skip the current row and go to the next and binary search until we find a row that is not.

- Time Complexity: O(m * logn)
- Space Complexity: O(1)

**Optimized Approach:** Binary search the 2d array as a 1d flattened array since its essentially a sorted list without the 2d array

- Time Complexity: O(log m * n)
    - Treating the matrix as 1d array means the total length of the array is m * n
- Space Complexity: O(1)

**Solution:** Binary search a 2d flattened array, the mid index is a coordinate, and we can calculate the (y, x) coordinates to find the value in matrix[y][x].

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/46e8980f-aebe-4e8a-abc7-46539d97f651/Untitled.png)

**Unique uses:**

- Finds coordinates of an index in a 2d matrix
    - **y coordinate: index // n**
        - **`n`**, the number of columns, represents the width of each row.
        - Therefore, dividing a linear index (**`idx`**) by **`n`** gives you the row index because it tells you how many full rows you've "passed" to reach the position represented by **`idx`**.
            - For example, index = 6, number of columns = 4
                - 6 // 4 = 1, tells us that we’ve passed 1 full row of 4 columns.
    - **x coordinate: index % n**
        - We need to determine the position within the row.
        - The modulus operation (**`idx % n`**) gives the column index because it represents the remainder after dividing **`idx`** by the row width (**`n`**), indicating the offset from the start of the row.
            - For example, index = 6, number of columns = 4
                - 6 % 4 = 2, tells us the start of the row we’re in
- Flattening a 2d array as a 1d array

### Explaining 74 to an interviewer

### **Start with the Brute Force Approach**

1. **Initial Understanding**: Begin by explaining your initial approach to solve the problem directly based on the problem statement. For the "Search a 2D Matrix" problem, this might involve iterating over each row and then each column within that row to find the target. Acknowledge the straightforwardness of this method but also its inefficiency.
2. **Identify Limitations**: Discuss the limitations of the brute force approach, emphasizing its time complexity. For example, explain that searching every element in a matrix of size **`m x n`** results in a time complexity of O(m*n), which is not efficient for large matrices.

### **Transition to Optimization**

1. **Observation**: Share the key observation that led you to consider an optimized solution. For this problem, you might note that both the rows and columns of the matrix are sorted, which is a property that binary search can exploit to significantly reduce the search space.
2. **Conceptual Leap**: Explain the conceptual leap to treating the 2D matrix as a 1D sorted array. Emphasize how this perspective change allows you to apply binary search across the entire matrix, not just within a single row or column, thereby leveraging the sorted property of the matrix more fully.

### **Explain the Optimized Solution**

1. **Flattening the Matrix**: Describe how you "flatten" the matrix in a logical sense (without actually creating a new array) by mapping a 1D index to 2D row and column indices. Clarify the use of the formulas for row and column (**`row = idx // n`** and **`col = idx % n`**) and why dividing by the number of columns (**`n`**) correctly maps indices.
2. **Binary Search Application**: Detail how you apply binary search using the 1D index over the virtual flattened array. Highlight the reduction in time complexity to O(log(m*n)) because you're now performing a single binary search over the entire matrix, treating it as a sorted list.

## 875 - Koko Eating Bananas

**Brute Force:**  Create a K array (the amount of bananas Koko can eat per hour) from 1 to max of the piles then loop through each K per banana piles

- Time Complexity: O(p * max(P))
- Space Complexity: O(max(P))

**Optimized Approach:** Use binary search within a K array

- Time Complexity: O(p * log(max(P)))
    - Max of the piles since we know for sure the if bananas per hour eat speed is equal to the max piles. Koko would be able to hit the hour limit.
- Space Complexity: O(1)

**Solution:** Have a low and high pointer where it is the range of amount of bananas Koko can eat per hour. Binary search this range to find the min K to check if the hours to take to eat the piles is within the hour limit.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/cb83cbe7-f454-42b8-8b5e-ed5ad3ed286e/Untitled.png)

**Unique uses:**

- Loops through an array within a binary search
- Math.ceil to round up

## 153 - Find Minimum in Rotated Sorted Array

**Brute Force:**  Loop through entire array and calculate min each element

- Time Complexity: O(n)
- Space Complexity: O(1)

**Optimized Approach:** Use binary search

- Time Complexity: O(log n)
- Space Complexity: O(1)

**Solution:** Binary search to check if the middle number is greater than the end, if it is search left, else search right.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/ca01a870-b529-459e-9616-42cfcc7a1dda/Untitled.png)

**Unique uses:**

- Binary searching on a rotated sorted array
    - If the mid number is greater than end then it means its rotated in a way that the smaller numbers are on the left.
    - If the mid number is smaller than the end then it means its rotated where the smaller numbers are on the right.

## 33 - Search in Rotated Sorted Array

**Brute Force:**  Just iterate through array and find index of target

- Time Complexity: O(n)
- Space Complexity: O(1)

**Optimized Approach:** Use binary search

- Time Complexity: O(log n)
- Space Complexity: O(1)

**Solution:** Find out if you are in right or left sorted portion of the array. Binary search based on which side you are on and if target is on the rotated portion or if it is greater or less than our current mid index.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/08c16a56-47cc-4265-830e-632dbd508557/Untitled.png)

**Unique uses:**

- Binary searching a rotated sorted array
    - Checks which portion of the sorted array you are on

## 981 - Time Based Key Value Store

**Brute Force:** Just normally loop through the list of time map values

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach:** Binary search the list of time map values

- Time Complexity: O(log n)
- Space Complexity: O(n)

**Solution:** Timestamps are added strictly ascending, since its sorted we can binary search it. If the mid time stamp value is less or equal to target timestamp search on the right to find the highest previous time stamp.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/83d1294a-1368-430f-a8ce-3faa3b2820b2/Untitled.png)

**Unique uses:**

- Uses a hash table that maps values to a 2d array of value, timestamp pairing.
    - Timestamps are added ascending so we can binary search to find the highest previous time stamp or equal to target time stamp.
- Uses default dict

# Linked List

## 206 - Reversed Linked List

**Optimized Approach[O(n)]:** Normal traversal through a linked list

**Solution:** Point a temp pointer to ****the next current node then using the next node of the current node to point to the previous node effectively creating a reversal. The current node then becomes the temp pointer to restart the process again. 

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

## 143 - Reorder List

**Brute Force:**  Convert linked list to array, reorder the array, rebuild the linked list

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach:** Re-build linked list in-memory

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Find mid point using slow and fast pointers, get second list from slow pointer, reverse second list, then merge the lists.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/fa7d1b48-e72c-4815-8787-405be58f4090/Untitled.png)

**Unique uses:**

- Slow and fast pointers to find mid point of a linked list
- Rebuilding a linked list in memory by referencing the head to new variables and variable point to new places in memory
- Reversing a linked list
- Merging two linked lists together using 2 temp pointers

## 19 - Remove Nth Node from End of List

**Brute Force:**  Reverse the list

- Time Complexity: O(n)
- Space Complexity: O(1)

**Optimized Approach:** Use two pointers, similar to slow and fast pointers

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Slow and fast pointer approach but the fast pointer does not go faster, it just gets a head start of nth times. Slow pointer will end up at target node, so we need a dummy node that points to the head.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8cbd93cc-16f9-44e0-908d-29a9abf1ee08/Untitled.png)

**Unique uses:**

- Slow and fast pointer approach to get nth node from end.
    - Slow ends up at target node since fast pointer has a head start of nth amount
- Uses a dummy node so our slow pointer doesn’t end up at target that we need to remove

## 2 - Add Two Numbers

**Optimized Approach:** Normal traversal

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Adds two numbers (long addition) represented by two linked lists, digit by digit, taking care of carries and remainders, and returns the sum as a new linked list. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8249d086-8e8e-46ab-b188-8c51e8aff9dc/Untitled.png)

**Unique uses:**

- Checks if the total number has a carry associated with it (long addition), you can do this with floor division
    - Adds the carry to next node over
    - A carry may go through at the end of a list which is an edge case. So we have to add a new node of 1
- Checks for remainder using mod to get the 2nd digit of a number greater than 9 (e.g. 11 % 10 = 1)
- Uses dummy node to have a reference of the head of the node were traversing through

## 287 - Find the Duplicate Number

**Brute Force:**  Use a hashmap

- Time Complexity:  O(n)
- Space Complexity: O(n)

**Optimized Approach:** Use a “linked list”

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Use the indices as a “pointer” to connect to other indices. Detect the cycle and find the intersection point. Then find the cycle entry point by starting from the beginning and from the cycle intersection point 1 by 1. The distance between intersection and entry point is the same ( p = c - x). 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/296644c2-1bf3-4636-adbf-3ad0ee0c74f3/Untitled.png)

**Unique uses:**

- Pretends a list is a linked list by using the indices as pointers
- The cycle entry point is the duplicate number value
    - To find entry point, we move 1 by 1 from the beginning and the cycle intersection point
    - Using mathematical proofs, the distance between entry and intersection is the same, thus finding the cycle entry point.

## 138 - Copy List with Random Pointer

**Optimized Approach:** Use a hashmap 

- Time Complexity: O(n) + O(n) = O(n)
- Space Complexity: O(n)

**Solution:** Use a hashmap to map old current nodes to new nodes. 1st iteration will map with just values, 2nd iteration will map next and random pointers. Two iterations is needed as random pointers could map to non-existent nodes.

**Unique uses:**

- Uses a dictionary as a key in a hash map
- The hash map maps the new copied node as value so it allows us to map next nodes and random nodes
    - Mapping in just 1 iteration is not possible as we could map to non-existed forward nodes in the singly linked list

## 146 - LRU Cache

**Optimized Approach:** Use a hashmap and doubly linked list

- Time Complexity: O(1)
- Space Complexity: O(n)

**Solution:** Use a doubly linked list to access LRU (head) and MRU (tail). Use a hashmap to map a key to a node, helps to also access a node in O(1) time in the list, faster removal and access.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c8ffa08e-e57e-4293-885e-2f20a7e14f54/Untitled.png)

**Unique uses:**

- Uses a dictionary to map keys to a node for faster access to a node in a doubly linked list
- Uses a doubly linked list to keep track of LRU (head) and MRU (tail)
- Uses a dummy node for head and tail to prevent null pointers
- Uses LRU eviction, when at capacity it evicts the LRU

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

## 235 - Lowest Common Ancestor of a Binary Search Tree

**Optimized Approach:** Just traverse down the tree iteratively

- Time Complexity: O(n)
- Space Complexity: O(1)

**Solution:** Traverse from the root and moving left or right depending on the nodes' values, stopping when it finds the first node that is between the two target nodes or equal to one of them, leveraging the BST property where left nodes are less than the parent and right nodes are greater.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/7269b7e8-a930-4590-bc06-b8cc4c93755f/Untitled.png)

**Unique uses:**

- Does not use BFS or DFS to go down a tree, just go down from the root and find where to go depending on which node values are greater
- A lowest common ancestor is based on two cases:
    - If the node is between two target nodes so they are in different sub trees
        - Different subtrees means that we can’t find deeper common ancestors
    - If the node is equal to one of the target nodes
        - A node can be a descendant of itsself

## 102 - Binary Tree Level Order Traversal

**Optimized Approach:** BFS level order traversal

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Have a for loop that will traverse through all nodes in current level first before moving to next level with the queue

**Unique uses:** 

- Traverses through entire level first in BFS as opposed to looking through next level

## 98 - Validate Binary Search Tree

**Optimized Approach:** DFS

- Time Complexity: O(n)
- Space Complexity: O(h)

**Solution:** Validate the range of each current node value between low and high values. Going left means change high value (node in left subtree must have values less than current node) and going right means change low value (node in right subtree must have values greater than current node)

**Unique uses:** 

- We pass parameters to the recursive call so that it resets to previous value when the stack pops

### Explain 98 to interviewer

1. **Start with the BST Property**: Begin by stating the BST property clearly - for any node in a BST, all nodes in its left subtree must have values less than the node’s value, and all nodes in its right subtree must have values greater. Highlight that this property must hold not just between direct parent-child nodes but for all ancestor-descendant relationships.
2. **Introduce the Recursive Strategy**: Explain that you'll use a recursive depth-first search strategy to traverse the tree. Mention that the key to this approach is carrying along the maximum and minimum values a node can have, which are determined based on its position relative to its ancestors. This ensures that the BST property is validated not just locally but throughout the entire path from the root to each leaf.
3. **Describe the Helper Function**: Clarify that you've defined a helper function, **`validate`**, which checks if a node's value falls within a valid range (**`low < node.val < high`**). The function starts at the root with the range set to negative and positive infinity, meaning any value is initially valid.
4. **Explain the Recursion and Range Updates**: Detail how, for each node visited, the function makes two recursive calls - one for the left child and one for the right child. For the left child, the function updates the **`high`** limit to the current node's value because everything in the left subtree must be less than the current node. Similarly, for the right child, it updates the **`low`** limit to the current node's value. This dynamically adjusts the valid value range as the recursion moves deeper into the tree.
5. **Highlight the Base Case and Validation Logic**: Mention the base case of the recursion - when a node is **`None`**, indicating a leaf's child has been reached successfully, and thus, that path is considered valid. Then, emphasize that if a node falls outside its valid range, the tree violates the BST property, and the function returns **`False`**.
6. **Combining Results with Logical AND**: Explain that both the left and right subtrees must validate for the tree to be considered a BST. This is achieved through a logical AND between the results of the recursive calls. If either side returns **`False`**, the entire subtree is invalid.
7. **Final Result**: Conclude by stating that the recursion starts at the root and explores every path, ensuring every node meets the BST criteria based on its position. The initial call to the helper function thus determines whether the entire tree is a valid BST.

## 199 - Binary Tree Right Side View

**Optimized Approach:** BFS level order traversal

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Use level order traversal BFS and grab the value of the last node in the level using the index and length of queue. Allows us to see only nodes from the right side POV.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/69ab5337-7209-40a9-b106-27a2c9fae2e0/Untitled.png)

**Unique uses:** 

- Traverses through entire level first in BFS as opposed to looking through next level

## 1448 - Count Good Nodes in Binary Tree

**NOTE: GREAT IF YOU WANT TO UNDERSTAND HOW VALUES ARE PROPAGATED**

**Optimized Approach:** DFS traversal

- Time Complexity: O(n)
- Space Complexity: O(h)

**Solution:** Use preorder DFS to be able to find the max for the current path as it resets each propagation to previous value that was passed to prevent the max for being counted along other paths. The propagated return value would be the count as we need the accumulated count for both sub trees.

**Unique uses:** 

- Traverses through using preorder DFS
    - Allows us to accumulate the propagated count from both left and right subtrees

## 230 - Kth Smallest Element in Tree

**Optimized Approach:** Iterative DFS or Recursive DFS

- Time Complexity: Same time complexity O(n)
- Space Complexity: Iterative may have better space complexity due to non-recursive calls

**Solution:** Use Inorder traversal and have a counter to check if it equals Kth number. 

**Unique uses:**

- Uses iterative DFS
- Uses Inorder traversal

## 105 - Construct Binary Tree from Inorder and Preorder Traversal

**Not Optimized Approach:** Using .index() every recursive call

- Time Complexity: O(n^2)
- Space Complexity: O(n)

**Optimized Approach:** Mapping index instead of using .index()

- Time Complexity: O(n)
- Space Complexity: O(n)

**Solution:** Identify the root from the preorder list, finding its position in the inorder list to divide the tree into left and right subtrees, and then recursively doing the same for each subtree.

**Unique uses:**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/321be0a3-5d92-4bbb-af62-ff1875216ad5/Untitled.png)

- First value in **Preorder** is the root node
- The first value will be a middle value in **Inorder**
    - Left side of middle is left sub tree, right side is right sub tree
- How to partition:
    - The size of the sub arrays in Inorder array tells us how to partition the Preorder array
    - It’ll tell us how much length to cut from the preorder array
    - We will recursively run on the left and right sub array of the Preorder array
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/80b1a0f0-833d-4ed4-b208-2a28d694c6da/Untitled.png)
    
- Uses list slicing
    - Preorder List Slicing
        1. **`preorder[1:mid+1]`**:
            - This slice is intended to get the elements of the left subtree.
            - The **`1`** indicates that we start from the element right after the root node in the preorder list since the first element (**`0`** index) is the root.
            - **`mid+1`** indicates the end of the slice. Since slices are exclusive on the end, **`mid`** corresponds to the number of elements in the left subtree, which is the same as the position of the root in the inorder list. The slice goes up to, but does not include, **`mid+1`**, effectively capturing all elements that belong to the left subtree according to the preorder sequence.
                - For example the first left sub tree would pass in [9]
        2. **`preorder[mid+1:]`**:
            - This slice selects the elements of the right subtree.
            - Starting from **`mid+1`**, it includes all elements from that position to the end of the list. These elements are part of the right subtree, following the root-left-right order of preorder traversal.
    - Inorder List Slicing
        1. **`inorder[:mid]`**:
            - This slice gets all elements before the root in the inorder traversal, which correspond to the left subtree.
            - **`:mid`** means it starts from the beginning of the list up to, but not including, **`mid`**, the position where the root element is found. These are all the elements that belong to the left subtree.
        2. **`inorder[mid+1:]`**:
            - This slice is for the elements after the root in the inorder list, which belong to the right subtree.
            - **`mid+1:`** starts the slice from the element right after the root and includes everything to the end of the list. This captures the entire right subtree.
- How it all works:
    
    ### **Slicing for Left Subtree**
    
    - **Preorder for Left Subtree**: We take elements from the preorder list that belong to the left subtree: **`preorder[1:mid+1]`** → **`preorder[1:2]`** → **`[9]`**. This indicates that **`9`** is the root (and the only node) of the left subtree.
    - **Inorder for Left Subtree**: Similarly, we take elements before the root **`3`** in the inorder list for the left subtree: **`inorder[:mid]`** → **`inorder[:1]`** → **`[9]`**. The left subtree consists of a single node **`9`**, confirmed by both lists.
    
    ### **Slicing for Right Subtree**
    
    - **Preorder for Right Subtree**: For the right subtree, we take the remaining elements in the preorder list after those belonging to the left subtree and the root: **`preorder[mid+1:]`** → **`preorder[2:]`** → **`[20, 15, 7]`**. This indicates that **`20`** is the root of the right subtree, with **`15`** and **`7`** as its children.
    - **Inorder for Right Subtree**: For the right subtree in the inorder list, we take elements after the root **`3`**: **`inorder[mid+1:]`** → **`inorder[2:]`** → **`[15, 20, 7]`**. This confirms the structure of the right subtree, with **`20`** as the root and **`15`** and **`7`** as left and right children, respectively.
    
    ### **Recursive Construction**
    
    Using these sliced lists, the algorithm recursively constructs the left subtree with **`[9]`** and the right subtree with **`[20, 15, 7]`** using the same process:
    
    1. For the left subtree **`[9]`**, there's no further subdivision since it's a single-node subtree.
    2. For the right subtree **`[20, 15, 7]`**, **`20`** is identified as the root in the next recursive call, and further slicing is used to construct its left and right children (**`15`** and **`7`**).

# Tries

## 208 - Implement Trie (Prefix Tree)

**Brute Force:  Use a hashmap as a children property of Trie Node**

- Time Complexity: O(n)
- Space Complexity: O(n)

**Optimized Approach: Use an array of 26 size as children**

- Time Complexity: O(n)
- Space Complexity: O(26)

**Solution: O**ptimizes for lowercase English letters by using a fixed-size array of 26 for children nodes, allowing for efficient insertions, searches, and prefix checks by calculating character positions based on ASCII values.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8ad94c95-2f6a-4c5e-a643-2d1e1bf282f5/Untitled.png)

**Unique uses:**

- Each trie node consists of a children and an end property
    - Contains children as there could be multiple words with different combinations
    - Contains end property to let us know that it was inserted as a word, helps for searches
- Uses an array with a prefix sized amount of 26 to imitate the alphabet letters
    - Index is found by subtracting ASIIC value of “a” and the char we are on

## 211 - Design Add and Search Words Data Structure

**Brute Force:**  Create a list of all inserted words then search them 1 by 1

- Time Complexity: O(n * l * m) where N is # of words, L is length of words, M length of word being searched if it contains wildcards (.)
- Space Complexity: O(n)

**Optimized Approach:** Create a trie

- Time Complexity: O(n*26^L)
    - Complexity explanation
        
        Means for of *N* items, the algorithm might perform operations on all possible combinations of characters up to length *L*, with each character having 26 different choices (like the letters in the English alphabet). This complexity grows quickly with *L*, as every additional character multiplies the number of possibilities by 26
        
- Space Complexity: O(n)

**Solution:**

**Unique uses:**

- Uses backtracking or DFS to go back up a node to check other children nodes in a Trie if the search has failed for the child node we went down

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

## 972 - K Closest Points to Origin

**Brute Force:**  Sort the results of the Euclidean distance to get smallest of K closest points

- Time Complexity: O(nlogn)
- Space Complexity: O(n)

**Optimized Approach:** Use a min heap

- Time Complexity: O(n), heapify
- Space Complexity: O(n)

**Solution:** Finds the k closest points to the origin by calculating their Euclidean distances, adding them to a min heap, and then extracting the k points with the smallest distances.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f08a92a6-8e4d-4cbb-92f8-225b198b3e21/Untitled.png)

**Unique uses:**

- Uses a tuple in a min heap to store the key (in this case the coords) with the value
    - Heapify will only sort the first value in a tuple or array

## 215 - Kth Largest Element in an Array

**Brute Force:**  Sort the array or create a max heap

- Time Complexity: O(nlogn)
- Space Complexity: O(n)

**Optimized Approach:** Create a min heap

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/38ece84c-2f4c-4e48-a832-04351aa91927/Untitled.png)

- Time Complexity: O(k) + O((n-k) log k)
    - O(k), heapify an array of k size
    - O((n-k) log k), heappushpop heap of size of n-k
- Space Complexity: O(k), min heap storage

**More Optimized Approach:** Quick Select (similar to quick sort)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/7e3e82b2-8726-4a35-bb78-0ae589222448/Untitled.png)

- Time Complexity: O(n), worst case O(n^2)
- Space Complexity: O(n)

**Solution:** Maintains a min heap of size **`k`** to efficiently find the kth largest element in an array by ensuring only the k largest elements remain in the heap, returning the smallest among them as the kth largest overall.

**Unique uses:**

- Uses heappushpop operation on n-k size of min heap: O(log n) operation
    - Pushes the value to min heap, then pops smallest value of min heap
    - Helps sort the heap to get the Kth largest elements
- Using quick select over heap sort
    - Faster than heap sort
    - Not a stable algorithm
    - Used more than heap sort if you don’t care about worst case time complexity
- Quick select vs Quick sort
    
    ### **Quick Sort:**
    
    - **Purpose**: Quick Sort is a sorting algorithm used to order all elements in an array from smallest to largest (or vice versa).
    - **Process**: It picks an element as a pivot and partitions the given array around the picked pivot, ensuring that elements less than the pivot end up on the left side of the pivot and elements greater than the pivot end up on the right side. This partitioning is done for each sub-array around a new pivot until the entire array is sorted.
    - **Complexity**: The average time complexity of Quick Sort is *O*(*n*log*n*), though its worst-case complexity can degrade to *O*(*n*2) if not carefully implemented (e.g., always choosing the first or last element as the pivot in a sorted array).
    - **Entire Array**: Quick Sort is applied to the entire array, and its goal is to sort the whole dataset.
    
    ### **Quick Select:**
    
    - **Purpose**: Quick Select is used to find the kth smallest (or largest) element in an unsorted array. Unlike Quick Sort, it does not sort the entire array.
    - **Process**: Like Quick Sort, Quick Select uses a pivot selection and partitioning strategy. However, after partitioning, Quick Select only recurses into one side of the pivot—the side that contains the kth smallest element—ignoring the other side. This selective recursion significantly reduces the number of elements it needs to process.
    - **Complexity**: The average time complexity of Quick Select is *O*(*n*), making it faster for its specific task than sorting the entire array and then selecting the kth element. However, its worst-case complexity can also be *O*(*n*2), particularly with poor pivot choices.
    - **Specific Element**: Quick Select focuses on finding a single specified element's position (kth smallest or largest) without sorting the entire array.

## 621 - Task Scheduler

**Intuition:** The core idea is to arrange tasks so that the same tasks are spaced out by at least **`n`** intervals, with the most frequent tasks shaping the schedule's minimum length. Place the most frequent tasks first, separated by **`n`** spaces, then fill those spaces with other tasks, ensuring no idle time if possible. The challenge lies in efficiently filling these cooldown periods to minimize the total schedule time.

- Solutions
    
    **Optimized Approach:** Use a max heap and a queue
    
    - Time Complexity: O(26 + 26 log 26)
    - Space Complexity: O(n)
    
    **Solution:** using a max heap for managing task frequencies and a cooldown queue, ensuring tasks are executed with a minimum interval **`n`**, and calculates the total execution time by dynamically adjusting tasks' availability based on cooldown requirements.
    
    **Unique uses:**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/de2ecef2-077b-4b41-9956-30b99e2fe08d/Untitled.png)
    
    - Uses a max heap to store the frequency of counts
    - Uses a queue so we can execute next tasks when idle time is finished

## 355 - Design Twitter

**Intuition:** Create a simplified model of Twitter where users can post tweets, follow/unfollow each other, and view the 10 most recent tweets in their newsfeed.

- Solutions
    
    **Brute Force:**  Compare each recent tweet for every user in a normal loop
    
    **Optimized Approach:** Just add each recent tweet for every user in a max heap
    
    - Time Complexity: O(K log n), each pop operation is log n and we do it at most 10 times
    - Space Complexity: O(n)
    
    **Solution:** Uses a heap to manage the most recent tweets from a user and their followees, allowing efficient retrieval of the top 10 latest tweets for any user's news feed, while also supporting follow and unfollow operations with a follower map.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/40c5b4ef-c9af-4025-a060-79f0bd6609be/Untitled.png)
    
    **Unique uses:**
    
    - Similar to merge k sorted lists question
        - Grab each recent tweet in a heap and add the last index and following id to grab next recent tweets
        - Makes it much more optimized so if there are 10 users, we could grab all 10 recent tweets.
        - Then pop each 10 recent tweets and check if the user’s next tweet is more recent
    - Uses a list to get most recent tweet from a user
    - Uses a set to get what users someone has followed
    - Could use nlargest or heapq.merge in a different solution

# Backtracking

## 78 - Subsets

**Intuition:** Systematically explore all combinations of numbers in a given list by including or excluding each number, using recursion to navigate through these choices and generating all possible subsets.

- Solutions
    
    **Brute Force:** Use back tracking
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)
    
    **Solution:** Generates all possible subsets of a given list by using backtracking to explore every combination of inclusion and exclusion of each element, starting with an empty subset and adding elements one by one.
    
    ```python
                         []
                       /    \
                  [1]Y        N[]
                 /   \       /   \
           [1,2]Y    N[1]  [2]Y   N[]
             /  \    /  \   /  \   /  \
    [1,2,3]Y N[1,2]Y N[1]Y N[1,3] [3]Y  N[]
    ```
    
    **Unique uses:**
    
    - Uses list[:] to deep copy a list
    - Backtracking to try all possible combinations of choices
        - No base cases to prune as the only constraint is the length of the array

## 39 - Combination Sum

**Intuition:** Find all unique combinations in a list of numbers that sum up to a target number. You can use each number as many times as needed. 

- Solutions
    
    **Brute Force:** Use backtracking
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)
    
    **Solution:** Generates all unique combinations of numbers that sum up to a target, utilizing backtracking to explore every combination with duplicates allowed and pruning paths exceeding the target.
    
    ```python
    Start with an empty path [] and target 7.
    
                             []
    
                 /           |            \           \
               [2]          [3]           [6]         [7]
           /    |   \        | \           |           |
         [2,2] [2,3][2,6]  [3,3][3,6]    [6,6]        [7,7]
        /   |
     [2,2,2][2,2,3]
      |
    [2,2,2,2]
    
    - [2,2,2,2] exceeds the target, so we backtrack.
    - [2,2,3] exactly meets the target, so we add it to our result.
    - [2,3], [2,6], and [3,3] branches are pruned as they exceed the target.
    - [3,6] exceeds the target, so it's not explored.
    - [6,6] exceeds the target, so it's not explored.
    - [7] meets the target, so it's added to our result.
    
    Constraints:
    - Total cannot exceed target, prune search
    - Index cannot exceed length of number array (for loop)
    ```
    
    **Unique uses:**
    
    - Passes a parameter to a recursive function to keep track of it instead of re-initializing every time
    - Stays on current index in back tracking so we can have duplicates until combination is greater than target then prune the search

## 46 - Permutations

**Intuition:** Explore all possible ways to arrange a set of numbers, ensuring every number is used exactly once in each arrangement.

- Solutions
    
    **Brute Force:** Use backtracking
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)
    
    **Solution:** Swap each number into the "current" position, recursively generating permutations of the remaining numbers, and backtracking to undo swaps for the next iteration.
    
    ```
                                    [1, 2, 3]
                            /           |           \
                          /             |             \
                    [1, 2, 3]        [2, 1, 3]       [3, 2, 1]
                    /     \            /     \           /     \
                  /       \          /       \         /       \
            [1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 2, 1] [3, 1, 2]
    Constraints: A number cannot appear more than once
    Base case: Stop when the current index has same length as input set
    First choice (inclusion): Swap current index
    Second choice (exclusion): Undo swap
    ```
    

## 90 - Subsets 2

**Intuition:** Generate all possible unique subsets from a list that may contain duplicates.

- Solutions
    
    **Brute Force:** Use backtracking
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)
    
    **Solution:** Generates all unique subsets from a sorted list by using backtracking to include or exclude elements, while skipping duplicates to avoid identical subsets.
    
    ```
                    []
                  /    \
                [1]    []
              /    \     
            [1,2]  [1]    
           /    \     
       [1,2,2]  [1,2] 
    ```
    
    - Explanation:
        - At the root, we decide to include or not include **`1`**.
            - Including **`1`** moves us down the left branch to **`[1]`**.
            - Not including **`1`** keeps the subset empty, moving us down the right branch to **`[]`**.
        - At **`[1]`**, we decide to include the first **`2`** or not.
            - Including the first **`2`** moves us to **`[1,2]`**.
            - Not including the first **`2`** keeps us at **`[1]`**.
        - At **`[1,2]`**, we face a decision with the second **`2`**, which is a duplicate.
            - Including the second **`2`** moves us to **`[1,2,2]`**. This is allowed because we included the first **`2`**.
            - Not including the second **`2`** keeps us at **`[1,2]`**.
    
    **Unique Uses:**
    
    - Sorting the number first helps us find duplicates adjacent to each other

## 40 - Combination Sum 2

**Intuition:** Find all unique combinations of candidates that sum to a target number, with each candidate used once per combination.

- Solutions
    
    **Brute Force:** Use back tracking
    
    - Time Complexity: O(2^n) * n log n
    - Space Complexity: O(n)
    
    **Solution:** Sort the input to handle duplicates and explore all possible combinations that sum to the target, excluding duplicates by skipping over same consecutive elements after each backtrack step.
    
    ```
    Start with sorted array: [1,2,2,2,5]
    Target = 5
    
    []
    └── [1] (target now 4)
        ├── [1,2] (target now 3)
        │   ├── [1,2,2] (target now 1) X (exceeds target with next number)
        │   └── [1,2,2] (skipped due to duplicate)
        └── [1,2] (move to next distinct number, which is 5)
            └── [1,5] X (exceeds target)
    └── [2] (target now 3)
        ├── [2,2] (target now 1)
        │   └── [2,2,1] = 5 (Valid Combination, Add to result)
        └── [2,2] (skipped due to duplicate)
    └── [2] (skipped due to duplicate)
    └── [2] (skipped due to duplicate)
    └── [5] (target now 0)
        └── [5] = 5 (Valid Combination, Add to result)
    
    Valid combinations found: [[2,2,1], [5]]
    ```
    
    **Unique uses:**
    
    - Sort the input set so adjacent duplicates are beside each other.
        - Helps prevent duplicate results when we backtrack and pop, we check the next index num. Similar to problem 3Sum.
    - Prune search space after finding valid combination.
        - Avoids identical subsets that lead to same sum

## 79 - Word Search

**Intuition:** Visualize the grid as a maze where each cell's letter is a path you can follow, and your goal is to string together a path that spells out the target word. Each step can move to adjacent cells (up, down, left, right) but can't revisit cells used in the current spelling attempt.

- Solutions
    
    **Brute Force:** Backtracking
    
    - Time Complexity: O(4^k) * O(m*n)
        - O(4^k) → k is the length of target word, 4 is because we have up, left, right, down directions to explore to as deep as possible
        - O(m*n) → Counting frequencies for the entire board
    - Space Complexity: O(n)
    
    **Solution:** Uses DFS and backtracking to explore all possible paths on a board to find a given word, reversing the word for efficiency if its first letter is more common than its last, and marking visited cells temporarily to avoid revisiting them during the search.
    
    **Unique uses:**
    
    - count = defaultdict(int, sum(map(Counter, board), Counter()))
        - map(Counter, board) → Creates a counter frequency dictionary for all board rows
        - sum(map(Counter, board), Counter()) → Sums all counters into one counter
        - defaultdict → Initializes a dictionary with the summed counter of all freqs for all rows
    - Uses DFS on a 2d matrix
        - Uses directions for up, left, right down
        - Marks a node as visited

## 131 - Palindrome Partitioning

**Intuition:** Explore all substring combinations of a given string, identifying and collecting those sequences where every substring is a palindrome.

- Solutions
    
    **Brute Force:** Backtracking
    
    - Time Complexity: O(n * 2 ^ n)
        - O(2^n), for each character there’s a choice to partition or not
        - O(n), to check if the substring is a palindrome
    - Space Complexity: O(n)
    
    **Solution:** Use backtracking to partition a string into all possible palindromic substrings by exploring inclusion and exclusion choices for substrings verified as palindromes.
    
    ```
    []
    |
    ├─ [a]
    |  |
    |  ├─ [a, a]
    |  |  |
    |  |  └─ [a, a, b]  <- Valid palindrome partition
    |  |
    |  └─ [a, ab]       <- 'ab' is not a palindrome, stop exploring this branch
    |
    ├─ [aa]
    |  |
    |  └─ [aa, b]       <- Valid palindrome partition
    |
    └─ [aab]             <- Not a palindrome, stop exploring this branch
    
    The choices we have are the palindrome substrings
    Constraint is if we end up 
    ```
    
    **Unique uses:**
    
    - Two pointer approach to find palindromes
    - The choices for back track are the palindromes using a for loop of start and end

## 17 - Letter Combinations of a Phone Number

**Intuition:** Iterate through each digit, use the digit-to-letter map to generate all possible letter sequences.

- Solutions
    
    **Brute Force:** Backtracking
    
    - Time Complexity: O(4^n) → worst case input: “9999” = 4 x 4 x 4 x 4
    - Space Complexity: O(n)
    
    **Solution:** Map each digit to its corresponding letters, then recursively explore all letter combinations, advancing one digit at a time.
    
    ```
            root
            /  \
           a    b    c  <- digits for '2'
          /|\  /|\  /|\
         d e f d e f d e f <- digits for '3'
    Choices -> Letters for current digit
    Constraints -> Path combination can't be larger than digits
    ```
    
    **Unique uses:**
    
    - Exclusion choice for back track happens when call stack pops as path combinations is part of the parameter so no need to pop in loop

# Graphs

## 200 - Number of Islands

**Intuition:** Count the number of connected groups of '1's (islands) in a 2D grid by marking visited parts to avoid recounting.

- Solutions
    
    **Brute Force:** Nested for loop
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Optimized Approach:** DFS or BFS grid traversal
    
    - Time Complexity: O(m * n)
    - Space Complexity: O(n) or O(h)
    
    **Solution:** Use DFS or BFS to “sink” islands so that it is easier to count islands that have not been sunk. 
    
    **Unique uses:**
    
    - Used DFS or BFS to find all adjacent 1’s then sinks them so that other 1’s that are alone can be found.

## 133 - Clone Graph

**Intuition:** Clone a graph by creating copies of each node and their connections, ensuring duplicates maintain the original structure.

- Solutions
    
    **Optimized Approach:** DFS or BFS with hash map
    
    - Time Complexity: O(N + E), N is total number of nodes, E is edges
        - O(N) → we visit each node in the graph
        - O(E) → each node we visit all of its neighbors to clone the edges
    - Space Complexity: O(n)
    
    **Solution:** Clone a graph using DFS by mapping nodes to their copies and recursively connecting neighbors.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/18888442-afab-40f3-8b7c-aacb3178606a/Untitled.png)
    
    **Unique uses:**
    
    - Using a hash map to map old nodes to new nodes to create a deep copy of a graph

## 695 - Max Area of Island

**Intuition:** Find the largest connected area of '1's in a grid using traversal techniques like DFS or BFS.

- Solutions
    
    **Optimized Approach:** Use DFS or BFS
    
    - Time Complexity: O(m * n)
    - Space Complexity: O(1)
    
    **Solution:** Use DFS to explore and mark visited islands in a grid, accumulating area for each and tracking the maximum area found.
    

## 417 - Pacific Atlantic Water Flow

**Intuition:** Find cells where water can flow to both the Pacific and Atlantic oceans by checking from the edges inward, using DFS or BFS for water flow directions.

- Solutions
    
    **Brute Force:** Traverse every single single cell to see if it can flow as deep as possible to Pacific and Atlantic. Restart the DFS each time without checking if its been visited
    
    - Time Complexity: O(M * N)^2
    - Space Complexity: O(n)
    
    **Optimized Approach:** Traverse from the boundaries of the Pacific and Atlantic ocean then find the intersections between both.
    
    - Time Complexity: O(m * n), instead of restarting the DFS per cell, we check if its already been visited
    - Space Complexity: O(n)
    
    **Solution:** Use DFS from ocean boundaries to find cells where water can flow both to the Pacific and Atlantic, marking reachable areas and identifying intersections.
    
    **NOTE:** Water can flow from all directions. So we need to check starting from the cell we are at to see if it flows from the four directions of up, down, left, and right.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/4edf6cf9-4258-462f-a742-f8610521424e/Untitled.png)
    
    **Unique uses:**
    
    - Using a set to check if a tuple of coordinates has been visited for the grid

## 130 - Surrounded Regions

**Intuition:** Think of isolating regions of 'O's surrounded by 'X's on a board by first marking the 'O's connected to the edges and then flipping the unmarked, enclosed 'O's to 'X's.

- Solutions
    
    **Optimized Approach:** DFS starting from the borders
    
    - Time Complexity: O(m * n)
    - Space Complexity: O(n)
    
    **Solution:** Mark border-connected 'O's as temporary, flip all other 'O's to 'X's, then revert temporary marks back to 'O's to surround regions. Starting from un-surrounded regions also helps mark the ones directionally attached to the un-surrounded region that are not in the border.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/3dd92b30-22ae-4d59-a2a6-13c885d7413f/Untitled.png)
    
    **Unique uses:**
    
    - Adds a temporary value to the cell value then flips it back
        - This is called reverse engineering to help us find the solution instead of focusing on surrounded region we focus on un-surrounded

## 994 - Rotting Oranges

**Intuition:** Envision tracking the spread of rot from initially rotten oranges across a grid, where each time increment allows the rot to extend to adjacent fresh oranges.

- Solutions
    
    **Brute Force:** Using a set to track fresh oranges
    
    - Time Complexity: O(m * n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use a counter to track fresh oranges
    
    - Time Complexity: O(m * n)
    - Space Complexity: O(1)
    
    **Solution:**  Spreads rot from rotten oranges to adjacent fresh ones in a grid using level-order BFS, tracking time until no fresh oranges remain or returning -1 if isolation prevents complete rotting.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/15beb298-379d-48de-9ef3-5cd1340ea38c/Untitled.png)
    
    **Unique uses:**
    
    - Uses BFS level order traversal
        - Does the validation checks right away when adding a new row and new col to the queue
            - Helps prevent counting minutes to a queue that contains fresh oranges
    - Adds multiple starting points to the queue of BFS if there are more than 1 rotten orange

## 286 - Walls and Gates

**Intuition:** 

- Solutions
    
    **Brute Force:** Do a DFS or BFS traversal for every cell to find the nearest gate
    
    - Time Complexity: O(mn)^2
    - Space Complexity: O(n)
    
    **Optimized Approach:** Do a BFS level order traversal for all of the gates all at once
    
    - Time Complexity: O(m *n)
    - Space Complexity: O(n)
    
    **Solution:** 
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/31fdf55a-bee3-4284-ba9a-fa41cef09306/Untitled.png)
    
    **Unique uses:**
    
    - BFS level order traversal

## 207 - Course Schedule

**Intuition:** Think of determining if you can complete all courses without prerequisites forming a loop, essentially checking if the course dependency graph is acyclic.

- Solutions
    
    **Optimized Approach:** Do topographic sort
    
    - Time Complexity: O(V + E)
    - Space Complexity: O(n)
    
    **Solution:** DFS to detect cycles in a course prerequisite graph, marking a course as completable by clearing its prerequisites after exploration, ensuring all courses can be completed if no cycles exist.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/9e10da09-1255-49da-9646-f94a471144b9/Untitled.png)
    
    **Unique uses:**
    
    - Representing a graph as an adjacency list
    - Clearing the edges for a vertex if the course has been completed
    - Using topographic ordering in a directed acyclic graph to help explore the vertices
        - To detect a loop we check if its cyclic

## 210 - Course Schedule 2

**Intuition:** Find a possible order of courses to complete based on prerequisites, akin to organizing tasks with dependencies using a directed graph to ensure all prerequisites are met before taking any course.

- Solutions
    
    **Optimized Approach:** Topological ordering
    
    - Time Complexity: O(V+E)
    - Space Complexity: O(V+E)
        - Prerequisite map stores all edges (prerequisites) for a vertex (course)
    
    **Solution:** Detect cycles and determine a topological order of courses by tracking visited (cycle) and completed nodes, reversing the resulting list to ensure prerequisites come before courses.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/eec66326-eb62-4912-a1eb-9347d26fdbbf/Untitled.png)
    
    **Unique uses:**
    
    - Uses backtracking for topological ordering
        - To check if a course has been completed we add it to a set when we start backtracking to a next prerequisite

## 323 - Number of Connected Components in an Undirected Graph

**Intuition:** Involves counting the number of disconnected subgraphs (connected components) in an undirected graph by examining which nodes are directly or indirectly connected through edges.

- Solutions
    
    **Optimized Approach:** DFS Solution
    
    - Time Complexity: O(V + E)
    - Space Complexity: O(V + E)
    
    **More Optimized Approach:** Union Find
    
    - Time Complexity: *O*((*N*+*E*)*α*(*N*))
        - Worst complexity of Union Find is O(log N) but with path compression and using rank it is *O*(*α*(*N*))
        - We need to perform union operations of all edges which takes *O*(*Eα*(*N*))
        - Then at the end to get the result, we run the find function for all parent nodes which is another *O*(*Nα*(*N*))
    - Space Complexity: O(N)
    
    **Solution:** Uses a Union Find data structure with path compression and rank to efficiently count the number of connected components in a graph by unioning edges and determining the unique root nodes.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a1381a68-d0bd-47f4-b51b-34e59972e99d/Untitled.png)
    
    **Unique uses:**
    
    - Uses UnionFind with path compression and rank to efficiently count the connected components

## 684 - Redundant Connection

**Intuition:** Find an edge that, when removed, eliminates a cycle in an undirected graph, essentially identifying the redundant connection that forms a loop within the graph's structure.

- Solutions
    
    **Brute Force:** Use DFS to traverse undirected graph, if the source equals to target then there’s a cycle 
    
    - Time Complexity: O(V+E), if its an adjacent matrix instead of list it could be O(n^2)
    - Space Complexity: O(V+E)
    
    **Optimized Approach:** 
    
    - Time Complexity: Very close to O(n)
        - Worst complexity of Union Find is O(log N) but with path compression and using rank it is *O*(*α*(*N*)) → which is close to O(n)
    - Space Complexity: O(n)
    
    **Solution:** Union-Find data structure to detect and return the first edge that causes a cycle in an undirected graph, indicating a redundant connection.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/4856108b-b058-4e79-b19f-f4204d9d95d8/Untitled.png)
    
    **Unique uses:**
    
    - Detects a cycle using Union Find data structure by checking if the nodes we want to union have the same parent nodes thus we are connecting the group creating a cycle
    - Traversing an undirected graph using BFS or DFS, different to directed as we need a source and target to traverse to.

## 261 - Graph Valid Tree

**Intuition:** Verify if a given undirected graph is a tree by checking that it's fully connected without any cycles.

- Solutions
    
    **Brute Force:** DFS traversal of undirected graph
    
    - Time Complexity: O(V+E)
    - Space Complexity: O(V+E)
    
    **Optimized Approach:** Union Find
    
    - Time Complexity: Close to O(n)
        - Worst complexity of Union Find is O(log N) but with path compression and using rank it is *O*(*α*(*N*)) → which is close to O(n)
    - Space Complexity: O(n)
    
    **Solution:** Valid tree is when there are no cycles in the graph and there is only 1 group of connections.
    

## 1584 - Min Cost to Connect All Points (Advanced)

**Intuition:** Construct a minimum spanning tree from given points in a 2D space, focusing on minimizing the total edge cost with the constraint that edges represent the Manhattan distance between points.

- Solutions
    
    **Brute Force:** Kruskal’s algorithm with sorting
    
    - How it works:
        1. Calculate the Manhattan distance between every pair of points and create a list of edges with their distances.
        2. Sort all the edges based on their distances in ascending order.
        3. Use a Disjoint Set Union (DSU) or Union-Find data structure to help in detecting cycles.
        4. Iterate through the sorted list of edges, and for each edge, if the two points are not already in the same set (i.e., not connected), connect them and add the distance to the total cost.
        5. Continue this process until all points are connected.
    - Time Complexity: O(N^2 log N) + O(N^2) = O(N^2 log N
        - O(N^2) for calculating distances between all pairs of points, up-front
        - O(N^2 log N) for sorting the edges based on distance
    - Space Complexity: O(n^2) since storing all Manhattan distances at the beginning
    
    **Optimized Approach:** Use Prim’s algorithm with a priority queue (BFS)
    
    - How it works:
        1. Start with an arbitrary point as the current vertex and add all other points with their distances to the current vertex into a min-heap.
        2. Extract the point with the minimum distance from the heap, mark it as visited, and add the distance to the total cost.
        3. Update the heap with distances to this newly visited point for all non-visited points, if the new distances are smaller.
        4. Repeat steps 2 and 3 until all points have been visited.
    - Time Complexity: O(n^2 log N) → similar to Kruskal
    - Space Complexity: O(n) → since we are just storing min heap and visited
        - Prim’s algorithm doesn’t necessarily store all edges at once in memory
    
    **Solution:** Prim's algorithm with a priority queue (min heap) to build a minimum spanning tree by iteratively adding the nearest unvisited point based on Manhattan distance, starting from point 0.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5cb007de-bf4d-4632-bd79-a94cb9a34a84/Untitled.png)
    
    **Unique uses:**
    
    - Uses Prim’s and Kruskal’s algorithm to get the minimum cost of a weighted tree

## 743 - Network Delay Time (Advanced)

**Intuition:** Find the minimum time it takes for a signal to reach all nodes in a network, starting from a given node; think of spreading out from the starting node to cover the entire network, using the shortest path to each node based on the time delays along different paths.

- Solutions
    
    **Brute Force:** Bellman Ford’s algorithm
    
    - Time Complexity: O(V*E) → O(n^2)
    - This is due to Bellman Fords being less efficient for graphs without negative weights
    
    **Optimized Approach:** Use Dijkstra’s algorithm BFS
    
    - Time Complexity: *O*(*E*log*E*)+*O*(*E*)+*O*(*N*)
        - Graph construction: O(E)
        - Time mapping: O(n)
        - Dijkstra’s algorithm: O(E log E), each edge can result in a heap operation
    - Space Complexity: O(N + E)
    
    **Solution:** 
    
    **Unique uses:**
    
    - Uses Dijkstra’s algorithm to find the shortest path to get all nodes receive the network.

## 787 - Cheapest Flights within K Stops (Advanced)

**Intuition:** Find the cheapest flight price from a starting city to a destination city, given a maximum number of stops, by exploring different flight routes and their costs.

- Solutions
    
    **Brute Force:** Using a BFS with a priority queue
    
    - Time Complexity: O(E * K * log (V*K)) → TLE error
    - Space Complexity: O(E)
    
    **Optimized Approach:** Bellman Ford’s algorithm within K stops
    
    - Time Complexity: O(|E| * K)
        - Usually O(|V| * |E|) → O(n^2), but we can optimize to only do it within K stops
    - Space Complexity: O(|E|)
    
    **Optimized Approach:** Dijkstra’s algorithm
    
    - Time Complexity:
    - Space Complexity: O(|E|)
    
    **Solution:** Update flight prices to find the cheapest price from source to destination within k stops by relaxing all edges up to k+1 times, ensuring the minimum cost path is considered even if direct flights are not available.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/3ca1edd1-b177-4992-a976-17731511b9f1/Untitled.png)
    
    **Unique uses:**
    
    - Uses Bellman Ford’s algorithm within K stops instead of all the way up to |V| - 1 times of edge relaxation

# Dynamic Programming

## 70 - Climbing Stairs

**Intuition:** Count the ways to climb to the top of a staircase with n steps, where you can either take 1 or 2 steps at a time; the essence lies in recognizing the problem as a Fibonacci sequence, where the number of ways to reach a step is the sum of the ways to reach the two previous steps.

- Solutions
    
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

- Solutions
    
    **Brute Force:**  Use recursion to calculate all sub problems for taking one step and taking two steps.
    
    - Time Complexity: O(2^n), exponential since some sub problems repeat
    - Space Complexity: O(h)
    
    **Optimized Approach:** Use bottom up DP to find a relationship between sub problems.
    
    See example of how it was solved here: ‣ 
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/31c526eb-11a0-4489-8c4e-107d0b0b7d0a/Untitled.png)
    
    - ****Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Update an array with the cost for each step based on the cheaper cumulative cost of the two previous steps, concluding with the minimum of the last two calculated costs to account for the final step choice.
    
    **Unique uses:**
    
    - **DICTIONARIES DONT NEED TO BE NONLOCALIZED**
        - This is due to the fact that dictionaries are mutable, we are modifying the content rather than reassigning the cache variable itself
    

## 198 - House Robber

**Intuition:** Choosing between robbing a house and not robbing its neighbor, or skipping it, to maximize your total loot without triggering alarms.

- Solutions
    
    **Brute Force:** Explore all possible combinations using recursion
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(h) → height of tree
    
    **Optimized Approach:** Use tabulation
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Calculates the maximum loot by tracking the best choices up to each house, deciding at each step between robbing it (and adding to the loot from the house before last) or moving on with the loot from the last house.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d9e5f18d-31ff-4cdc-a3ec-0dcddcec4ee9/Untitled.png)
    

## 213 - House Robber 2

**Intuition:** Maximize the sum of non-adjacent numbers from a circular list of integers, meaning you have to choose wisely since the first and last elements are considered neighbors.

- Solutions
    
    **Brute Force:** Use tabulation DP but with an array
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use tabulation without an array
    
    - Time Complexity:O(n)
    - Space Complexity: O(1)
    
    **Solution:** Maximizes the robbery amount by separately handling two scenarios: excluding the first and excluding the last house, then taking the maximum of these two.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/30c1cdab-acc2-49ee-bf4f-83f36e205a56/Untitled.png)
    

## 5 - Longest Palindromic Substring

**Intuition:** Find the longest segment within a given string that reads the same backward as forward, exploring every possible center of symmetry.

- Solutions
    
    **Brute Force:** Check each substring for every character and check if its a palindrome
    
    - Time Complexity: O(n^3)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use palindrome expand
    Palindromes are symmetric around their center. The optimal way to identify a palindrome involves moving outward from the center rather than inward from the edges. Starting from the edges works for problems like "valid palindrome" checks but not for finding the longest palindromic substring where the palindrome can start anywhere within the string.
    
    Odd length: “racecar”, Even length: “abba
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Solution:** Finds the longest palindromic substring by checking palindromes centered at each character (for odd lengths) and between each pair of characters (for even lengths), updating the longest palindrome found.
    
    **Unique uses:**
    
    - Palindrome expand to find all palindromes anywhere within a string as opposed to using a traditional two pointer approach using the edges.

## 647 - Palindromic Substrings

- Solutions
    
    **Brute Force:** Check for palindromes per substring
    
    - Time Complexity: O(n^3)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Outward expand to find palindromes
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Solution:** Outward expand to find palindromes
    

## 91 - Decode Ways

**Intuition:** Determine how many distinct ways you can decode a given numeric string into letters, given that the numbers correspond to letters in a way where "1" is "A", "2" is "B", ..., "26" is "Z".

- Solutions
    
    **Brute Force:** Top down solution
    
    - Time Complexity: O(2^n), with caching O(n)
    - Space Complexity: O(h)
    
    **Optimized Approach:** Bottom up tabulation
    
    - Time Complexity: O(n)
    - Space Complexity: O(n), with prev1 and prev2 it is O(1)
    
    **Solution:** Count the number of ways to decode a string, using two variables to cache the last two states and update them iteratively based on current and previous digit validity.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/816cd966-6643-479e-993b-fad4843d095f/Untitled.png)
    
    - How it works:
        
        # **How to Reach the Solution**
        
        ### Subproblems Identified
        
        1. Decoding a Single Digit: Any single digit from '1' to '9' can be decoded into its corresponding letter ('A' to 'I'). The subproblem here is determining if a single digit at position `i` can be decoded and how that affects the total count of decoding ways.
        2. Decoding Two Digits as a Pair: Two consecutive digits that form a number between 10 and 26 inclusive can be decoded into a letter ('J' to 'Z'). The subproblem is to determine if digits at positions `i-1` and `i` can be decoded together as a valid pair, affecting the total decoding ways.
        3. Handling Zeros: Zeros cannot be decoded on their own; they must be part of a valid pair ('10' to '20'). This introduces conditional logic into the subproblems, as the presence of a zero at position `i` necessitates checking the digit at `i-1` for a valid pairing.
        
        ### Recurrence Relation Based on Subproblems
        
        Given these subproblems, the recurrence relation for `dp[i]` (representing the number of ways to decode the substring ending at position `i`) can be defined as follows, considering a 1-indexed array for explanation (adjust for 0-indexing in actual implementation):
        
        - For a Single Digit (not '0'): If the digit at position `i` is not '0', it can form a letter on its own. This means all decoding ways leading up to `i-1` can be extended by this single digit, contributing to `dp[i-1]` ways.
        - For Two Digits forming a valid pair (10-26): If the two digits ending at `i` form a valid number between 10 and 26, then all ways leading up to `i-2` can be extended by this pair, contributing to `dp[i-2]` ways.
        - For Zeros: Special handling where the zero must pair with the preceding digit, affecting the conditions under which `dp[i-2]` is considered.
        
        ### Putting It All Together
        
        The recurrence relation thus integrates these subproblems:
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d83ee54a-718b-45b6-9bc8-92edceb86c0d/Untitled.png)
        
        - Base Cases: `dp[0]` is 1 (an empty string has one way to decode, by doing nothing), and `dp[1]` is set based on whether the first character forms a valid decoding.
        
        # **Indexing**
        
        It sounds like you've pinpointed a crucial aspect of understanding how indexing works in the context of dynamic programming, especially for this type of problem. Let's clarify this to ensure there's no confusion moving forward.
        
        ### **Clarifying `dp[i-1]` and `dp[i-2]` in the Context of "11106"**
        
        When using dynamic programming (DP) to solve problems like "Decode Ways," it's essential to keep track of how indices in your **`dp`** array relate to characters in the string. Specifically, for a string "11106" and when referring to **`dp[i-1]`** and **`dp[i-2]`**, here's what they represent in the context of iterating through the string:
        
        - **At any index `i` in the iteration**:
            - **`dp[i]`** represents the total number of ways to decode the substring that ends at the character corresponding to **`i-1`** in 0-based indexing for the string.
            - **`dp[i-1]`**: Refers to the total decoding ways up to (and including) the character immediately before the current one in the iteration. It represents the cumulative decodings considering the string up to the previous character.
            - **`dp[i-2]`**: Refers to the total decoding ways up to two characters before the current one in the iteration. This is crucial for considering pairs of digits that can be decoded together (like "10" to "26").
        
        ### **Example with "11106"**
        
        When iterating through "11106", at the point where you are considering the full string (i.e., at the end of your iteration):
        
        - **Index `i` = 5 (for the full string "11106") in `dp`**:
            - **`dp[i-1]` (or `dp[4]`)** corresponds to decoding ways up to and including "1110". It does not mean the digit '0' alone but represents the cumulative ways the substring "1110" can be decoded.
            - **`dp[i-2]` (or `dp[3]`)** then represents decoding ways up to "111". It's about the cumulative ways up to that point, not just the digit '1'.
        
        # **What is [i-2] and [i-1]?**
        
        ### **Single Digit Decoding (`dp[i-1]`)**
        
        - **Decoding a Single Digit**: Each digit from '1' to '9' can be independently decoded into a letter ('A' to 'I'). This means that if the current character at position **`i-1`** (since the string is 0-indexed and **`dp`** is 1-indexed) is not '0', it represents a valid single-digit encoding.
        - **Why Add `dp[i-1]`**: The presence of a valid single digit at position **`i-1`** allows for all the decoding ways counted up to **`i-1`** to be extended by one more letter. Essentially, **`dp[i-1]`** captures all the ways the substring ending just before the current digit can be decoded. Adding this value to **`dp[i]`** signifies that each of those ways can include the current digit as a new, valid letter in the sequence.
        
        ### **Double Digit Decoding (`dp[i-2]`)**
        
        - **Decoding Two Digits Together**: If the two digits at positions **`i-2`** and **`i-1`** (reflecting the current segment being considered) form a number between 10 and 26, they can be decoded together into a single letter. This is based on the rule that numbers like '10' to '26' correspond to letters 'J' to 'Z'.
        - **Why Add `dp[i-2]`**: When two digits form a valid double-digit encoding, it introduces an additional way to decode the string up to position **`i`**. The **`dp[i-2]`** count represents all the ways to decode the substring up to (and not including) these two digits. By adding **`dp[i-2]`** to **`dp[i]`**, you're acknowledging that each of these prior decoding ways can be extended by decoding the two current digits as one letter. This does not disrupt the previously counted **`dp[i-1]`** ways since it represents an alternative decoding path that incorporates the two digits as a pair rather than individually.
        
        ### **Summary**
        
        - **Adding `dp[i-1]`**: Reflects extending previous decodings with the current single digit, indicating continuity in the decoding process where each valid single digit augments the existing decoding paths.
        - **Adding `dp[i-2]`**: Accounts for the additional decoding possibility introduced by a valid two-digit pair, offering an alternate path that can complement the single-digit decoding paths.

## 322 - Coin Change

**Intuition:** Try to find the minimum number of coins needed to make up a specific amount of money, using coins of given denominations with an unlimited supply.

- Solutions
    
    **Brute Force:** Bottom up memoized solution
    
    - Time Complexity: O(2^S*n), with cache O(S*n) → where S is amount and n is coins
    - Space Complexity: O(S)
    
    **Optimized Approach:** Top down tabulation
    
    - Time Complexity: O(S)
    - Space Complexity: O(S)
    
    **Solution:** Fill a table with the minimum number of coins needed for each amount up to the target, updating each entry based on the smallest number of coins needed to reach that amount with the given denominations. **Greedy is not possible.**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/6160f84e-cf7e-4cd3-9dae-8ee1176c1241/Untitled.png)
    

## 152 - Maximum Product Subarray

**Intuition:** Find the largest product possible from a contiguous subarray within an integer array, considering that multiplying negative numbers can turn a small product into a large one.

Read code solution comments if you are confused.

- Solutions
    
    Maybe mention that sliding window algorithm won’t work as its better for sums
    
    **Brute Force:** Use a nested for loop and check for every possible sub array
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Use DP
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Track both maximum and minimum products up to each position in an array, swapping them when encountering a negative number, to maximize the product of a contiguous subarray.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d41da346-e862-4838-bc40-ac95e77dc4b2/Untitled.png)
    

## 139 - Word Break

**Intuition:** Determine if a given string can be segmented into one or more dictionary words, ensuring each segment is a valid word from the provided list.

- Solutions
    
    **Brute Force:** Use DFS to backtrack and find other segments
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use DP tabulation
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Solution:** Keep track of where a word has been successfully segmented so for each partitioned substring we know that the start point was previously segmented therefore we can mark the end point as another segment preventing to having to backtrack.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c7b79338-6c32-425f-9d30-70b5f146923d/Untitled.png)
    

## 300 - Longest Increasing Subsequence

**Intuition:** Find the length of the longest subsequence of a given array where the elements of the subsequence are strictly increasing. This subsequence does not need to be contiguous, but it should maintain the order of appearance in the array.
**Read code if confused.**

- Solutions
    
    **Brute Force:** DFS approach, create a subsequence per index and decide whether to keep current index or not (2 choices)
    
    - Time Complexity: O(2^n) → can lower with memoization
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use tabulation
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Solution: C**alculate the longest increasing subsequence of a list, where each element in a DP array **`dp`** is updated based on the maximum length of subsequences ending at each position, ensuring only values from previous smaller elements contribute to the current position’s length calculation.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f1e1eb32-31f3-4a66-9e0d-1fc23a316235/Untitled.png)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5ccae31e-45c4-4ab1-a19f-6ac02430a34e/Untitled.png)
    
    **Subproblem:** Which previous numbers are smaller than the current number we are on? 
    **LIS[i] = max(LIS[..], LIS[..], …) + 1**
    
    **Unique ways:**
    
    - Problem 139 and 300 are similar in how it partitions the array and iterates through partition

## 416 - Partition Equal Subset Sum

**Intuition:** This problem essentially asks whether you can find a subset of numbers that sums to half of the total sum of the array.

- Solutions
    
    **Brute Force:** DFS, 2 choices, include or exclude to subset
    
    - Time Complexity: O(2^n) → can be optimized with memoization
    - Space Complexity: O(n)
    
    **Optimized Approach:** Top down tabulation
    
    - Time Complexity: O(n * sum(nums))
    - Space Complexity: O(n)
    
    **Solution:**  Updates a DP array from right to left for each element to ensure each number contributes only once to each possible subset sum.
    
    Top down solution:
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d8c47103-61e1-488f-8090-11fa2b21581d/Untitled.png)
    
    Bottom up solution:
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/00d6bc22-ea7d-4dde-a997-e5e418a692f7/Untitled.png)
    
    - States
        
        ### **Explanation of the States `True` and `False`**
        
        **1. `False` State:**
        
        - **Meaning**: When **`dp[j]`** is **`False`**, it means that, based on the elements considered so far, there is no subset of those elements that sums to **`j`**.
        - **Usage**: This is the default state, implying that a sum has not been achieved. As the algorithm processes each element of the input array, it attempts to switch this state to **`True`** for various sums if they can be made with available numbers.
        
        **2. `True` State:**
        
        - **Meaning**: When **`dp[j]`** is **`True`**, it signifies that there is at least one subset of the numbers processed up to that point which sums to **`j`**.
        - **Usage**: Once a **`dp[j]`** reaches a **`True`** state, it remains **`True`** for the remainder of the process because once a sum **`j`** can be achieved, adding more numbers to the pool (without subtracting) cannot make this sum impossible.

# 2D Dynamic Programming

## 62 - Unique Paths

**Intuition:** This problem essentially asks you to calculate all possible paths through a grid given fixed movement constraints.

- Solutions
    
    **Brute Force:** Use a DFS to explore all paths, ends up re-visiting paths
    
    - Time Complexity: O(2^n) → memoized would be O(m x n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use tabulation 
    
    - Time Complexity: O(m*n)
    - Space Complexity: O(n)
    
    **Solution:** Updated states in a single loop to sum paths from the left and above (bottom + right), simulating a bottom-up approach by effectively rotating and compressing a 2D grid into a 1D array that accumulates paths to the bottom-right corner.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/236a4398-2f1d-4727-bd8a-d6c44e060180/Untitled.png)
    
    **Unique uses:**
    
    - Uses a 1D array in tabulation and just iterate over it in a nested loop doing calculations like its a 2d array
    - Think of the bottom up approach as just flipping the 2d table upside down and inverting it.
        - Adding the current column we are on + the previous column will be similar to a right + down operation in recursive solution

## 1143 - Longest Common Subsequence

**Intuition:** Find the length of the longest subsequence common to two strings, which means identifying the longest sequence of characters that can appear in the same order within both strings without needing to be consecutive.

- Solutions
    
    **Brute Force:** Use a DFS to explore all choices
    
    - Time Complexity: O(2^m+n) → memoized is O(m * n)
    - Space Complexity: O(m*n)
    
    **Optimized Approach:** Use a bottom up tabulation approach
    
    - Time Complexity: O(m * n)
    - Space Complexity: O(m*n)
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8448e486-4cca-48fd-b2e5-cebc2f99e2e9/Untitled.png)
        
    
    **Solution:** Find the longest common subsequence between two strings by building a 2D matrix bottom-up, where each cell represents the LCS length using the choice of extending the sequence on matches or skipping a character on mismatches.
    **Bottom up chart:**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/158ffd37-122b-49fa-8e67-8b7e287199d1/Untitled.png)
    

## 309 - Buy and Sell Stock with Cooldown

**Intuition:** Maximize profit from stock trades with the constraint that after selling a stock, you cannot buy another on the next day (a cooldown period). The challenge is to decide on each day whether to buy, sell, or rest to achieve the maximum possible profit over the given list of prices.

- Solutions
    
    **Brute Force:** Use DFS to explore all scenarios of holding, buying and selling stock
    
    - Time Complexity: O(2^n) → memoization O(n)
    - Space Complexity: O(1) → memoization O(n)
    
    **Optimized Approach:** Use tabulation
    
    - Time Complexity: O(n)
    - Space Complexity: O(2 * n) → can be improved to O(1)
    
    **Solution:** Maintaining a 2D DP array, where **`dp[i][0]`** and **`dp[i][1]`** track the maximum profits without and with stock respectively, updating these states based on previous day's profits and current price actions.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/edb08cfa-6f6d-474b-a959-1efdda3960f2/Untitled.png)
    
    **Tabulation 2D Data:**
    
    ```python
       Day    dp[i][0]    dp[i][1]
        0        0          -1
        1        1          -1
        2        3          -1
        3        3           1
        4        3           1
        
    dp[i][0] represents the maximum profit achievable by the end of 
    day i without holding any stock. This accounts for either selling stock 
    or resting if it was better not to have sold the stock the previous day.
    
    dp[i][1] shows the maximum profit achievable by the end of day i while 
    holding a stock, considering whether to buy on that day or continue holding 
    from a previous purchase.
    ```
    

## 518 - Coin Change 2

**Intuition:** Figure out all possible combinations of the coins that sum up to the target amount.

- Solutions
    
    **Brute Force:** Use DFS to explore all possibilities of skipping and using the coin
    
    - Time Complexity: O(2^n) → memoized is O(m*n)
    - Space Complexity: O(m*n)
    
    **Optimized Approach:** Use tabulation
    
    - Time Complexity: O(m*n)
    - Space Complexity: O(n) where n is amount + 1
    
    **Solution:** Calculate the number of ways to make a specific amount with a list of coins, where each cell **`dp[i][j]`** accumulates the ways to make amount **`j`** using the first **`i`** coins, summing the possibilities without the current coin and adding those from using the current coin multiple times.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/9fa5c50a-f154-4942-8816-77bb671cc0f3/Untitled.png)
    
    **Bottom Up Matrix:**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/ab444488-9f19-4d53-9dc9-2f808d99baa8/Untitled.png)
    

## 494 - Target Sum

**Intuition:** Find how many ways you can add or subtract the given numbers in an array to achieve a specific target sum.

- Solutions
    
    **Brute Force:** Use DFS to explore all choices for subtract and add
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(h)
    
    **Optimized Approach:** Memoization
    
    - Time Complexity: O(n* total(nums)) → total(nums) since we may call the function total of the nums array times. E.g. [1, 1] → -2 to 2
    - Space Complexity: O(* total(nums))
    
    **Solution:** Count the number of ways to sum subsets of **`nums`** to reach **`target`** by exploring and caching both adding and subtracting each number from the total.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/34db8a44-84b1-4eae-9f1c-b5b9bf2de997/Untitled.png)
    

## 97 - Interleaving String

**Intuition:** Determine if you can interleave two strings **`s1`** and **`s2`** to form a third string **`s3`**, using all characters from **`s1`** and **`s2`** in a way that maintains their relative order within the original strings **`s1`** and **`s2`**.

- Solutions
    
    **Brute Force:** Use DFS to explore all combinations of slicing s1 and s2
    
    - Time Complexity: O(2^n) → memoization is O(s1 * s2)
    - Space Complexity: O(s1 * s2)
    
    **Optimized Approach:** Use tabulation
    
    - Time Complexity: O(s1 * s2)
    - Space Complexity: O(s1 * s2)
    
    **Solution:** Verify if **`s3`** can be formed by interleaving **`s1`** and **`s2`**, caching results to avoid redundant calculations while exploring choices to use characters from either **`s1`** or **`s2`** if they match the current character in **`s3`**.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c1394c29-baeb-4419-a14b-c217f3769d5a/Untitled.png)
    

## 72 - Edit Distance

**Intuition:** Determine the minimum number of operations (insertions, deletions, or substitutions) required to convert one string (**`word1`**) into another (**`word2`**), exploring the concept of edit distance.

- Solutions
    
    **Brute Force:** Explore all ways to insert, delete, replace
    
    - Time Complexity: O(2^n) → memoized is O(m*n)
    - Space Complexity: O(m*n)
    
    **Optimized Approach:** Use tabulation ****
    
    - Time Complexity: O(m*n)
    - Space Complexity: O(m*n)
    
    **Solution: C**ompute the minimum edit distance between two strings, **`word1`** and **`word2`**, by constructing a DP table that iteratively fills in the minimal costs for transforming substrings of **`word1`** into substrings of **`word2`** based on insertion, deletion, and substitution operations.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/6b4b4763-3c61-4ba9-a415-98a32c3d966d/Untitled.png)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/87af42ca-d1d0-4b84-8661-061bf926e18f/Untitled.png)
    

# Greedy

## 53 - Maximum Subarray

**Intuition:** Find the contiguous subarray within an array of integers that has the highest sum, focusing on efficiently determining the range that maximizes this cumulative value.

- Solutions
    
    **Brute Force:** Nested for loop to check for all subarrays and save the sum for each subarray
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Greedy approach
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Use a greedy approach, choose the local optimum choice of restarting the subarray if our current sum becomes negative.
    

## 55 - Jump Game

**Intuition:** Determine if it's possible to reach the last index of an array from the first index, where each array element indicates the maximum jump length from that position. You don’t always have to use the maximum jump length.

- Solutions
    
    **Brute Force:** DFS to explore all jumps for each jump length
    
    - Time Complexity: O(n^n) → memoized is O(n) due to doing the furthest jump first, without that it is O(n^2)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/bf2bea60-518d-433b-b779-fdbe3eb256d1/Untitled.png)
    
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use tabulation
    
    - Time Complexity: O(n^2) → can be optimized to O(n)
    - Space Complexity: O(n) → can be optimized to O(1)
    
    **Greedy Approach:** Use most local optimal choice
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Update the furthest point you can reach at each iteration (greedy), at any point if the max reachable is greater than or equal to length of the array, it means we can reach it.
    

## 45 - Jump Game 2

**Intuition:** Find the minimum number of jumps required to reach the last index of an array from the first index, with each array element indicating the maximum jump length from that position. The challenge is to optimize the path to minimize the number of jumps needed.

- Solutions
    
    **Brute Force:** DP solution
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Greedy approach
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Greedily choose the farthest jump length per iteration and update a pointer to the end. 
    
    **Unique uses:**
    
    - Similar to two pointer approach

## 134 - Gas Station

**Intuition:** Determine the starting gas station index from which you can complete a circuit around a circular route, where each station provides a certain amount of fuel and requires a certain cost in fuel to reach the next station; the challenge is to ensure you never run out of gas at any point during the journey.

- Solutions
    
    **Brute Force:** Nested for loop using modulo for circular route
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Greedy approach
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Greedy choice to reset starting point if our current tank from previous station we started from becomes negative. 
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/392bd24a-19ae-4ac5-a4e1-08fbbf0b53bd/Untitled.png)
    
    **Unique uses:**
    
    - Starting index + current position % length of array will give circular index in brute force approach.

## 846 - Hand of Straights

**Intuition:** Determine if an array of card values can be grouped into consecutive subsequences of a specific length, ensuring each subsequence is strictly sequential with no skipped numbers.

- Solutions
    
    **Optimized Approach:** Greedy choice
    
    - Time Complexity: O(K log k + k * size)
    - Space Complexity: O(k)
    
    **Solution:** Select the smallest card first then check how many groups that card needs to start in. The subsequent cards needs to also begin in the same amount of groups.
    
    **Unique uses:**
    
    - Sorting as the greedy local optimal choice to select the smallest cards first.

## 1899 - Merge Triplets to Form Target Triplet

**Intuition:** Determine if you can select some of these triplets and use them to form a target triplet. The selection process allows using the maximum values from any of the selected triplets' positions to match exactly the respective positions in the target triplet.

- Solutions
    
    **Optimized Approach:** Greedy approach
    
    - Time Complexity: O(n)
    - Space Complexity: O(3) → O(1)
    
    **Solution:** Locally optimal choice is to prevent choosing triplets that have greater values than target values then greedily choose the highest values across all triplets to match to target.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/0609a9ce-5638-48dd-a883-1aab172387e4/Untitled.png)
    

## 763 - Partition Labels

**Intuition:** Divide a string into as many parts as possible so that each letter appears in only one part, and then return a list of the lengths of these parts.

- Solutions
    
    **Optimized Approach:** Greedy approach
    
    - Time Complexity: O(n)
    - Space Complexity: O(26), 26 letters constraint in hash map
    
    **Solution:** Greedily choose the character that has the farthest last found index so that no characters appear in more than one partition. Global optimum is reached when we reach the end of the last found index.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/6493a78c-96fb-4665-b310-c77b3f610b70/Untitled.png)
    
    **Unique uses:**
    
    - Use enumerate to get index and value of array to populate hash map

## 678 - Valid Parenthesis String

**Intuition:** Determine if a given string composed of characters '(', ')', and '*' is valid. The '*' can be treated as a '(', a ')', or be ignored, and the goal is to check if it's possible to arrange the characters so that the parentheses are correctly balanced.

- Solutions
    
    **Brute Force:** Use memoization
    
    - Time Complexity: O(3^n) → O(n^2)
    - Space Complexity: O(h) → O(n^2)
    
    **Optimized Approach:** Use bottom up tabulation
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n^2)
    - How tabulation works here:
        
        ### **Example String:**
        
        - String: **`"(*))"`**
        - Length: 4
        
        ### **DP Table Visualization:**
        
        | Index/Unmatched j | 0 | 1 | 2 | 3 |
        | --- | --- | --- | --- | --- |
        | 0 (Start) | T | F | F | F |
        | 1 ('(') | F | T | F | F |
        | 2 ('*') | T | T | T | F |
        | 3 (')') | F | T | T | F |
        | 4 (')') | T | F | F | F |
        
        ### **Explanation of Each Row:**
        
        - **Row 0**: Before any characters are processed. Only **`dp[0][0]`** is true, indicating zero unmatched parentheses are possible with zero characters processed.
        - **Row 1** (**`'('`**):
            - **`dp[1][1]`** becomes true because processing **`(`** increases the unmatched count by 1 (from **`dp[0][0]`**).
        - **Row 2** (**`'*'`**):
            - **`dp[2][0]`**: True because **``** can act as an empty character, carrying over **`dp[1][0]`** (not applicable here).
            - **`dp[2][1]`**: True because **``** can act as **`(`**, increasing the unmatched count from **`dp[1][0]`**.
            - **`dp[2][2]`**: True because **``** can also act as **`(`**, increasing the unmatched count from **`dp[1][1]`**.
        - **Row 3** (**`')'`**):
            - **`dp[3][0]`**: Remains false because you cannot have zero unmatched parentheses after an odd number of symbols unless compensated by a **``**.
            - **`dp[3][1]`**: True because **`)`** decreases the unmatched count by 1 from **`dp[2][2]`**.
            - **`dp[3][2]`**: True as **`)`** decreases the unmatched count by 1 from **`dp[2][3]`** (if it were applicable).
        - **Row 4** (**`')'`**):
            - **`dp[4][0]`**: True because **`)`** can reduce the unmatched count from **`dp[3][1]`** to zero, balancing all open parentheses.
        
        ### **How to Read the Table:**
        
        - Each **column** represents a possible number of unmatched opening parentheses (**`j`**) after processing the first **`i`** characters.
        - Each **row** corresponds to processing another character in the string, updating possible states based on the character's nature (**`(`** increases, **`)`** decreases, **``** has multiple effects).
    
    **Best Optimized Approach:** Use greedy solution
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Greedy approach to dynamically track the range of possible unmatched opening parentheses (**`low`** to **`high`**) while processing characters in string **`s`**, adjusting **`low`** and **`high`** for **`(`**, **`)`**, and **`*`**, resetting **`low`** to zero if it goes negative, and returning **`False`** if **`high`** becomes negative, 
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/fa5312fe-15b9-4f8a-b13f-783bf233ee0f/Untitled.png)
    

# Intervals

## 252 - Meeting Rooms

**Intuition:** Determine if a person can attend all meetings based on given time intervals for each meeting, by checking if any meeting times overlap.

- Solutions
    
    **Brute Force:**  Compare every interval with each other to see if there are overlaps
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Sort the intervals by start time in ASC order then iterate
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/922fd683-0956-44c4-b54c-ec5702953c85/Untitled.png)
    
    - ****Time Complexity: O(nlogn)
    - Space Complexity: O(n)
    
    **Solution:** Overlap = currStartTime< prevEndTime, since the 2nd class starts before the previous class ended.
    
    **Unique uses:**
    
    - Using lambda to sort
        - Using lambda is an anonymous function similar to arrow functions in Javascript
    - Sort the intervals by start time allows us to not compare with every other interval because the next start times will be greater than the previous start times.
        - This means if the previous start time did not overlap, then that means the next start times could never overlap as well.

## 57 - Insert Interval

**Intuition:** Given a list of non-overlapping intervals sorted by their start times, and your task is to insert a new interval into this list so that the intervals remain sorted and without overlaps, possibly merging the new interval with existing ones if necessary.

- Solutions
    
    **Optimized Approach:** 
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** First add intervals in the beginning with no overlap, then check for overlaps, finally add the rest of intervals.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d1421ea8-c742-4c52-87c0-b4f88e2676e6/Untitled.png)
    
    **Unique uses:**
    
    - Multiple while loops to add intervals
    - Using min and max to find the new values for the overlapped interval

## 56 - Merge Intervals

**Intuition:** Merge the overlapping intervals into one interval.

- Solutions
    
    **Optimized Approach:** Sort the start time to easily find overlaps since we only compare the current interval with last interval
    
    - Time Complexity: O(nlogn) + O(n)
    - Space Complexity: O(n)
    
    **Solution:** Sort the intervals, compare current and last, merge overlaps by end time. Start time is not needed to change since its already sorted by start time.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5c6485e5-602c-4103-887c-321f7f77bb05/Untitled.png)
    
    **Unique uses:**
    
    - Using lambda is an anonymous function similar to arrow functions in Javascript

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