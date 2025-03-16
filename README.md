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

**Intuition:** Check if array contains a duplicate

- Solutions
    
    **Brute Force:** Nested for loop
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Hashmap or set
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Iterate through the list and check if it already exists inside the hashmap/set
    

## 242 - Valid Anagrams

**Intuition:** Check for valid anagram (word that uses all original letters from another word)

- Solutions
    
    **Brute Force:** Nested for loop
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Somewhat Optimized:** Sort the letters then check if it equals
    
    - Time Complexity: O(nlogn)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use hashmaps
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **More Approaches:**
    
    - Have 1 hashmap that counts string s then decrement it in string t, check if the count is all 0 at the end
    - Initialize an array with 26 index then use `ord` for each char and subtract it by `‘a’` to get the 0-indexed value and increment it. Decrement the array for string t. Check at the end with `all()` to check if all values in the array are 0.
    
    **Solution:** Count letters in both strings using a hashmap then compare the two hashmaps for both key and value pairs
    
    **Unique uses:**
    
    - Comparing two hashmaps and check if it is equal is allowed in python

## 1 - Two Sum

**Intuition:** Find two numbers that add up to the target.

- Solutions
    
    **Brute Force:** Nested for loop
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Somewhat Optimized:** Sort then use two pointer approach
    
    - Time Complexity: O(nlogn) + O(n) → O(nlogn)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Use a hashmap, stored the nums as key and its index as value
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Uses a hashmap to store and look up the complement of each number (target - current number) to find the indices of the two numbers that add up to the target.
    

## 49 - Group Anagrams

**Intuition:** Group each anagram in a 2D array.

- Solutions
    
    **Brute Force:** Nested for loop that sorts current string then compares against all other strings
    
    - Time Complexity: O(nlogn * n^2)
    - Space Complexity: O(n)
    
    **More Optimized Approach:** Sort the current string, add the the sorted string as a key and the original string as the value. Check if the sorted string key exists per iteration.
    
    - Time Complexity: O(n * mlogm) → n is number of strings, m is letters in each string
    - Space Complexity: O(n)
    
    **Optimized Approach:** Each iteration create an array of 26 space, use the ascii code as the index of the array. Place the array as the key of the hashmap and add the original strings as the value. (USE A TUPLE AS THE KEY, DO NOT JOIN STRINGS AS ITS O(N))
    
    - Time Complexity: O(n * m) → n is each string, m is letters per string
    - Space Complexity: O(n)
    
    **Solution:** Create an array of 26 length to represent the alphabet and use the ascii code of letter a to get the index position of the character you are on. Convert the array to tuple as a key to a hashmap.
    
    **Unique uses:**
    
    - Uses defaultdict
        - Helps optimize checking for existing keys
        - It’ll automatically create a new key for you without check if it exists
    - Uses tuples as a key in a hashmap
        - Tuples are hashable because they are immutable
        - Lists are not hashable because they mutable
    - Uses sorted: sorted_string_case_insensitive = ''.join(sorted(my_string, key=str.lower))
        - Sorts characters in a string lexicographically
    - Uses ascii codes as an index in an array to represent alphabets

## 347 - Top K Frequent Elements

**Intuition:** Get the top K elements that are shown the most

- Solutions
    
    **Brute Force:** Sort a map’s frequency values
    
    - Time Complexity: O(nlogn)
    - Space Complexity: O(n)
    
    **Kinda Brute Force Not Really:** Heapify the values from a map and create a max heap pop and use a tuple as the values for the heap
    
    - Time Complexity: O(k * logn), mostly better than brute force IF k < n
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use bucket sort
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Use an array to bucket sort (index→count, value→[elements]), the length of the array will be the length of elements we need to count since the element can only show up length amount of times.
    
    **Unique uses:**
    
    - 1st approach:
        - Use a max heap to heapify the first value of tuple or array
    - 2nd approach
        - A bucket sort is when you use the index of an array as the key and the value is the element of the index
            - In this case, you can use the key (index) as the frequency count then place an array in the index filled with elements that has the count
            
            ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/86e71971-75fe-4af2-b74a-4e46a3b5a639/Untitled.png)
            

## 238 - Product of Array Except Self

**Intuition:** Calculating a new array where each element at index **`i`** is the product of all the numbers in the original array except the one at **`i`**. This should be done without using division.

- Solutions
    
    **Brute Force:** Nested for loop, multiply each number except for itself
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Wrong Optimized Approach:** Calculate the product of all elements then divide by the element we are on. 
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Actual Optimized Approach:** We make two lists: one has the product of all numbers before each element, and the other has the product of all numbers after each element. Multiply the prefix and postfix for any element we are on.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/69a6aabc-6ae9-4ad4-bdfb-cd45e159a16b/Untitled.png)
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Actual More Optimized Approach:** No need for prefix and product arrays, just calculate it within output array itself.
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** The main idea is that calculating the prefix and postfix allows us to get the product of all elements except for the current index we are on (e.g. we are on index 2, prefix will give all products before index 2 and postfix will give all products after index 2, multiplying prefix index 1 and postfix index 3, gives us the products except for the current element)
    
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

## 36 - Valid Sudoku

**Intuition:** Determine if a given 9x9 Sudoku board is valid, focusing on checking if each row, each column, and each of the 3x3 sub-boxes contain no repeated numbers from 1 to 9, excluding empty spaces denoted as '.'.

- Solutions
    
    **Optimized Approach:** Use a set to check if a value already exists
    
    - Time Complexity: O(9^2)
    - Space Complexity: O(1)
    
    **Solution:** Check duplicates for each rule by: Add values to a row using index of row were on as key, add values to a column using index of column were on as key, use integer division for each row and column to identify the 3x3 square (key = (r//3, c//3) we are on.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/05ecacab-086e-4894-bab3-002331ac6c93/Untitled.png)
    
    **Unique uses:**
    
    - Uses integer division to round down to nearest whole number,  effectively grouping 1-9 numbers in one of the 3x3 squares.
        - Observe that each group of three consecutive rows and each group of three consecutive columns form one of the nine smaller 3x3 squares.
        - Recognize that rows 0-2 form the first band of 3x3 squares, rows 3-5 the second, and rows 6-8 the third. The same applies for columns.
            - **Rows and Columns**: Dividing the row or column index by 3 categorizes the indices into three groups (0 for indices 0-2, 1 for 3-5, 2 for 6-8).
            - **Identifying Subgrids**: Combining these results from rows and columns helps pinpoint which of the nine subgrids the cell falls into, simplifying navigation within the 9x9 grid by treating it as a grid of smaller 3x3 blocks.

## 271 - Encode and Decode Strings

**Intuition:** Design methods to convert a list of strings into a single string that can later be decoded back into the original list, ensuring the encoding is robust enough to handle any characters within the strings.

- Solutions
    
    **Harder Approach:** Use a string delimiter such as “#” and if you see one in the original string just escape it.
    
    **Issue:** Escape character may appear in original string, so we also have to escape the escape character
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Easier Approach:** Use the length of a string plus a string delimiter, in the case that within the string there is another length of string plus delimiter, it does NOT matter since **when we encode, the encoding scheme is always FIRST**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/57c9ef07-e57b-4299-8fa8-af5ba9ad8553/Untitled.png)
    
    - Time Complexity: O(n)
        - Integer conversion from a string is generally O(m) where m is the number of digits, and since the lengths of strings being encoded/decoded are likely small relative to the total length of the input, their impact is minimal on the overall time complexity.
    - Space Complexity: O(n)
    
    **Solution:** “len(str)#” delimiter allows us to know the length of the string to slice the string that needs to be decoded.
    
    **Unique uses:**
    
    - Better than escaping characters “\#” which is more complex as we have to figure out a solution to escape escape characters
        - **You can see in the example above, we have to figure out how to escape the “#” encoding. Or else it will not decode the character.**
    - Uses string.find(’#’, i) to get the index of a character in a string
    - Uses string splicing

## 128 - Longest Consecutive Sequence

**Intuition:** Find the longest sequence of an unsorted integer array.

- Solutions
    
    **Brute Force:** Sort the array then for each number increment 1 and see check if each value is greater.
    
    - Time Complexity: O(nlogn)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Use a hash set to check sequences ****
    
    - Time Complexity: O(n)
    - Space Complexity: O(2n) → O(n)
        - If a number is part of a sequence, it’ll be visited at most twice
        - But if its a sequence itself, then visited once
    
    **Most Optimized Approach:** Loops through the set instead of the list to prevent iterating through duplicates (e.g. [1, 2, 2, 3] → [1, 2, 3] only looks at 2 once)
    
    - Time Complexity: Amortized O(n)
    
    **Solution:** Using a hash set helps find left neighbors, if there aren’t it is the start of a sequence then we can loop to begin the consecutive sequence.
    
    In the picture below, we first check if its the start of a sequence by checking for a left neighbor.
    
    Then we begin incrementing by 1 to see if there are further consecutive sequences which is found at iteration 4.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/577030d0-e93b-4132-b03e-b4f6eb467503/Untitled.png)
    
    **Unique uses:**
    
    - Uses a hash set

# Pointers

## 125 - Valid Palindrome

**Intuition:** A palindrome is a word or phrase that reads the same forwards and backwards. E.g. Racecar. For this question, we need to convert the phrase to or word from uppercase to lowercase and remove all non-alphanumeric characters.

- Solutions
    
    **Brute Force:** Nested for loop
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Use a two pointer approach or use the reverse string in python
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** 
    
    **Unique uses:**
    
    - Converts the string to lowercase using `.tolower()` .
    - Uses `isalnum()` to check if a character is an alphanumeric character.
    - Also uses regex to remove alphanumeric characters.

## 167 - Two Sum II, Input Array is Sorted

**Intuition:** Find the 1-indexed index of two numbers that add up to the target.

- Solutions
    
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

**Intuition:** Determine the maximum amount of water that can be contained between two lines on a chart, where the width between the lines is fixed and the height is determined by the shorter of the two lines you choose.

- Solutions
    
    **Brute Force:** Use a nested for loop, check each combination of heights
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach: Use two pointer approach**
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Use a left and right pointer and find the area using min height to prevent water overflow. Move pointers based on which pointer has current smaller height
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8adfa2cb-f5ca-43f5-a72d-83c09e5a3027/Untitled.png)
    
    **Unique uses:**
    
    - Left and right pointer
    

## 15 - 3Sum

**Intuition:** Finding all unique triplets in an array that sum up to zero, emphasizing the need to handle duplicates and ensuring no triplet is repeated in the output.

1. You need to find triplets that sum to 0
2. You must use different indices (positions) for each number
3. You can use the same value if it appears at different indices
    1. But the three values have to be unique (e.g. [-2, 1, 1] is wrong because 1 is shown twice)
- Solutions
    
    **Brute Force:**  3 nested loops
    
    - Time Complexity: O(n^3)
    - Space Complexity: O(1)
    
    **Optimized Approach:** 2 nested loops, 1 loop to iterate 1st index, another loop to iterate 2nd and 3rd index using two pointers
    
    - Time Complexity: O(nlogn) + O(n^2) = O(n^2)
    - Space Complexity: O(1)
    
    **Solution:** Sort the numbers to easily find duplicates together, then use a loop for 1st index and a 2nd loop that has a two pointer approach to help reach target 0.
    
    1. Sort the array first (to group duplicates together)
    2. Skip duplicates for the first number (i)
        1. If we don’t skip the first number you’ll end up with the same result sets twice. 
        2. E.g. For array: [-1, -1, -1, 2] → [-1, -1, 2], [-1, -1, 2]
    3. Skip duplicates for the second number (l) after finding a valid triplet
    
    **Unique uses:**
    
    - Two pointer approach to find if the target equals to 0
        - Uses a while loop to move the other pointers
    - Sorting the array to easily find duplicates as neighbors.
        - Only need to find duplicates based on 1st and 2nd index
        - 3rd index is taken care of because at this point the left pointer has moved enough which means moving the right pointer to the same value will make the total too large. So if a duplicate is hit for the 3rd index, it wont matter as the total will still be too large.

## 42 - Trapping Rain Water

**Intuition:** Calculate how much water can be trapped after raining on a series of bars of different heights, where the amount of trapped water at each bar depends on the heights of the tallest bars to its left and right.

Think of the image below as an elevated land, so it would be hard to trap rain water on the ends such as index 0 that has a height of 0 since it just spills over to the left edge.

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/22a247d7-c219-42f7-ba7a-d8febf1a0b3c/image.png)

- Solutions
    
    **Optimized Approach:** One loop to check all left max for current position, another loop for right max, and another loop to check units between all left max and right max.
    
    **The important thing here is that we grab the tallest bars to the left or right of the CURRENT index we are on.**
    
    This allows us to check if the current index we are on could be filled with rain water trapped between the heights to left and right.
    
    - Time Complexity: O(3n) → O(n)
    - Space Complexity: O(n)
    
    **More Optimized Approach:** Two pointer approach ****
    
    **Similar to previous approach, move the pointer that has the smaller max height between left or right. Allows us to use the left pointer as the current height and calculate it against the smaller max height.** 
    
    Don’t forget to check for max of current height and the smaller max height to use with calculation of current height to get the units of water to prevent NEGATIVE units. 
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Moving the pointer with the lower boundary (either left or right maximum height) towards the other, updating the maximum heights as it progresses, and accumulating the trapped water at each step when the current height is less than the maximum height seen from that side.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/4522f2b4-15a6-4c28-b61d-9b4c549dc498/Untitled.png)
    

# Sliding Window

## 121 - Best Time to Buy and Sell Stock

**Intuition:** Find the maximum profit from a single transaction given daily prices of a stock, where you must buy before you can sell.

- Solutions
    
    **Brute Force:** Nested for loop
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Sliding window
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Sliding window approach to find the maximum profit by buying low and selling high, dynamically updating the pointers based on the current and next day's prices.
    
    **Unique uses:**
    
    - Uses a dynamic sliding window technique
        - It continues to slide the right side of the window until it hits some sort of parameter then moves the left side of the window

## 3 - Longest Substring Without Repeating Characters

**Intuition:** Find the length of the longest substring in a given string that contains no repeated characters.

- Solutions
    
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

**Intuition:** Find the longest substring length you can get by replacing no more than 'k' characters in the string with any other character, focusing on making the substring contain only one type of character.

- Solutions
    
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
    
    - Solution 1:  Keep track of the most frequent characters in a map, shrink the window if length of the window minus max count of the map is greater than K (the amount of letters we can replace) since max count is classified as the longest repeating character. **Then subtracting the max repeating character by length would equal the amount that we have to replace. If its greater than K than we no longer have enough to replace those characters.**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f8b86622-dae8-4442-bbb5-820e8f6cb4df/Untitled.png)
    
    - Solution 2: Instead of calculating the max count every iteration, just keep track of the max frequency. All we really care about is which letter has the highest count in a given window since the max count that is first seen will always be the answer with the longest length of a valid window.
    
    **Unique uses:**
    
    - Uses dynamic size window with auxiliary
    
    The key insight is that maxFreq in this implementation **never decreases**, even when we remove characters from the window. This is actually a clever optimization because:
    
    - If we find a longer valid window later, we'll need at least as many occurrences of some character as we found before
    - Even if the actual maximum frequency in the current window becomes smaller, keeping the old maxFreq doesn't affect the correctness because:
        - If the window is valid with a smaller actual frequency, it would also be valid with our stored larger maxFreq
        - If the window is invalid, we'll shrink it anyway due to the while condition
    
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

**Intuition:** Determine if one string's permutation can become a substring of another string, effectively checking for any sequence in the second string that includes all characters of the first string, in any order.

- Solutions
    
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
    

## 76 - Minimum Window Substring

**Intuition:** Find the smallest substring in a given string **`s`** that contains all the characters of another string **`t`**, ensuring every character in **`t`** is included in the substring at least as many times as it appears in **`t`**

- Solutions
    
    **Brute Force:** Use a nested for loop that checks for each substring then check if each substring contains valid amount of characters by creating a new set per substring
    
    - Time Complexity: O(n^2) * O(26)
    - Space Complexity: O(n) + O(m)
    
    **Optimized Approach:** Dynamic sized window, loop through dictionary counts per iteration to check if required count is valid
    
    - Time Complexity: O(n * m)
    - Space Complexity: O(n) + O(m)
    
    **Most Optimized Approach:** Dynamic sized window, check for required letters for the two strings
    
    - Time Complexity: O(n)
    - Space Complexity: O(n) + O(m)
    
    **Solution:** Count letter occurrences in t and compare it with sliding window occurrences. Use a variable to check if letter occurrences are complete (have, need)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/ddc5d4c7-0922-4495-ae0a-7f4404f99ec3/Untitled.png)
    

## 239 - Sliding Window Maximum

**Intuition:** The sliding window has a fixed size of K, find the maximum numbers per window.

- Solutions
    
    **Brute Force:** Use a max heap per window
    
    - Time Complexity: O(n) * O(k log k) → O(nk log k)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Monotonically decreasing queue using the INDEX of the array
    
    - Time Complexity: A*mortized* O(n), we will only trigger the while loop at most once each iteration to remove a smaller element from the back of the queue.
    - Space Complexity: O(n)
    
    **Solution:** Uses a monotonically decreasing queue to keep keep the highest element in the window per iteration. The index is added to the queue instead of the value so that we can keep track of which index in the array has the highest value per window.
    
    - **Example:**
        
        ```python
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        
        1. end = 0 (nums[0] = 1)
           window: [1]
           q: [0]           # index of 1
           res: []          # window not full yet
        
        2. end = 1 (nums[1] = 3)
           window: [1, 3]
           q: [1]           # 3 removes 1 since 3 > 1
           res: []          # window not full yet
        
        3. end = 2 (nums[2] = -1)
           window: [1, 3, -1]
           q: [1, 2]        # keep 3's index, add -1's index
           res: [3]         # first window complete
        
        4. end = 3 (nums[3] = -3)
           window: [3, -1, -3]
           q: [1, 2, 3]     # keep all since in descending order
           res: [3]         # add max (nums[q[0]] = 3)
        
        5. end = 4 (nums[4] = 5)
           window: [-1, -3, 5]
           q: [4]           # 5 removes everything before it
           res: [3, 5]      # add max (nums[q[0]] = 5)
        
        6. end = 5 (nums[5] = 3)
           window: [-3, 5, 3]
           q: [4, 5]        # keep 5's index, add 3's index
           res: [3, 5, 5]   # add max (nums[q[0]] = 5)
        
        7. end = 6 (nums[6] = 6)
           window: [5, 3, 6]
           q: [6]           # 6 removes everything before it
           res: [3, 5, 5, 6]
        
        8. end = 7 (nums[7] = 7)
           window: [3, 6, 7]
           q: [7]           # 7 removes everything before it
           res: [3, 5, 5, 6, 7]
        
        Final result: [3, 3, 5, 5, 6, 7]
        ```
        
    
    **Core Idea:**
    
    1. Keep track of potential maximum values in a queue
    2. Only keep numbers in decreasing order (biggest → smallest)
    3. When adding a new number:
        - Remove any smaller numbers from the back (they can never be maximum)
        - The front of queue will always be our current window's maximum
    
    ***“We only care about big numbers that could be maximum in current or future windows. Small numbers that come after big numbers don't matter because they'll never be the maximum while the big numbers are in our window.”***
    
    **Unique uses:**
    
    - Monotonically decreasing queue
        - A queue where each element is less than or equal to the previous element when traversing from front to back.
    - Amortized O(n)
        - Means that we do expensive operations within a loop but it does not happen every time, just occasionally

# Stacks

## 20 - Valid Parentheses

**Intuition:** Ensure that the first CLOSING parentheses found is matched with the last OPENING parentheses.

```python
# Valid Examples:
"()"        # Simple pair
"()[]{}"    # Multiple pairs side by side
"([{}])"    # Nested pairs
"([]{})"    # Multiple types nested
"{[]}"      # Different order of nesting

# Invalid Examples:
"("         # Unclosed bracket
")"         # No opening bracket
"(]"        # Mismatched brackets
"([)]"      # Incorrectly nested
"]{"        # Wrong order (closing before opening)
"((("       # Multiple unclosed brackets
```

- Solutions
    
    **Brute Force:** Nested for loop and counting open vs closing parentheses
    
    - Time Complexity:
    - Space Complexity:
    
    **Optimized Approach:** Use a hashmap and stack
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Uses a stack to ensure that each closing bracket correctly matches and properly follows its corresponding opening bracket, returning false if the stack is empty or the top of the stack doesn't match the expected opening bracket for a given closing bracket.
    

## 155 - Min Stack

**Intuition:** Design a stack that supports push, pop, top, and retrieving the minimum element in constant time, requiring efficient tracking of the minimum value throughout stack operations.

- Solutions
    
    **Brute Force:**  Use a min function for the entire stack array every time getMin is called
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use a second stack to place all the min numbers
    
    - Time Complexity: O(1)
    - Space Complexity: O(n)
    
    **More Readable Approach:** Use 1 stack but push arrays into it with a structure of [value, minimum value] to keep track of the min value of the current index.
    
    - Time Complexity: O(1)
    - Space Complexity: O(n)
    
    **Solution:** Use two stacks, 1 for the actual stack, the other for the min numbers for the current position of the actual stack. **Using 1 stack is much more readable.**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/dfa2452c-b65e-44bc-ac48-fcd614cf78dd/Untitled.png)
    
    **Unique uses:**
    
    - Uses a second stack to see what min number is within an array
        - Compares with a positive infinite number to find the min number
    - Uses 1 stack but pushes an array to keep track of [value, minimum value]

## 150 - Evaluate Reverse Polish Notation

**Intuition:** Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN) by using a stack to handle operators and operands in the correct order. (**post fix notation)**

```python
# Regular Math      vs      RPN (postfix)
# 3 + 4            →       3 4 +
# 3 + 4 * 2        →       3 4 2 * +
# (3 + 4) * 2      →       3 4 + 2 *
```

- Solutions
    
    **Approach:** Use a stack
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Push numbers to the stack, pop the stack when an operator shows and perform the operation on the last 2 numbers (the 2nd popped number should be first in the operation). Push the result to the stack.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a2960a10-46a4-46f9-ab2c-fcb481deac55/Untitled.png)
    
    **More Example:**
    
    ```python
    # Number LAST added to stack is at THE RIGHT SIDE OF EQUATION
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    1st operation) 9 + 3 = 12 (push 12 to stack)
    2nd) (-11 * (12 from 1st operation)) = -132 (push -132 to stack)
    3rd) (6 / (-132 from 2nd operation)) = -0.045 -> 0 (turns to 0, integer division)
    4th) 10 * 0 = 0 (push 0 to stack)
    5th) 0 + 17 = 17 (push 17 to stack)
    6th) 17 + 5 = 22 
    Output = 22
    ```
    
    **Unique uses:**
    
    - Converts a floating point number to an int to truncate to 0
        - Floor division with //, is wrong here as it truncates to -Infinity
    - isdigit() cannot be used to check if a string is a number as it only checks for 0-9
        - So we just create a string to check if the current token is an operation `"+-*/"`
    - The advantage of reverse Polish notation is that it removes the need for order of operations and parentheses that are required by [infix notation](https://en.wikipedia.org/wiki/Infix_notation) and can be evaluated linearly, left-to-right. For example, the infix expression (3 + 4) × (5 + 6) becomes 3 4 + 5 6 + × in reverse Polish notation.

## 739 - Daily Temperatures

**Intuition:** Finding the number of days until a warmer temperature for each day in a list of daily temperatures, which can be efficiently tracked using a stack to compare current and future temperatures.

- Solutions
    
    **Brute Force:** Nested for loop that checks current temperature across all temperatures except for current
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use monotonic decreasing stack
    
    - Time Complexity: O(n)
        - While loop simply pops out stack elements one by one and there can’t be more than n elements pushed inside the stack as every element is pushed once. Therefore nested while loop will also not execute more than n times. The inner loop will not be counted as a nested loop until its covers n elements.
    - Space Complexity: O(n)
    
    **Solution:** Use a monotonic decreasing 2d array stack to help find the next greatest temp number by checking if the top of the descending stack has a smaller number than the current temp.
    
    To find the difference of when the next larger temperature is for the previous temperature, we need to get the difference of the current largest temp day and compare with previous smaller temp day.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f9a49265-ddef-4476-b90d-9c15927237cb/Untitled.png)
    
    **Unique uses:**
    
    - 2D array helps keep track of what index the previous temp number was
    - Monotonic decreasing stack is uses to maintain elements in a decreasing order from the top to bottom
        - In this specific problem, we use it to find the next greatest element of multiple previous temperatures

## 853 - Car Fleets

**Intuition:** Calculate how many car fleets will arrive at a destination, considering each car's speed and position, where a car fleet forms if a slower car is caught by a faster car before reaching the target.

- Solutions
    
    **Brute Force:**  Calculate the time using a sorted list of position and speed, then iterate through the times and count the new fleets.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/fd8b7178-aeae-4c6e-b228-e6aa32b86a81/Untitled.png)
    
    - Time Complexity:  O(n log n), could become more expensive dealing with fleet mergers
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use a ~~monotonic decreasing stack,~~ not really a monotonic decreasing stack since were not actively popping the stack
    
    - Time Complexity: O(n log n)
    - Space Complexity: O(n)
    
    **Solution:** 
    
    - Zip the position and speed into a tuple (position, speed) pairing.
    - Sort tuple to get cars beside each other to easily find which cars join a fleet.
    - Reverse the array of tuples so that we don’t have to iterate the array backwards.
        - More intuitive to process right to left because we want to start with the car closes to target position.
        - It allows us to know that any car we are currently processing can only join the fleet of what we most recently processed.
        - If we started from left to right, its hard to know if we can join the car in the front since we don’t know if it already joined a fleet thats even more ahead.
    - Calculate the time it takes for a car to reach target:
        - Push it to a stack since its a new fleet due to being to slow to reach the previous fleet (fleets at the front of the car)
        - **OR** to skip iteration if it CAN join the fleet since its going fast enough to join fleet at the front.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/709ef3ff-b3eb-43dd-972b-58461f88b809/Untitled.png)
    
    **Unique uses:**
    
    - Uses sorted and zip
        - Sorted sorts an iterable list like tuples, list, dictionaries, etc.
        - Zip combines two arrays by joining the elements in the same index as a tuple
    - Uses reverse=True to reverse an array
    - Uses a ~~monotonic decrease stack algorithm~~ to find the next greater element
        - Not really a monotonic decreasing stack since we don’t actively pop elements
    - Uses physics formula: time = distance / speed

## 84 - Largest Rectangle in a Histogram

**Intuition:** Find the largest rectangle that can be formed in a histogram, represented by an array of bar heights. Use stack data structure to efficiently track the boundaries of potential rectangles.

- Solutions
    
    **Optimized Approach:** Use monotonic increasing stack
    
    - Time Complexity: O(2n) → O(n)
    - Space Complexity: O(n)
    
    **Solution:** Use a stack to maintain increasing heights and calculate the maximum rectangle area by popping from the stack when a shorter height is encountered, extending the width of rectangles to the current index.
    
    The remaining rectangles in the stack are rectangles where the heights before them were taller thus allowing them to extend their rectangle all the way to the left to the tallest height before them.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/9463fc77-71e2-4aab-8a7d-57c2d9946ec0/Untitled.png)
    
    **Example of popping heights:**
    
    We pop heights from our stack when we encounter a smaller height because:
    
    1. When we find a smaller height, it represents a "right boundary" for all taller rectangles in our stack
        - Since our stack is monotonic increasing (from bottom to top), we pop larger heights first. This helps calculate smaller heights in the loop if there are since it can be extended to the larger height.
        - Each pop calculates the maximum possible rectangle for that height, extending from its start position to our current position
    2. As we pop each height, we also learn how far left our current (smaller) height can extend
        - Each time we pop a height, we update our current height's start position to the popped height's start position
        - This works because all heights between these positions were taller, so our current height can form a valid rectangle across this entire width
    
    ```markdown
    heights = [6, 5, 2]
    indices = [0, 1, 2]
    
    When we're at index 1 (height=2):
    - Previous largest height in stack is 6
    - We can't extend the rectangle of height 6 past index 1 because 
      height 2 "cuts it off"
    - So we calculate: 6 * (2-1) = 6 * 1 = 6 as the area
    
    After calculating, the first largest height, we see there is also another
    height 5 that is bigger than 2.
    - Calculate: 5 * (2 - 0) = 5 * 2 = 10 as the area
    - The reason why the length is 2 (2-0) is because we know for sure that
      5 can extend to 6 since we know its a larger number thus creating a bigger
      rectangle.
      
    At this point, we push (2,2) to the stack, a length of 2 since we now know
    that the smaller height 2 can extend all the way to height 5. 
    Creating a new rectangle.
    
           ┌─┐
         ┌─┤6│
         │5│ │ ┌─┐
         │ │ │ │2│
         │ │ │ │ │
       ──┴─┴─┴─┴─┴──
          0 1   2
    ```
    
    **Unique uses:**
    
    - Uses monotonic increasing stack where the values in the stack are in increasing order
        - Helps find the next greater or previous greater elements

# Binary Search

## 704 - Binary Search

**Intuition:** Find the target in a sorted list

- Solutions
    
    **Brute Force:** For loop
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Divide and conquer with binary search
    
    - Time Complexity: O(logn)
    - Space Complexity: O(1)
    
    **Solution:** Binary search to find the target in a sorted array by repeatedly dividing the search array in half with two low and high pointers. If the target is less than the mid number go right, else vice-versa.
    
    **Unique uses:**
    
    - Mid number uses lo + ((hi+lo)//2) to prevent arithmetic overflow
        - Normal lo + hi // 2, could go over 32 bit integer limits

## 74 - Search a 2D Matrix

**Intuition:** Find a target value in a sorted 2D matrix

- Solutions
    
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
            - Therefore, dividing an index (**`idx`**) by **`n`** gives you the row index because it tells you how many full rows you've "passed" to reach the position represented by **`idx`**.
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

**Intuition:** Determine the minimum eating speed at which Koko can finish all the bananas within a given number of hours.

- Solutions
    
    **Brute Force:**  Create a K array (the amount of bananas Koko can eat per hour) from 1 to max of the banana in the piles then loop through each K per banana piles looking for the new minimum calculating the piles that can be eaten in less than an hour.
    
    - Time Complexity: O(p * max(P))
    - Space Complexity: O(max(P))
    
    **Optimized Approach:** Use binary search within a K array instead of just a normal for loop
    
    - Time Complexity: O(p * log(max(P)))
        - Max of the piles since we know for sure the if bananas per hour eat speed is equal to the max piles. Koko would be able to hit the hour limit.
    - Space Complexity: O(1)
    
    **Solution:** Have a low and high pointer where it is the range of amount of bananas Koko can eat per hour. Binary search this range to find the min K to check if the hours to take to eat the piles is within the hour limit.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/cb83cbe7-f454-42b8-8b5e-ed5ad3ed286e/Untitled.png)
    
    **Unique uses:**
    
    - Loops through an array within a binary search
    - Math.ceil to round up

## 153 - Find Minimum in Rotated Sorted Array

**Intuition:** Find the minimum element in a rotated sorted array

- Solutions
    
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

**Intuition:** Search for a specific target in a rotated sorted array

- Solutions
    
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

**Intuition:** Time-based key-value store that allows setting values with timestamps and retrieving the most recent value for a given key and timestamp

- Solutions
    
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

## 4 - Median of Two Sorted Arrays **** Need to go back to this ****

**Intuition:** Find the median of two sorted arrays, requiring a method to efficiently combine and balance the arrays to determine the median value.

- Solutions
    
    **Brute Force:** Just merge the two arrays and find the mid value to calculate median
    
    - Time Complexity: O(n + m)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Partition the two arrays ****
    
    - Time Complexity: O(log(m+n))
    - Space Complexity: O(1)
    
    **Solution:** Perform binary search on the shorter array to find a partition that balances the number of elements on either side, ensuring the maximum left-side element is less than or equal to the minimum right-side element, and calculating the median based on the parity of the total number of elements.
    
    Look at the visualization below to understand how it works better! Read it line by line!
    
    **Visualization:**
    
    Odd numbers
    
    ```markdown
    Step 1: Initial setup
    nums1: [1, 3, 8, 9]        length = 4 (x)
    nums2: [4, 5, 6, 7, 10]    length = 5 (y)
    Total elements = 9 (odd), so we need 5 elements in left half
    
    Step 2: Binary search process
    Try partitionX = 2 (taking 2 elements from nums1)
                            left │ right
    nums1: [1, 3 │ 8, 9]       maxX = 3, minX = 8
    nums2: [4, 5, 6 │ 7, 10]   maxY = 6, minY = 7
                    ↑
                    partitionY = 3 (need 5 total in left, so 5-2=3 from nums2)
    
    Check if valid:
    Left side max = max(maxX, maxY) = max(3, 6) = 6
    Right side min = min(minX, minY) = min(8, 7) = 7
    6 < 7, so this is valid!
    
    Final partition:
    Left half:  [1, 3] + [4, 5, 6]
    Right half: [8, 9] + [7, 10]
    
    Since total length is odd, median is max of left half = 6
    We use the max of left half since the highest number on the left half
    is the middle point of the "virtually sorted array"
    ```
    
    Even numbers
    
    ```markdown
    nums1 = [1, 3]
    nums2 = [2, 4]
    
    Step 1: Initial setup
    nums1: [1, 3]      length = 2 (x)
    nums2: [2, 4]      length = 2 (y)
    Total elements = 4 (even), so we need 2 elements in left half
    
    Step 2: Binary search process
    Try partitionX = 1 (taking 1 element from nums1)
                        left │ right
    nums1: [1 │ 3]         maxX = 1, minX = 3
    nums2: [2 │ 4]         maxY = 2, minY = 4
                ↑
                partitionY = 1
    
    Check if valid:
    Left side max = max(maxX, maxY) = max(1, 2) = 2
    Right side min = min(minX, minY) = min(3, 4) = 3
    2 < 3, so this is valid!
    
    Since length is even, median = (max(left) + min(right))/2
                                 = (2 + 3)/2 
                                 = 2.5
    ```
    
    **Unique uses:**
    
    - Uses integer division to floor to 0 so we can divide by odd or even numbers when finding the partition of second array

# Linked List

## 206 - Reversed Linked List

**Intuition:** Reverse a single linked list

- Solutions
    
    **Brute Force:** Transform it to an array, reverse array, then add it again as a linked list
    
    - Time Complexity: O(3n) → O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use temp pointers
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Point a temp pointer to ****the next current node then using the next node of the current node to point to the previous node effectively creating a reversal. The current node then becomes the temp pointer to restart the process again. 
    

## 21 - Merge Two Sorted Lists

**Intuition:** Merging two sorted lists making sure the two lists are still when merged.

- Solutions
    
    **Optimized Approach:** Singly linked list traversal
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Point the merged list to a reference to a dummy node, the dummy node will be used to traverse and create the sorted list by connecting it to the list with the smallest value each iteration.
    
    **Unique uses:**
    
    - Merged list needs to point to a dummy node to reference the head of the new sorted list as it will traverse to the tail end
    - Since while loop may exit early with a list still having remaining elements, we need to connect the dummy node to the remaining elements
    - Use Chat GPT as a visualization of how the iterative process works:
        - Initialization: mergedList -> [dummy node]
        - Moving dummy node to the next node: mergedList -> [dummy node] -> [1]
        - Moving dummy node to the next node: mergedList -> [dummy node] -> [1] -> [2]
        - Returning the next node of mergedList:  [1] -> [2]

## 141 - Linked List Cycle

**Intuition:** Check if the linked list has a cycle

- Solutions
    
    **Brute Force:** Visit each node using a set and check if the nodes value already exists
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Visit each node using pointers
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** The solution uses Floyd's Tortoise and Hare algorithm, where two pointers move at different speeds through the list, and a cycle is detected if the slow pointer meets the fast pointer.
    

## 143 - Reorder List

**Intuition:** Reorder the list where every 2nd node are the last nodes.

- Solutions
    
    **Brute Force:**  Convert linked list to array, reorder the array, rebuild the linked list
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Re-build linked list in-memory
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Find mid point using slow and fast pointers allows us to split the linked list in half, get second list from referencing slow pointer, reverse second list so that we are able to connect to the last nodes, then merge the lists. Now the list will be reordered where every 2nd node are the last nodes of the original list.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/fa7d1b48-e72c-4815-8787-405be58f4090/Untitled.png)
    
    **Finding midpoint using slow and fast pointers:**
    
    ```markdown
    Initial:
    1 -> 2 -> 3 -> 4 -> 5 -> NULL
    s,f
    
    After 1 iteration:
    1 -> 2 -> 3 -> 4 -> 5 -> NULL
         s    f
    
    After 2 iterations:
    1 -> 2 -> 3 -> 4 -> 5 -> NULL
              s         f
    
    Final (fast can't move 2 more steps):
    1 -> 2 -> 3 -> 4 -> 5 -> NULL
              s         f
    
    The key is the relationship: fast_position = 2 × slow_position
    Therefore fast must always be twice as far along as slow
    ```
    
    **Unique uses:**
    
    - Slow and fast pointers to find mid point of a linked list
    - Rebuilding a linked list in memory by referencing the head to new variables and variable point to new places in memory
    - Reversing a linked list
    - Merging two linked lists together using 2 temp pointers

## 19 - Remove Nth Node from End of List

**Intuition:** Remove the target node index starting from the end of the list.

- Solutions
    
    **Brute Force:**  Reverse the list then traverse from the reversed list to find the nth node
    
    - Time Complexity: O(2n) → O(n)
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

**Intuition:** Add two linked lists that are in reversed order already. 

- Solutions
    
    **Optimized Approach:** Normal traversal
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Adds two numbers (long addition) represented by two linked lists, digit by digit, taking care of carries and remainders, and returns the sum as a new linked list. 
    
    **NOTE: We are doing long addition from left to right instead of right to left due to the direction of the linked list**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8249d086-8e8e-46ab-b188-8c51e8aff9dc/Untitled.png)
    
    **Unique uses:**
    
    - Checks if the total number has a carry associated with it (long addition), you can do this with floor division
        - Adds the carry to next node over
        - A carry may go through at the end of a list which is an edge case. So we have to add a new node of 1
    - Checks for remainder using mod to get the 2nd digit of a number greater than 9 (e.g. 11 % 10 = 1)
    - Uses dummy node to have a reference of the head of the node were traversing through

## 287 - Find the Duplicate Number

**Intuition:** Find the duplicate number in a list using only constant space. The numbers indexes are “linked”.

- Solutions
    
    **Brute Force:**  Use a hashmap
    
    - Time Complexity:  O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use a “linked list”
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Use the indices as a “pointer” to connect to other indices by using the value of the current index. Detect the cycle and find the intersection point. Then find the cycle entry point by starting from the beginning and from the cycle intersection point 1 by 1. The distance between intersection and entry point is the same ( p = c - x) which is the duplicate value.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/296644c2-1bf3-4636-adbf-3ad0ee0c74f3/Untitled.png)
    
    **Unique uses:**
    
    - Pretends a list is a linked list by using the indices as pointers
    - **Solution:**
        - Step 1: Detect if there’s a cycle
            - A cycle tells us that there was a duplicate somewhere
            - However, it does not tell us the duplicate value.
        - Step 2: Find the cycle entry point
            - The cycle entry point is the duplicate number value (in the case above, 2 is the entry point)
                - To find entry point, we move 1 by 1 from the beginning and the cycle intersection point
                - Using mathematical proofs, the distance between entry and intersection is the same, thus finding the cycle entry point.
            - More intuitive explanation:
                
                Once they meet at the cycle intersection where loop was detected:
                
                - We know we're somewhere in the loop
                - If we start a new person at the beginning and have them move at the same pace as someone from the meeting point
                - They'll meet at the duplicate number
                - Why? Because the duplicate number is where multiple paths converge - it's the 'entrance' to our loop"

## 138 - Copy List with Random Pointer

**Intuition:** Create a deep copy of a linked list where it contains a random pointer

- Solutions
    
    **Optimized Approach:** Use a hashmap 
    
    - Time Complexity: O(n) + O(n) = O(n)
    - Space Complexity: O(n)
    
    **Solution:** Use a hashmap to map old current nodes to new nodes. 1st iteration will map with just values without the next or random pointer. 2nd iteration will map next and random pointers to the new mapped nodes due to 1st iteration. A map that is created from 1st iteration is needed as random pointers could possibly point to non-existent nodes when we begin connecting them.
    
    Without an old to new node hash map, we could end up pointing to a random node that does not exist yet.
    
    **Unique uses:**
    
    - Uses a dictionary as a key in a hash map
    - The hash map maps the new copied node as value so it allows us to map next nodes and random nodes
        - Mapping in just 1 iteration is not possible as we could map to non-existed forward nodes in the singly linked list

## 146 - LRU Cache

**Intuition:** A least recently used cache is where it removes data that has not been accessed for a certain period of time.

- Solutions
    
    **Optimized Approach:** Use a hashmap and doubly linked list
    
    - Time Complexity: O(1)
    - Space Complexity: O(n)
    
    **Solution:** Use a doubly linked list to access LRU (head) and MRU (tail). Use a hashmap to map a key to a node, helps to also access a node in O(1) time in the list, faster removal and access.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c8ffa08e-e57e-4293-885e-2f20a7e14f54/Untitled.png)
    
    **NOTE:** I’ve updated the code to make it more intuitive by making the MRU the head and the LRU the tail. It is easier to visualize this way as its similar to a structure of a stack. 
    
    **Unique uses:**
    
    - Uses a dictionary to map keys to a node for faster access to a node in a doubly linked list
    - Uses a doubly linked list to keep track of LRU (head) and MRU (tail)
    - Uses a dummy node for head and tail to prevent null pointers
    - Uses LRU eviction, when at capacity it evicts the LRU

## 23 - Merge K Sorted Lists

**Intuition:** Merge multiple sorted linked lists into a single sorted linked list, combining all the nodes from the given lists into a new list that maintains the sorted order.

- Solutions
    
    **Brute Force:** Iterate through every list and adding the value to a merged list, continuously sorting it each iteration.
    
    - Time Complexity: O(k * n), where k is the lengths of lists and n is traversing through the entire merged list
    - Space Complexity: O(N)
    
    **Optimized Approach:** Use a min heap
    
    - Time Complexity: O(n log k), where k is number of linked lists and N is total number of nodes across entire list
    - Space Complexity: O(k)
    
    **Optimized Approach:** Use pair wise merging **(more intuitive)**
    
    - Time Complexity: O(n log k), where k is the lists and n is total nodes across all lists
    - Space Complexity: O(k)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/579d126a-f6e3-4ac4-96b0-0561bfdadabc/Untitled.png)
    
    **Solution:** Heapify the first values of K linked lists into a tuple, pop the heap and add it to a merged list until the heap is empty. **Min Heap,** is the ffaster approach.
    
    **Unique uses:**
    
    - Pushes a tuple to a min heap, the tuple needs a second element to iterate to in the case that the first element (node value) contains duplicate elements in the heap already.
        - Heaps usually sort by first element unless there’s a duplicate
        - So we need to use an index so that the heap can use a unique ID to sort with next in the case of a duplicate
    - Uses pairwise combinatorics
        - Pairwise Definition:
            
            In mathematics, "pairwise" means relating to or occurring between pairs of items. It is a fundamental concept in combinatorics.
            
            Simple mathematical example:
            
            - Given set S = {1, 2, 3}
            - Pairwise comparisons would be: (1,2), (1,3), (2,3)
            
            The term is commonly used in phrases like:
            
            - "pairwise disjoint" (no two items overlap)
            - "pairwise distinct" (no two items are equal)
            - "pairwise operations" (operations performed on two elements at a time)

## 25 - Reverse Nodes in K-group

**Intuition:** Reverse nodes in a singly linked list in groups of k, meaning you should reverse the first k nodes, then the next k nodes, and so on, with any remaining nodes at the end that don't make up a full group left as they are. (remember it is **k at a time** meaning its not just first k but **every k**)

- Solutions
    
    **Optimized Approach:** Iterative solution
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Check for ‘k’ group length, reversing the group, and then reconnecting the reversed group with the rest of the list, using a dummy node for simplified edge handling.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/88c75354-a71f-4611-a851-565b1c77bbc2/Untitled.png)
    
    **The solution has 4 steps:**
    
    Step 1) Check if we have enough k nodes left to reverse
    
    Step 2) Setup the pointer to be ready for reversal
    
    Step 3) Reverse the current group
    
    Step 4) Connect prev group to the new reversed group and prep for possible next kth group
    
    **Visualization:**
    
    ```markdown
    Initial List:
    dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> [6]
      ^
      |
    groupPrev
    
    STEP 1: Check if we have k nodes left (using getKth)
    dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> [6]
      ^                    ^      ^
      |                    |      |
    groupPrev             kth   groupNext
    
    STEP 2: Set up pointers
    dummy -> [1] -> [2] -> [3] -> [4] -> [5] -> [6]
      ^      ^                    ^
      |      |                    |
    groupPrev curr               prev
             (groupPrev.next)   (groupNext)
    
    STEP 3: Reverse the group (showing each iteration)
    
    Iteration 1:
    # temp = curr.next ([2])
    # curr.next = prev ([4])
    # prev = curr ([1])
    # curr = temp ([2])
    
    dummy -> [1] ----------------> [4] -> [5] -> [6]
      ^            [2] -> [3]
      |
    groupPrev
    
    Iteration 2:
    # temp = curr.next ([3])
    # curr.next = prev ([1])
    # prev = curr ([2])
    # curr = temp ([3])
    
    dummy -> [1] ----------------> [4] -> [5] -> [6]
      ^       ↑
      |       |
    groupPrev [2] -> [3]
    
    Iteration 3:
    # temp = curr.next ([4])
    # curr.next = prev ([2])
    # prev = curr ([3])
    # curr = temp ([4])
    
    dummy -> [1] ----------------> [4] -> [5] -> [6]
      ^       ↑
      |       |
    groupPrev [2] <-- [3]
    
    STEP 4: Connect with rest of the list
    Before final connections:
    dummy       [3] -> [2] -> [1] -> [4] -> [5] -> [6]
      ^          ^           ^
      |          |           |
    groupPrev    prev    oldGroupStart
    
    After connections:
    dummy -> [3] -> [2] -> [1] -> [4] -> [5] -> [6]
                            ^
                            |
                        groupPrev (for next iteration)
    
    Ready for next group:
    dummy -> [3] -> [2] -> [1] -> [4] -> [5] -> [6]
                            ^      ^      ^      ^
                            |      |      |      |
                        groupPrev curr   kth   groupNext
    ```
    

# Binary Tree

## 226 - Invert Binary Tree

**Intuition:** All leaf nodes in a binary tree is swapped so that it is fully inverted.

- Solutions
    
    **Brute Force:** Maybe an iterative approach since we have to use arrays
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use a recursive approach
    
    - ****Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **Solution:** Do a post-order or pre-order traversal, swap the nodes when you visit the root node.
    

## 104 - Maximum Depth of Binary Tree

**Intuition:** Go deep as possible in the binary tree and return the length of its depth.

- Solutions
    
    **BFS Approach:** Maybe an iterative approach since we have to use arrays
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **DFS Approach:** Use a recursive approach
    
    - ****Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **BFS Solution:** Do a level order traversal by using a queue and adding the left and right nodes to the queue. Use a for loop with range length of queue inside a while loop to only traverse through nodes in each level.
    
    **DFS Solution:** Add a 1 for the current level then add with the max between the left and right sub tree.
    

## 543 - Diameter of Binary Tree

**Intuition:** Get the longest path between two nodes in a binary tree not including the node you started in.

- Solutions
    
    **DFS Approach:** Use a recursive approach
    
    - ****Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **DFS Solution:** Find the maximum depth ( 1+ max(..)) of each sub tree and add the left and right sub tree every time the stack pops to get max diameter. 
    
    **Unique uses:**
    
    - Nonlocal keyword to use variables outside of the scope function.

## 110 - Balanced Binary Tree

**Intuition:** Check if the binary tree does not have two sub trees where the height differs by more than one.

- Solutions
    
    **DFS Approach:** Use a recursive approach
    
    - ****Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **DFS Solution:** Find the maximum depth ( 1+ max(..)) of each sub tree then check for an imbalance between the left and right sub tree by a value of greater than 1. (e.g. 3-1 = 2, unbalanced)
    
    **Unique uses:**
    
    - Continuously return a value up the call stack if no further work is necessary

## 100 - Same Tree

**Intuition:** Check if two binary trees are the same.

- Solutions
    
    **DFS Approach:** Use a recursive approach
    
    - ****Time Complexity: O(p+q) 2 trees to traverse to
    - Space Complexity: O(h)
    
    **DFS Solution:** Traverse through both trees left and right nodes. You know their the same tree if you are able to reach the depths with a None value.
    

## 572 - Subtree of Another Tree

**Intuition:** Check if a binary tree contains the given subtree

- Solutions
    
    **DFS Approach:** Use two recursive DFS approaches
    
    - ****Time Complexity: O(m * n)
        - Where m is the nodes of the Root tree and n is the nodes of the sub root
    - Space Complexity: O(max(m, n))
        - Depends on the height of the recursion stack for either root or sub root
    
    **DFS Solution:** DFS through the root tree and run another DFS on a node of a root tree if you haven’t hit the end of the root tree. The second DFS runs a check if the root tree or sub root tree are the same trees.
    
    **Unique uses:**
    
    - Uses recursion within a recursion

## 235 - Lowest Common Ancestor of a Binary Search Tree

**Intuition:** When looking at a BST from its root downwards, the lowest common ancestor between two nodes is the lowest node in the tree that has both nodes as descendants in its subtree.

- **Example Visualization:**
    
    ```python
    '''
    Let's look at this BST:
    
                    6
                  /   \
                2       8
               / \     / \
              0   4   7   9
                 / \
                3   5
    
    Example 1: Finding LCA of nodes 2 and 8
    - LCA is 6 (root) because it's the first node that has 2 in left subtree 
      and 8 in right subtree
    
    Example 2: Finding LCA of nodes 2 and 4
    - LCA is 2 because it's the first node that has both 2 (itself) 
      and 4 in its subtree
    
    Example 3: Finding LCA of nodes 7 and 9
    - LCA is 8 because it's the first node that has 7 in left subtree 
      and 9 in right subtree
    
    Key Intuition:
    - Start from root
    - If both nodes are greater than current node, go right
    - If both nodes are less than current node, go left
    - If nodes are split (one <= current, one > current), we found LCA!
    '''
    ```
    
- Solutions
    
    **Optimized Approach:** Just traverse down the tree iteratively
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** Traverse from the root and moving left or right depending on the nodes' values, stopping when it finds the first node that is between the two target nodes or equal to one of them, leveraging the BST property where left nodes are less than the parent and right nodes are greater.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/7269b7e8-a930-4590-bc06-b8cc4c93755f/Untitled.png)
    
    **Unique uses:**
    
    - Does not use BFS or DFS to go down a tree, just go down from the root and find where to go depending on which node values are greater
    - In a BST, the LCA can be identified more straightforwardly due to the ordered properties of BSTs, where each node's left subtree contains only nodes with values less than the node's value, and the right subtree only nodes with values greater.
    - A lowest common ancestor is based on two cases:
        - If the node is between two target nodes so they are in different sub trees
            - Different subtrees means that we can’t find deeper common ancestors
        - If the node is equal to one of the target nodes
            - A node can be a descendant of itsself

## 102 - Binary Tree Level Order Traversal

**Intuition:** Find the values of a binary tree per level from left to right.

- Solutions
    
    **Optimized Approach:** BFS level order traversal
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Have a for loop that will traverse through all nodes in current level first before moving to next level with the queue
    
    **Unique uses:** 
    
    - Traverses through entire level first in BFS as opposed to looking through next level

## 98 - Validate Binary Search Tree

**Intuition:** Focus on whether each node's value strictly adheres to the BST properties—that is, all left descendants must have values less than the node’s value, and all right descendants must have values greater.

- Solutions
    
    **Optimized Approach:** DFS
    
    - Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **Solution:** Validate the range of each current node value between low and high values. Going left means change high value (next node in left subtree must have values less than current node) and going right means change low value (next node in right subtree must have values greater than current node)
    
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

**Intuition:** What are the values that we see looking at the right side of a tree, meaning we cant see values on the left since its being blocked.

- Solutions
    
    **Optimized Approach:** BFS level order traversal
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Use level order traversal BFS and grab the value of the last node in the level using the index and length of queue. Allows us to see only nodes from the right side POV.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/69ab5337-7209-40a9-b106-27a2c9fae2e0/Untitled.png)
    
    **Unique uses:** 
    
    - Traverses through entire level first in BFS as opposed to looking through next level
        - This means we have a for loop to iterate through entire level
        - The queue length only gets recalculate with the new nodes we’ve appended after the for loop is done.

## 1448 - Count Good Nodes in Binary Tree

**Intuition:** A node is considered "good" if its value is greater than or equal to all the values in the nodes along the path from the root to that node.

- Solutions
    
    **NOTE: GREAT IF YOU WANT TO UNDERSTAND HOW VALUES ARE PROPAGATED**
    
    **Optimized Approach:** DFS traversal
    
    - Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **Solution:** Use preorder DFS to be able to find the max for the current path as it resets each propagation to previous value that was passed to prevent the max for being counted along other paths. The propagated return value would be the count as we need the accumulated count for both sub trees.
    
    **Unique uses:** 
    
    - Traverses through using preorder DFS
        - Allows us to accumulate the propagated count from both left and right subtrees

## 230 - Kth Smallest Element in Tree

**Intuition:** Return the value of the kth smallest element in a Binary Search Tree

- Solutions
    
    **Optimized Approach:** Iterative DFS or Recursive DFS
    
    - Time Complexity: Same time complexity O(n)
    - Space Complexity: Iterative may have better space complexity due to non-recursive calls
    
    **Solution:** Use Inorder traversal and have a counter to check if it equals Kth number. 
    
    **Unique uses:**
    
    - Uses iterative DFS
    - Uses Inorder traversal

## 105 - Construct Binary Tree from Inorder and Preorder Traversal

**Intuition:** Use Inorder and Preorder arrays to reconstruct a binary tree.

- Solutions
    
    **Not Optimized Approach:** Using .index() every recursive call
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Mapping index instead of using .index()
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Identify the root from the preorder list, finding its position in the inorder list to divide the tree into left and right subtrees, and then recursively doing the same for each subtree.
    
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

## 124 - Binary Tree Maximum Path Sum

**Intuition:** Path must consist of a straight path and no zig zags/U shape.

- Solutions
    
    **Optimized Approach:** Use DFS, post order traversal
    
    - Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **Solution:** Go as deep as possible for the left and right subtrees and calculate a new path using both left and right paths with current root node. Then compare it with current max path sum. 
    
    Propagate the current node value + only one of the paths that has a higher value since it has to be a straight path. 
    
    We need to compare the left and right sub trees with a zero to remove any paths with negative values or else it will be included in the path calculations. E.g. A path may have -10 or -5, we will end up keeping -5 which will be included in the calculation. So its better to just remove it and possibly just keep the root node.
    
    **Unique uses:**
    
    - Comparing with 0 to prune negative valued paths

## 297 - Serialize and De-serialize Binary Tree

**Intuition:** Convert the tree into a string format that captures its structure and node values so it can be reconstructed into the original binary tree from this string representation.

- Solutions
    
    **Optimized Approach:** Use preorder traversal
    
    - Time Complexity: O(n)
    - Space Complexity: O(h)
    
    **Solution:** Use preorder traversal to serialize (encode as a string) and deserialize (decode the string) the tree. You can encode with a delimiter and then split the delimiter in the decoder.
    
    **Unique uses:**
    
    - Uses `iter` and `next`
        - `iter`  creates an iterable object from an array (mimics a stream of data)
        - `next`  will iterate to the next item in the iterable object
        - Example use:
            
            ```python
            # This is essentially what happens when we do:
            # values = iter(data.split(','))
            values_list = "1,2,N,N,3,N,N".split(',')  # ['1', '2', 'N', 'N', '3', 'N', 'N']
            iterator = TreeValuesIterator(values_list)
            
            # This is what happens when we call next(values):
            print(next(iterator))  # '1'
            print(next(iterator))  # '2'
            print(next(iterator))  # 'N'
            ```
            

# Tries

## 208 - Implement Trie (Prefix Tree)

**Intuition:** Create a prefix tree data structure

- Solutions
    
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

**Intuition:** We need to search for a word where it contains skips

- Solutions
    
    **Brute Force:**  Create a list of all inserted words then search them 1 by 1
    
    - Time Complexity: O(n * l * m) where N is # of words, L is length of words, M length of word being searched if it contains wildcards (.)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Create a trie
    
    - Time Complexity: O(n*26^L)
        - Complexity explanation
            
            Means for of *N* items, the algorithm might perform operations on all possible combinations of characters up to length *L*, with each character having 26 different choices (like the letters in the English alphabet). This complexity grows quickly with *L*, as every additional character multiplies the number of possibilities by 26
            
    - Space Complexity: O(n)
    
    **Solution:** To search for words, we need to skip the `.` character by incrementing our index (similar to backtracking) and explore each child of the current Trie node so that we can check if at some point we end up at the end of a word when we skip a letter.
    
    **Unique uses:**
    
    - Uses backtracking or DFS to go back up a node to check other children nodes in a Trie if the search has failed for the child node we went down

## 212 - Word Search 2

**Intuition:** Search for multiple words in a grid

- Solutions
    
    **Brute Force:** DFS over each word
    
    - Code Example:
        
        ```python
        # DFS for each word
        for word in words:
          for row in range(self.ROWS):
              for col in range(self.COLS):
                  if board[row][col] == word[0] and dfs(row, col, word, 0):
                      found.append(word)
                      break  # Move to next word once found
              if word in found:
                  break
        ```
        
    - Time Complexity: w * mn * 4 ^k
        - w is the word, mn is size of grid, k is length of longest word, and 4 is because we have 4 choices (up, down, left, right). 
        Example:
        
        ```
        If we're looking for a word of length 3 starting at 'E':
                             E
                    /    |    \    \
                   B     D     F     H   (4 choices)
                /|\|\   /|\|\  /|\|\  /|\|\
               A B C... A B C... (4 choices each)
        ```
        
    - Space Complexity: O(h)
    
    **Optimized Approach:** Create a trie and use it to search for multiple words
    
    - Time Complexity: mn * 4 ^ k
    - Space Complexity: O(h)
    
    This approach is inefficient for problems where the word is shown multiple times in the word search:
    
    ```
    board = [
        ["a", "a", "a"],
        ["a", "a", "a"],
        ["a", "a", "a"]
    ]
    words = ["aaa"]
    
    We will end up searching "aaa" across all directions thus 
    hitting a worst case time complexity.
    ```
    
    **Most Optimized Approach:** Similarly use a trie but remove a word from trie when its been found, prevents from finding it again similar to the issue shown above.
    
    - Time Complexity: mn * 4 ^ k
    - Space Complexity: O(h)
    
    **Solution:** Create a trie and use that to search through each word when we DFS the board.
    
    **Unique uses:**
    
    - Using array for the path and using `.join`instead of the concatenating word
        - Reduces time complexity since string concatenation could end up O(n^2)
    - `deleteWord`  function in Trie to remove a word from the Trie once its found
        - Reduces size of Trie
        - Speeds up subsequent searches
    - Add reference to the parent in each Trie node
        - Easier backtracking and prune nodes from the trie dynamically since no other words can start from that prefix

# Heap/Priority Queues

## 703 - Kth Largest Number

**Intuition:** Return the Kth largest number in an array

- Solutions
    
    **Brute Force:**  Sort the array each time and return the kth index
    
    - Time Complexity: O(nlogn)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use a min heap
    
    - ****Time Complexity:
        - Constructor: O(n) (heapify) + O(n-k)logn (popping the elements)
        - Add method: O(log k)
    - Space Complexity: O(k), array will be as large as kth elements
    
    **Solution:** Using a min-heap, maintaining a heap of size k to ensure the kth largest element is always at the top, with adjustments made upon each new addition.
    
    **Unique uses:**
    
    - Uses a heap:
        - Heapify → O(n)
        - Heappop/Heappush → O(logn)

## 1046 - Last Stone Weight

**Intuition:** Repeatedly reduce the largest two stones' weights by smashing them together until only one stone or none remains, with the new stone's weight being the difference between the two largest stones' weights if they're not equal, or discarding both if they are equal.

- Solutions
    
    **Brute Force:**  Sort the array in descending and pop values for the stones
    
    - Time Complexity: O(n) → first while loop, O(nlogn) → inside while loop = O(n^2 log n)
    - Space Complexity: O(1) → memory is in-place
    
    **Optimized Approach:** Create a max heap 
    
    - ****Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Create a max heap to get the 2 largest stones then just follow the instructions.
    
    **Unique uses:**
    
    - Creates a max heap work around by multiplying by -1

## 973 - K Closest Points to Origin

**Intuition:** Return the top K closest points to the origin on a graph

- Solutions
    
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
        - However, if there are duplicate values then it’ll use the next value in the tuple to sort

## 215 - Kth Largest Element in an Array

**Intuition:** Find the kth largest in an array

- Solutions
    
    **Brute Force:**  Sort the array or create a max heap
    
    - Time Complexity: O(nlogn) **or** O(n + klogn)
        - O(nlogn) is worse case if k is the same as the length of array
    - Space Complexity: O(n)
    
    **Optimized Approach:** Create a min heap of size k so that when we look for root of heap, its always the Kth largest element
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/38ece84c-2f4c-4e48-a832-04351aa91927/Untitled.png)
    
    - Time Complexity: O(k) + O((n-k) log k) → O(n log k)
        - O(k), heapify an array of k size
        - O((n-k) log k), heappushpop heap of size of n-k
    - Space Complexity: O(k), min heap storage
    
    **More Optimized Approach:** Quick Select (similar to quick sort) **(THIS NO LONGER WORKS, TLE) USE DUTCH THREE WAY PARTITIONING INSTEAD**
    
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
        - **Complexity**: The average time complexity of Quick Select is *O*(*n*), making it faster for its specific task than sorting the entire array and then selecting the kth element. However, its worst-case complexity can also be *O*(*n^2*), particularly with poor pivot choices.
        - **Specific Element**: Quick Select focuses on finding a single specified element's position (kth smallest or largest) without sorting the entire array.

## 621 - Task Scheduler

**Intuition:** The core idea is to arrange tasks so that the same tasks are spaced out by at least **`n`** intervals. Place the most frequent tasks first, separated by **`n`** idle time, then fill those spaces with other tasks, ensuring no idle time if possible. The challenge lies in efficiently filling these cooldown periods to minimize the total schedule time.

- Solutions
    
    **Optimized Approach:** Use a max heap and a queue
    
    - Time Complexity: O(26 + 26 log 26)
    - Space Complexity: O(n)
    
    **Solution:** Using a max heap for managing task frequencies and a cooldown queue, ensuring tasks are executed with a minimum interval **`n`**, and calculates the total execution time by dynamically adjusting tasks' availability based on cooldown requirements.
    
    Essentially just use the most frequent task to be processed first and fill in between other tasks to prevent high amount of idle times.
    
    **Unique uses:**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/de2ecef2-077b-4b41-9956-30b99e2fe08d/Untitled.png)
    
    - Uses a max heap to store the frequency of counts
    - Uses a queue so we can execute next tasks when idle time is finished

## 355 - Design Twitter

**Intuition:** Create a simplified model of Twitter where users can post tweets, follow/unfollow each other, and view the 10 most recent tweets in their newsfeed.

- Solutions
    
    **Brute Force:**  Compare each recent tweet for every user in a normal loop
    
    - Time Complexity: O(n*t log n*t) where:
        - N is number of users being followed
        - T is number of tweets per user
    - Space Complexity: O(n)
    
    This approach essentially: 
    
    - Gets ALL tweets from ALL followed users
    - Sorts ALL of them
    - Then takes top 10
    
    **Optimized Approach:** Just add each recent tweet for every user in a max heap
    
    - Time Complexity: O(K log n), each pop operation is log n and we do it at most 10 times
    - Space Complexity: O(n)
    
    This approach essentially: 
    
    - Only takes the LATEST tweet from each followed user initially
    - Uses heap to keep track of the most recent tweets
    - Only processes more tweets from a user when needed
    - Stops after finding 10 tweets
    
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

## 295 - Find Median from Data Stream

**Intuition:** Design a data structure that can efficiently find the median of a continuously growing list of numbers, ensuring quick access to the median as new numbers are added.

- Solutions
    
    **Brute Force:** Insert the numbers in order so that it is in ascending order
    
    - Time Complexity: O(n), insert it within the array where it is larger or smaller than the current number
        - Could also sort it which is worst case scenario of O(nlogn)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use a heap approach
    
    - Time Complexity: O(logn)
    - Space Complexity: O(n)
    
    **Solution:** Have two heaps, small heap is a max heap and large heap is a min heap. If at the end of inserts the heaps are equal to each other that means median is popping from both heaps. If they are not equal but instead approximately equal, then we grab the number from the the heap with a larger length which would be the median.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/89ee82e5-8c23-4833-ac28-71f91717c413/Untitled.png)
    
    **Unique uses:**
    
    - Calculates the median
        - Sort the numbers in ascending order.
        - If the number of elements is odd, the median is the middle number.
        - If the number of elements is even, the median is the average of the two middle numbers.
    - Uses two heaps
        - A max-heap to keep track of the lower half of the numbers.
        - A min-heap to keep track of the upper half of the numbers.

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
    
    - Uses list[:] to deep copy a list or you can also do list.copy()
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

## 22 - Generate Parentheses

**Intuition:** Generating all valid combinations of **`n`** pairs of parentheses, ensuring each combination is properly balanced.

- Solutions
    
    **Brute Force:** Backtracking
    
    - Time Complexity: O(2^n)
    - Space Complexity: O(n)
    
    **Solution:** Append a path string to include an open bracket if its less than the amount of `n` , exclude an open bracket and add a close bracket instead if there are greater amounts of open brackets.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/0bc255c7-7b70-458d-9be5-5ae0a61c38e1/Untitled.png)
    
    ![image.png](attachment:228ae965-cfef-4bc9-8a44-e642dfea96f0:image.png)
    
    - As an example in the picture above, see the first sub tree.
        - We found a valid parentheses where `open brackets === closed brackets === n`
        - Once that happened, we prune the search space and go ALL the way back to `“((”`
        - The reason for this is that the previous functions has already finished as it passed through the last if statement to add the closing bracket so after we popped the stack with pruning, the other functions finished thus popping more of the stack.
        - The call stack popped all the way back to `“((”`
        - Which then begins to include the next closing bracket instead as we’ve already added the 3rd closing bracket previously before the stack popped.

## 46 - Permutations

**Intuition:** Explore all possible ways to arrange a set of numbers, ensuring every number is used exactly once in each arrangement.

- Solutions
    
    **Brute Force:** Use backtracking
    
    - Time Complexity: O(n!)
    
    ```
    Why its n! complexity:
    n    2^n    n!
    1    2      1
    2    4      2
    3    8      6
    4    16     24
    5    32     120
    
    The number of permutations of a list of length n is !
    (n factorial). This is because for the first position, 
    you have n choices, for the second position  n−1 choices, 
    and so on, down to 1 choice for the last position.
    
    In the example below, we had 3 choices for the 2nd level,
    then it becomes 2 choices in the first level until down to 1 choice.
    ```
    
    - Space Complexity: O(n)
    
    **Solution:** Swap each number into the "current" position, recursively generating permutations of the remaining numbers, and backtracking to undo swaps for the next iteration.
    
    ```
                             [1,2,3]
                                |
                  ______________|______________
                 |             |              |
            [1|2,3]        [2|1,3]        [3|1,2]    <- start=0: try each number in first position
              |               |               |
           ___|___         ___|___         ___|___
          |       |       |       |       |       |
    [1,2|3]   [1,3|2] [2,1|3]   [2,3|1] [3,1|2]   [3,2|1]    <- start=1: try each number in second position
       |         |        |         |        |         |
       |         |        |         |        |         |
    [1,2,3]  [1,3,2]  [2,1,3]   [2,3,1]  [3,1,2]   [3,2,1]    <- start=2: final position
    
    Constraints: A number cannot appear more than once
    Base case: Stop when the current index has same length as input set
    First choice (inclusion): Swap current index
    Second choice (exclusion): Undo swap
    
    Example of the first left subtree:
    start = 0: [1|2,3] -> We're deciding what goes in first position
    start = 1: [1,2|3] -> First position is fixed, deciding second position
    start = 2: [1,2,3|] -> First two fixed, deciding last position
    start = 3: [1,2,3] -> All positions filled! (base case hit) back to start=2
    
    Example of backtracking after first left subtree:
     start=2: [1,2,3] -> backtrack, undo 3,3 swap
     start=1: [1,2,3] -> backtrack, undo 2,2 swap
             [1,2,3] -> now swap 2,3 to get [1,3,2]
     start=2: [1,3,2|] -> continue with new arrangement
     start=3: BASE CASE! Save [1,3,2]
     
     There are no duplicates because for example trying position 0 (start = 0):
     start=0:
        i=0: [1|2,3] → try 1 in first position
        i=1: [2|1,3] → try 2 in first position
        i=2: [3|1,2] → try 3 in first position
        
        We never try:
        - Same number twice in same position
        - Already used positions
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
       [1,2,2]  [1,2]X Skip search here since [**1**, 2, **2**] is a duplicate
    ```
    
    - **Explanation of how duplicate subsets could happen:**
        - At the root, we decide to include or not include **`1`**.
            - Including **`1`** moves us down the left branch to **`[1]`**.
            - Not including **`1`** keeps the subset empty, moving us down the right branch to **`[]`**.
        - At **`[1]`**, we decide to include the first **`2`** or not.
            - Including the first **`2`** moves us to **`[1,2]`**.
            - Not including the first **`2`** keeps us at **`[1]`**.
        - **At `[1,2]`, we face a decision with the second `2`, which is a duplicate.**
            - Including the second **`2`** moves us to **`[1,2,2]`**. This is allowed because we included the first **`2`**.
            - Not including the second **`2`** keeps us at **`[1,2]`**.
                - [1, 2] would be a duplicate so we need to prune the search here so its not included.
    
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
        - Helps prevent duplicate results when we backtrack and pop, we check the next index num. Similar to problem 3Sum and Subset 2
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
        - map(Counter, board) → Creates a counter frequency dictionary for all each letter per board row
        - sum(map(Counter, board), Counter()) → Sums all counters into one counter
        - defaultdict → Initializes a dictionary with the summed counter of all freqs for all rows
        - Example of what it looks like:
            
            ```python
            board = [["a", "b"], ["a", "c"]]
            
            # Applying Counter to each sublist
            mapped_counters = list(map(Counter, board))
            print("Counters of each sublist:", mapped_counters)  
            # [Counter({'a': 1, 'b': 1}), Counter({'a': 1, 'c': 1})]
            
            # Summing all Counters
            total_counter = sum(mapped_counters, Counter())
            print("Total Counter:", total_counter)  
            # Counter({'a': 2, 'b': 1, 'c': 1})
            
            # Creating a defaultdict from the total Counter
            count = defaultdict(int, total_counter)
            print("Final defaultdict:", count)  
            # defaultdict(<class 'int'>, {'a': 2, 'b': 1, 'c': 1})
            
            ```
            
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
    
    ![image.png](attachment:3a87557f-105d-443d-b727-03a761c83de2:image.png)
    
    **Unique uses:**
    
    - Two pointer approach to find palindromes
    - The choices for back track are the palindromes using a for loop of start and end

## 17 - Letter Combinations of a Phone Number

**Intuition:** Iterate through each digit, use the digit-to-letter map to generate all possible letter sequences.

- Solutions
    
    **Brute Force:** Backtracking
    
    - Time Complexity: O(4^n) → worst case input: “9999” = 4 x 4 x 4 x 4,
        - Worst case of 4 letters per digit that needs to be explored
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
    
    ![image.png](attachment:cee9d168-829a-4f7f-b5d9-eb886fe4c75e:image.png)
    
    **Unique uses:**
    
    - Exclusion choice for back track happens when call stack pops as path combinations is part of the parameter so no need to pop in loop

## 51 - N Queens (great to practice visualizing backtracking)

**Intuition:** Find out how many Queen pieces you can fit in a n x n chess board without the pieces eliminating each other.

- Solutions
    
    **Brute Force:** Use sets
    
    - Time Complexity: O(n ^n)
    - Space Complexity: O(n)
    
    **Solution:** Track which positions a placed Queen can eliminate by adding the positions of the board using a set, a cols set to track horizontal, posDiags and negDiags set to track diagonals. Rows do not need to be tracked as we will only surely just place 1 Queen per row since its a choice.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d915bf42-5f96-4f74-b162-2e35c27ad7a8/Untitled.png)
    
    ```
    
    ```
    
    **Unique uses:**
    
    - Uses a positive and negative diagonal set to track where a Queen can eliminate diagonal positions
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/bf12c74f-50a0-4059-be0d-1d690942e74d/Untitled.png)
    

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
    
    ![image.png](attachment:818a8ed2-c614-4587-9198-00b2890faf60:image.png)
    
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
    
    **Optimized Approach:** Traverse from the boundaries of the Pacific and Atlantic ocean then find the intersections between both. **If we don’t traverse from the boundaries, it would be hard to know if it flowed to the Pacific or Atlantic. The boundaries lets us know it can already flow from there.**
    
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
    
    **Solution:** Mark border-connected 'O's as temporary, flip all other 'O's to 'X's, then revert temporary marks back to 'O's to surround regions. 
    
    If you find a region when convert boundary “O”s as “TEMP”s, turn these into temps as well since they will never be surrounded with X’s if they are connected to a boundary ‘O’
    
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

**Intuition:** Fill each empty room with the distance to its nearest gate

- Solutions
    
    **Brute Force:** Do a DFS or BFS traversal for every cell to find the nearest gate
    
    - Time Complexity: O(mn)^2
    - Space Complexity: O(n)
    
    **Optimized Approach:** Do a BFS level order traversal for all of the gates all at once
    
    - Time Complexity: O(m *n)
    - Space Complexity: O(n)
    
    **Solution:** Do a level order traversal at every gate at the same time so that you can’t intersect different distances in the same room.  
    
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
    
    - **The Intuition:**
        
        Example of **`prerequisites = [1,0]` :**
        
        In the example "To take course 1 you should have finished course 0":
        
        - This is represented as [1,0] in the prerequisites list
        - This means: Course 1 → Course 0 (where the arrow means "depends on")
        
        Let's break down both approaches:
        
        **Current Implementation (Course → Prerequisite)**:
        
        ```python
        preMap[crs].append(pre)  *# For input [1,0], creates preMap[1] = [0]*
        ```
        
        ***Think about how it "backtracks", we complete the course when we backtrack so it goes backwards***
        
        This creates a graph where:
        
        - Each key (course) points to what you need to take before it
        - It directly answers the question: "What do I need to complete before taking this course?"
        - When doing DFS, we start at a course and check if we can complete all its prerequisites
        
        **Alternative (Prerequisite → Course)**:This would create a graph where:
        
        ```python
        preMap[pre].append(crs)  *# For input [1,0], would create preMap[0] = [1]*
        ```
        
        - Each key (prerequisite) points to what courses it unlocks
        - Less intuitive because it answers: "What courses does this unlock?"
        - Makes it harder to check if a course can be completed
        
        **The current implementation (approach 1) is more intuitive because:**
        
        - It models the dependency relationship directly
        - Makes it easier to detect cycles (if we find a course we're currently visiting)
        - Matches the natural question: "To take course X, what do I need to complete first?"
    
    **Unique uses:**
    
    - Representing a graph as an adjacency list
    - Clearing the edges for a vertex if the course has been completed
    - Using topographic ordering in a directed acyclic graph to help explore the vertices
        - To detect a loop we check if its cyclic

## 210 - Course Schedule 2

**Intuition:** Find a possible order of courses to complete based on prerequisites, similar to organizing tasks with dependencies using a directed graph to ensure all prerequisites are met before taking any course.

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

**Intuition:** Verify if a given undirected graph is a tree by checking that it's fully connected without any cycles and only one connected graph.

- Solutions
    
    **Brute Force:** DFS traversal of undirected graph
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/e2dd14c4-a100-4370-a117-9e3ea290f9cd/Untitled.png)
    
    - Time Complexity: O(V+E)
    - Space Complexity: O(V+E)
    
    **Optimized Approach:** Union Find (read code to understand)
    
    - Time Complexity: Close to O(n)
        - Worst complexity of Union Find is O(log N) but with path compression and using rank it is *O*(*α*(*N*)) → which is close to O(n)
    - Space Complexity: O(n)
    
    **Solution:** Valid tree is when there are no cycles in the graph and there is only 1 group of connections.
    

## 127 - Word Ladder

**Intuition:** Connect the words in a list and visualize it like a graph. Check the shortest path to go from the begin word to the end word based on the difference of a single letter.

- Solutions
    
    **Optimized Approach:** Create an adjacency list and do a BFS
    
    - Time Complexity:
        - Creating the adjacency list O(n*m^2)
            - n is the list of words
            - m is the length of the word
        - Doing a BFS O(n*m^2)
            - n is the list of words
            - m is the length of words,
    - Space Complexity:
    
    **Solution:** Create an adjacency list undirected graph of the patterns of the length of word where it differs by 1 letter. Traverse through the graph using level order BFS to find shortest path to end word.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/df0fa26a-0172-478c-bf57-930f9c377a54/Untitled.png)
    
    ```python
    # Above drawing was missing some nodes.
    # What the graph adjacency looks like based on example above:
    graph = {
        "*ot": ["hot", "dot", "lot"],
        "h*t": ["hot", "hit"],
        "ho*": ["hot"],
        "d*t": ["dot"],
        "do*": ["dot", "dog"],
        "*og": ["dog", "log", "cog"],
        "d*g": ["dog"],
        "l*t": ["lot"],
        "lo*": ["lot", "log"],
        "l*g": ["log"],
        "c*g": ["cog"],
        "co*": ["cog"],
        "*it": ["hit"],
        "hi*": ["hit"]
    }
    ```
    
    **Unique uses:**
    
    - BFS level order traversal
        - Visit the starting node right away and begin count at 1 since we are visiting the node right away
    - Adjacency list using list of words
        - defaultdict of list since a pattern (`*ot` , `h*t` , `ho*` ) can be found in other words

## 1584 - Min Cost to Connect All Points (Advanced)

**Intuition:** Construct a minimum spanning tree from given points in a 2D space, focusing on minimizing the total edge cost with the constraint that edges represent the Manhattan distance between points. (The weights (cost) here is the Manhattan distance from two points)

- Solutions
    
    **NOTE:** Keep in mind that the graph is a COMPLETE graph which means from any point we can connect to any other point. Therefore, algorithms like Prim does not need to be done in a traditional sense where we need to only connect to vertices we have visited.
    
    **Kruskal Approach:** Kruskal’s algorithm with sorting
    
    - How it works:
        1. Calculate the Manhattan distance between every pair of points and create a list of edges with their distances.
        2. Sort all the edges based on their distances in ascending order.
        3. Use Union-Find data structure to help in detecting cycles.
        4. Iterate through the sorted list of edges, and for each edge, if the two points are not already in the same set (i.e., not connected), connect them and add the distance to the total cost.
        5. Continue this process until all points are connected.
    - Time Complexity: O(N^2 log N) + O(N^2) = O(N^2 log N)
        - O(N^2) for calculating distances between all pairs of points, up-front
        - O(N^2 log N) for sorting the edges based on distance
    - Space Complexity: O(n^2) since storing all Manhattan distances at the beginning
    
    **Prim Approach:** Use Prim’s algorithm with a priority queue (BFS)
    
    - How it works:
        1. Start with an arbitrary point as the current vertex and add all other points with their distances to the current vertex into a min-heap.
        2. Extract the point with the minimum distance from the heap, mark it as visited, and add the distance to the total cost.
        3. Update the heap with distances to this newly visited point for all non-visited points, if the new distances are smaller.
        4. Repeat steps 2 and 3 until all points have been visited.
    - Time Complexity: O(n^2 log N) → similar to Kruskal
    - Space Complexity: O(n^2)
        - We end up storing all edges to the min heap when we visit an edge to check which point is the min cost.
    
    **Solution:** Prim's algorithm with a priority queue (min heap) to build a minimum spanning tree by iteratively adding the nearest unvisited point based on Manhattan distance, starting from point 0.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5cb007de-bf4d-4632-bd79-a94cb9a34a84/Untitled.png)
    
    **Unique uses:**
    
    - Uses Prim’s and Kruskal’s algorithm to get the minimum cost of a weighted tree
        - Starting at 0,0 is a common strategy for Prims algorithm
    - Manhattan Distance: ***The distance between two points measured along axes at right angles***.
        - Also useful in scenarios where movement is restricted to only horizontally and vertically directions, such as navigating a city with a grid-like street layout.
            - Not allowed diagonally.
        - In this case, its used to determine the smallest edge to add to MST in Prims algorithm.
    - The graph is a **COMPLETE** graph where we can connect to any point from a point.

## 743 - Network Delay Time (Advanced)

**Intuition:** Find the minimum time it takes for a signal to reach all nodes in a network, starting from a given node; think of spreading out from the starting node to cover the entire network, using the shortest path to each node based on the time delays along different paths.

- Solutions
    
    **Brute Force:** Bellman Ford’s algorithm
    
    - Time Complexity: O(V*E) → O(V^2)
        - O(V^2) since vertices could be proportional to size of edges
    - Space Complexity: O(V)
        - Our distance list will be the same size of vertices
    - Easier to understand
    - **Solution Example**
        
        ## **Initialization:**
        
        `distances = [inf, inf, 0, inf, inf]  # 0-indexed is unused, distances[2] = 0`
        
        ## **Iteration 1:**
        
        Process edges:
        
        - Edge (2,1,1): distances[2] = 0, so distances[1] = 0 + 1 = 1
        - Edge (2,3,1): distances[2] = 0, so distances[3] = 0 + 1 = 1
        - Edge (3,4,1): distances[3] = 1, so distances[4] = 1 + 1 = 2
        
        After iteration 1:
        
        `distances = [inf, 1, 0, 1, 2]`
        
        ## **Iteration 2:**
        
        Process edges:
        
        - Edge (2,1,1): distances[2] = 0, distances[1] = 1. No update needed.
        - Edge (2,3,1): distances[2] = 0, distances[3] = 1. No update needed.
        - Edge (3,4,1): distances[3] = 1, distances[4] = 2. No update needed.
        
        No updates occurred, so we break early.
        
        ## **Iteration 3:**
        
        We don't reach this iteration because of the early termination.
        
    
    **Optimized Approach:** Use Dijkstra’s algorithm BFS
    
    - Time Complexity: *O*(*E*log*E*)+*O*(*E*)+*O*(V)
        - Graph construction: O(E)
        - Time mapping: O(V)
        - Dijkstra’s algorithm: O(E log E), each edge can result in a heap operation
    - Space Complexity: O(V + E)
    - **Solution Example**
        
        For the example: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        
        ## **Initial State**
        
        - Distance map: {1: inf, 2: 0, 3: inf, 4: inf}
        - Min heap: [(0, 2)] (time, node)
        - Visited: {}
        
        ## **Step 1: Process node 2**
        
        - Pop (0, 2) from heap
        - Mark node 2 as visited
        - Process neighbors:
            - Update node 1: distance = 1
            - Update node 3: distance = 1
        - New state:
            - Distance map: {1: 1, 2: 0, 3: 1, 4: inf}
            - Min heap: [(1, 1), (1, 3)]
            - Visited: {2}
        
        ## **Step 2: Process node 1**
        
        - Pop (1, 1) from heap
        - Mark node 1 as visited
        - No neighbors to process
        - New state:
            - Distance map: {1: 1, 2: 0, 3: 1, 4: inf}
            - Min heap: [(1, 3)]
            - Visited: {1, 2}
        
        ## **Step 3: Process node 3**
        
        - Pop (1, 3) from heap
        - Mark node 3 as visited
        - Process neighbors:
            - Update node 4: distance = 2
        - New state:
            - Distance map: {1: 1, 2: 0, 3: 1, 4: 2}
            - Min heap: [(2, 4)]
            - Visited: {1, 2, 3}
        
        ## **Step 4: Process node 4**
        
        - Pop (2, 4) from heap
        - Mark node 4 as visited
        - No neighbors to process
        - New state:
            - Distance map: {1: 1, 2: 0, 3: 1, 4: 2}
            - Min heap: []
            - Visited: {1, 2, 3, 4}
        
        ## **Final Result**
        
        - All nodes visited
        - Maximum distance = 2
        - Return: 2
    
    **Solution:** Uses Dijkstra’s algorithm to find the shortest path to make all nodes receive the network.
    
    **Unique uses:**
    
    - Uses Dijkstra’s algorithm to find the shortest path to make all nodes receive the network.

## 787 - Cheapest Flights within K Stops (Advanced)

**Intuition:** Find the cheapest flight price from a starting city to a destination city, given a maximum number of stops, by exploring different flight routes and their costs.

- Solutions
    
    **Brute Force:** Using a BFS with a priority queue
    
    - Time Complexity: O(E * K) → TLE error
    - Space Complexity: O(E)
    
    **Optimized Approach:** Bellman Ford’s algorithm within K stops
    Bellman Ford and BFS with a priority queue does have similar time complexity
    
    - Time Complexity: O(|E| * K)
        - Usually O(|V| * |E|) → O(V^2), but we can optimize to only do it within K stops
    - Space Complexity: O(V)
    
    **Optimized Approach:** Dijkstra’s algorithm
    
    - Time Complexity: O((E + V log V)
    - Space Complexity: O(V + E)
    
    **Solution:** Update flight prices to find the cheapest price from source to destination within k stops by relaxing all edges up to k+1 times, ensuring the minimum cost path is considered even if direct flights are not available.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/3ca1edd1-b177-4992-a976-17731511b9f1/Untitled.png)
    
    **Unique uses:**
    
    - Uses Bellman Ford’s algorithm within K stops instead of all the way up to |V| - 1 times of edge relaxation
        - This means we need to deep copy the prices of the previous iteration to not mix updates from the same iteration to ensure that we do not do **multi-hops.**
        - The constraint here is that we need to do it at k-stops and keeping the same distances array cascades the in-place array to allow us to hop multiple times per relaxed edge.
        - See example here why we copy: ‣

## 332 - Reconstruct Itinerary (Advanced)

**Intuition:** Create a valid itinerary that includes all tickets once (use 1 edge once). It is a valid itinerary when the result of the visited edges are in lexical order (alphabetical order).

- Solutions
    
    **Brute Force: Sort each vertex’s edges in lexical order and use pop(0)**
    
    - Time Complexity: O(E^2)
        - **Graph Construction:** O(E), create graph then we sort later
        - **Sorting Adjacency Lists:** O(E Log E) → sorting each vertex edges
        - **DFS traversal with pop(0):** O(E^2)
            - First O(E) is traversal with DFS
            - Second O(E) is pop(0) will need to iterate through entire array to pop first index in array
            - Creates O(E^2)
    - Space Complexity: O(E)
    
    **Optimized Approach: Use a min heap and queue**
    
    - Time Complexity: O(E Log E)
        - **Graph Construction**: O(Elog⁡E),
            - Heap push each edge
        - **DFS Traversal**: O(Elog⁡E)
            - Heap pop each node to get smallest lexical destination
        - **Overall**: O(Elog⁡E)
    - Space Complexity: O(E)
    
    **Solution:** 
    
    - Create an adjacency list graph.
    - When creating the graph, the graph will be pushing to the list (min heap).
    - Trigger a post order DFS (visit all children vertices then process them),
        - For each node, heap pop so we grab nodes in the adjacency list in lexical order
    - Process the node after visiting all children
        - Add it to a queue using append left (added to left of array) instead of push (added to end of array) so that its in reverse order
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/b35e3516-36af-4271-852b-59c815ef1dac/Untitled.png)
    
    **Unique uses:**
    
    - Uses a while loop in DFS traversal of graph to traverse through all nodes instead of for loop
        - Allows us to heap pop the nodes rather than a for loop that just iterates through the list in order
    - Backtracks by exploring as deep possible first then when we explore it, we add it to the queue result that adds it in reverse order
        - Uses post order traversal
    - Similar to topographical sort traversal

## 778 - Swim in Rising Water (Advanced)

**Intuition:** Find the minimum time to reach the bottom-right corner from the top-left corner of a grid. Time is measured by water elevation rising because it is raining. Let’s say adjacent cells are 2 and 3, we have to wait till water rise to that level. 

If we go to 2, we need to wait a time of 2, if we go to 3, we wait a time of 3. The time is determined by the highest water level you encounter on your path. So if the next cells after the 3 is 1, then time is still 3 because we don’t have to wait for the water to rise to get to cell 1.

- Solutions
    
    **Optimized Approach:** Use Djikstra’s algorithm to get the shortest path to bottom right corner
    
    - Time Complexity: O(n^2 log n)
        - n^2 since grid is size of n x n
        - log n since we do a heap push every n
    - Space Complexity: O(n^2)
    
    **Solution:** Check for the shortest path where the elevation in your path is less or equal to the time. Do this by modifying Djikstra’s algorithm by doing a BFS with a min heap but instead you don’t need to measure the distances for all vertices, just keep track of the highest time in the path.
    
    **Unique uses:**
    
    - Modified Djikstra’s algorithm
        - Does not keep track of all distances from source to vertex but keeps track of highest distance (max time/height) instead.

## 269 - Alien Dictionary (Advanced)

**Intuition:** The alien language has its own ordering of letters that's different from English. Figure out how the alphabets are ordered in the Alien Dictionary by checking which letters are lexicographically smaller in a list of words that are **already** sorted lexically. 
For example, `ac` and `ab`  → `c` < `b` which means c comes before b in the alien language which is wrong for english language.

**Lexicographically definition:** 

String `a` letter is lexicographically smaller than string `b` letter when comparing two words:

1. The first difference in letters determines the order (e.g., "`hrn`" and "`hrf`", where 'f' is lexicographically smaller than 'n', so "`hrf`" is smaller than "`hrn`")
2. If one string is a prefix of the other, the shorter string is lexicographically smaller.
    1. Example: "`cat`" vs "`caterpillar`" → "`cat`" is a **prefix** of "`caterpillar`", so "`cat`" is **smaller** than "`caterpillar`".
- Solutions
    
    **Optimized Approach:** Topological sort
    
    - Time Complexity: O(C)
        - Where C is the total number of characters across all words in the input list
        - Building the graph takes O(C) time as we iterate through each character in each word once
        - The topological sort (DFS) visits each character in the alien alphabet at most once, and each edge at most once
    - Space Complexity: O(1) or O(U)
        - Where U is the number of unique characters in the alien alphabet
        - Since we're dealing with lowercase letters, the graph can have at most 26 nodes (if we assume only lowercase English letters)
        - The visited, completed sets, and order deque each take O(U) space
        - The recursion stack for DFS can go up to O(U) in the worst case
        - If we consider the alphabet size as constant (26 letters), then the space complexity is O(1)
        - Otherwise, it's O(U) where U is the number of unique characters
    
    **Solution:** Build a directed graph from adjacent words in the sorted list, where edges represent the relative ordering of letters in the alien language (for example, if "ac" comes before "ab", then 'c' comes before 'b' in the alien alphabet). 
    
    A topological sort is then performed on this graph to derive a valid ordering of the alien alphabet, returning an empty string if any contradictions (cycles) are detected, which indicates the ordering rules are inconsistent.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/9f7ca770-e3df-4016-b2ea-31cce3799fc4/Untitled.png)
    

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

**Intuition:** Find out the min cost of current step i, where you can either take 1 or 2 steps at a time selecting the most minimum cost per step.

- Solutions
    
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
        
        | **Index/Unmatched `j`** | **0** | **1** | **2** | **3** |
        | --- | --- | --- | --- | --- |
        | **0 (Start)** | T | F | F | F |
        | **1 ('(')** | F | T | F | F |
        | **2 ('*')** | T | T | T | F |
        | **3 (')')** | F | T | T | F |
        | **4 (')')** | T | F | F | F |
        
        ### **Explanation of Each Row:**
        
        - **Row 0**: Before any characters are processed. Only **`dp[0][0]`** is true, indicating zero unmatched parentheses are possible with zero characters processed.
        - **Row 1** (**`'('`**):
            - **`dp[1][1]`** becomes true because processing **`(`** increases the unmatched count by 1 (from **`dp[0][0]`**).
        - **Row 2** (**`'*'`**):
            - **`dp[2][0]`**: True because  can act as an empty character, carrying over **`dp[1][0]`** (not applicable here).
            - **`dp[2][1]`**: True because  can act as **`(`**, increasing the unmatched count from **`dp[1][0]`**.
            - **`dp[2][2]`**: True because  can also act as **`(`**, increasing the unmatched count from **`dp[1][1]`**.
        - **Row 3** (**`')'`**):
            - **`dp[3][0]`**: Remains false because you cannot have zero unmatched parentheses after an odd number of symbols unless compensated by a .
            - **`dp[3][1]`**: True because **`)`** decreases the unmatched count by 1 from **`dp[2][2]`**.
            - **`dp[3][2]`**: True as **`)`** decreases the unmatched count by 1 from **`dp[2][3]`** (if it were applicable).
        - **Row 4** (**`')'`**):
            - **`dp[4][0]`**: True because **`)`** can reduce the unmatched count from **`dp[3][1]`** to zero, balancing all open parentheses.
        
        ### **How to Read the Table:**
        
        - Each **column** represents a possible number of unmatched opening parentheses (**`j`**) after processing the first **`i`** characters.
        - Each **row** corresponds to processing another character in the string, updating possible states based on the character's nature (**`(`** increases, **`)`** decreases,  has multiple effects).
    
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

## 435 - Non-overlapping intervals

**Intuition:** Find the min amount of intervals you need to remove to make the rest of intervals non-overlapping.

- Solutions
    
    **Optimized Approach:** Greedy approach, sorting by end times to find which intervals end earliest
    
    - Time Complexity: O(nlogn)
    - Space Complexity: O(1)
    
    **Solution:** Greedily choose the intervals the end earliest but remove the ones that are overlapped and end longer. Allows us to maximize the amount of intervals we need to remove as it frees up future intervals. Essentially freeing up our “calendar”
    
    **Unique uses:**
    
    - Sorts by end times as opposed to start times to find which intervals end earlier
    - Greedy algorithm always selecting the earliest time

## 253 - Meeting Room 2

**Intuition:** Determine the minimum number of conference rooms needed to host all given meetings without overlaps. Each meeting has a start time and an end time, and the goal is to allocate meeting rooms such that no two meetings overlap in the same room.

- Solutions
    
    **Optimized approach:**
    
    - Time Complexity: O(2n*logn) → O(nlogn)
    - Space Complexity: O(n)
    
    **Solution:** Uses a min-heap to efficiently track and manage the minimum number of meeting rooms needed by comparing start times with the earliest available room's end time.
    
    **Unique uses:**
    
    - Uses a heap to be able to figure out the unique amount of conference rooms using the end time

# Math & Geometry

## 202 - Happy Number

**Intuition:** Repeatedly replace a number with the sum of the squares of its digits will eventually result in the number 1, indicating it's "happy," or if it falls into a cycle that does not include 1, proving it's not "happy.”

- Solutions
    
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

**Intuition:** Add one to a number represented as an array of its digits, handling any carry that results from adding one to the most significant digit.

- Solutions
    
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

## 48 - Rotate Image

**Intuition:** Rotate a square matrix (2D array) by 90 degrees to the right, modifying the matrix in place without using an additional matrix for the transformation.

- Solutions
    
    **More Intuitive Solution:** Transpose the matrix then reverse
    
    ```python
    OG Matrix:
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    
    Tranposed Matrix (swap rows and columns, turn rows into columns):
    [1, 4, 7]
    [2, 5, 8]
    [3, 6, 9]
    
    Reverse each row:
    [7, 4, 1] 
    [8, 5, 2]
    [9, 6, 3] 
    ```
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Uses two pointer approach, layer by layer
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/2aebcaeb-08ce-4c36-b3a7-1a6e8b2ff40a/Untitled.png)
    
    - Time Complexity:O(n^2)
    - Space Complexity: O(1)
    
    **Unique uses:**
    
    - Uses four pointers

## 54 - Spiral Matrix

**Intuition:** Need to traverse through the matrix in a spiral order

- Solutions
    
    **Optimized Approach:** Continuously shrink boundaries
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/f190f70e-9def-4823-a052-fbfca16436f5/Untitled.png)
    
    - Time Complexity: O(n^2)
    - Space Complexity: O(n)
    
    **Solution:** Use four pointers to get a boundary from left, right, bottom and top. Shrink and expand the boundaries depending on where we are iterating. Stop when boundaries cross.
    
    **Unique uses:**
    
    - Uses four pointers approach in matrix again

## 73 - Set Matrix to Zeroes

**Intuition:** Modify a matrix in place such that if an element is 0, all elements in its entire row and column are set to 0, using constant extra space to achieve this.

- Solutions
    
    **Brute Force:** Copy the matrix and fill it with zeros
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/7efba6ad-4a71-456b-9c31-10a7e3609947/Untitled.png)
    
    - Time Complexity: O(m*n)
    - Space Complexity: O(m*n)
    
    **Optimized Approach:** Create a rows and cols array and fill it based on where we hit a zero
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/60ea40bc-5388-4c69-b2cc-a97b10310539/Untitled.png)
    
    - Time Complexity: O(m*n)
    - Space Complexity: O(m + n)
    
    **More Optimized Approach:** Add the tracker as zeros in-place within the matrix based on where the zeros are.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/6bf33017-2f54-44e7-a951-a6cc072b8736/Untitled.png)
    
    - Time Complexity: O(m*n)
    - Space Complexity: O(1)

## 50 - Pow(x, n)

**Intuition:** Compute *x* raised to the power of 𝑛 efficiently, handling both positive and negative exponents.

- Solutions
    
    **Brute Force:** One for loop, 2*2*2*2 etc
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Optimized Approach:** Divide and conquer
    
    - Time Complexity: O(log n)
    - Space Complexity: O(1)
    - How it works
        - **Efficiency**: Each time you square the base and halve the exponent, you're doing much less work than multiplying **`x`** by itself **`n`** times. This drastically reduces the computational steps from **`n`** multiplications to about log2(*n*) multiplications.
        - **Divide and Conquer**: This is a classic divide and conquer algorithm because it breaks down a large problem (computing *xn*) into smaller problems of the same type (computing (*x*2)*n*/2), solving them recursively, and combining their results.
    
    **Solution:** Using a recursive approach that squares the base and halves the exponent, with a correction for negative exponents by taking the reciprocal. Divides and conquer the calculation.
    
    **Unique uses:**
    
    - Negative exponents → 1/2*2*2*2 etc. Its the inverse.
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/b9933ced-cc5f-44ff-864a-fbbd1bb09565/Untitled.png)
    

## 43 - Multiply Strings

**Intuition:** Multiply two non-negative integers represented as strings and return the result as a string, without using built-in big integer libraries, simulating the manual multiplication process used in elementary arithmetic.

- Solutions
    
    **Optimized Approach:** Reverse iteration and carry. Add the results in an array and keep track of the position in the array. Use similar elementary arithmetic
    
    - Time Complexity: O(mn)
    - Space Complexity: O(mn)

## 2013 - Detect Squares

**Intuition:** Design a data structure that can efficiently count and add points on a 2D plane, and determine how many squares can be formed that have one of their vertices as a point you have previously added.

- Solutions
    
    **Brute Force:** Create a loop per point and check if the four points are a square.
    
    - Time Complexity: O(n^3),
    - Space Complexity: O(n)
    
    **Optimized Approach:** One loop
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Detect a square by using diagonal points and a hashmap to look for duplicates
    
    **Unique uses:**
    
    - Detecting a square/rectangle from a grid:
        - Find the diagonal point from the queried point
        - Use the height and length difference from the diagonal point to figure out if the other points have the correct amount of difference.
        - Allows us to figure out if its a square.
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/252f383f-5712-4159-9416-ba579a926cc7/Untitled.png)
        

# Bit Manipulation

**Guide: [How to Solve: Bit Manipulation](https://www.notion.so/How-to-Solve-Bit-Manipulation-8f8e50b940144e84b5eb6925ce4f4c7a?pvs=21)** 

## 136 - Single Number

- Solutions
    
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

- Solutions
    
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
    
    **Solution:** Use AND operator of the value with “1” → “0001”, checks if right most bit of a digit is a 1 then we shift >> the number by 1, to filter out the right-most digit. Cycle until 32 bit is complete.
    
    **Unique uses:**
    
    - Uses shift operator and AND operator

## 338 - Counting Bits (Dynamic Programming too)

- Solutions
    
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

- Solutions
    
    **Brute Force:**  Manipulate it as a string and just reverse the string
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Optimized Approach:** Use shifts and bitwise operators to manipulate a new result array
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/90952219-5da7-4b62-9ad6-770760f1ab3e/Untitled.png)
    
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    
    **Solution:** Reverses the bits of an integer by shifting the result leftward to accumulate each rightmost bit of the input number.
    

## 268 - Missing Number

- Solutions
    
    **Brute Force:  Loop over 0 to n, use (if i not in nums) check which is an O(n) operation**
    
    - Time Complexity: O(n^2) due to the check inside the for loop
    - Space Complexity: O(1)
    
    **Optimized Approach:** Use bit manipulation
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d480ec6a-bab5-4434-977e-9ab7f46b3c4c/Untitled.png)
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:** 
    
    - You can XOR all indices and values, including **`n`** (since the array is from **`0`** to **`n-1`**), and the result will be the missing number because the missing number will not be cancelled out.
    - We are pretty much XORing indices from 0 to n, with the numbers array. It will end up finding the missing number because there will be 1 number from the indices that is not the same as the number array.
    
    **Unique uses:**
    
    - Uses XOR
        - A number XOR itself gives 0.
        - A number XOR 0 gives the number itself.
        - XOR is commutative and associative.
    - Use arithmetic series formula for summation optimized approach
    

## 371 - Sum of Two Integers

- Solutions
    
    **Optimized Approach:** Use bit manipulation
    
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    
    **Solution:**  Use XOR to simulate bit addition, then calculate carry by complementing and shifting by 1.
    
    **Unique uses:**
    
    - XOR mimics bit addition for binary numbers
    - For carries:
        - `&`  finds where both bits are 1, indicating a carry is generated
        - `<<` by 1 will move the carry to correct position for next addition iteration
    - Masking
        - `0xFFFFFFFF` , complementing with this ensures that numbers are treated as 32 bit integers
        - `ox7FFFFFFF` , determines if number is outside positive range of 32 bit integer
        

## 7 - Reverse Integer

- Solutions
    
    **Optimized Approach:** Handle overflows and underflows
    
    - Time Complexity: O(log n)
    - Space Complexity: O(1)
    
    **Solution:** 
    
    **Unique uses:**
    
    - Helps find int overflow and underflow
    - Uses fmod to handle negative numbers, e.g. -1 % 10 = -1 instead of 9
    - Multiplies by 10 to shift number to left and appends the next number by adding