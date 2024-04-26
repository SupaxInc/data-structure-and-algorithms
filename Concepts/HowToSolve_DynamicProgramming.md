https://www.youtube.com/watch?v=Clp5c7HvLqs

# Example 1: Longest Increasing Subsequence

## Step 1) Visualize examples

- Find a way to visualize an example
- A great way to visualize programming in DP’s is the **directed acyclic graph**
    1. Picture an element as a node
    - Create an edge from one node to another
- An example:
    - Create a directed acyclic graph of: LIS([3, 1, 8, 2, 5])
        - Create a directed edge from one node to another when it has a larger value
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/72e0097c-9331-4178-a7f0-1a1499444760/Untitled.png)
    
    - The longest length above is a length of 3
        - It is just the longest path of the graph
        - **LIS = Longest Path in DAG + 1**
        - + 1 → since we are counting nodes and not just edges

## Step 2) Find an appropriate sub-problem

- ***A sub problem is a simpler version of the overall problem***
    - Focus on what we know about the current problem:
        1. We know that the increasing subsequence are subsets of an original sequence
        2. All increasing subsequences have a start and end point
    - Modify one of what we know about the problem above to create a sub-problem
        - We will use #2: *all increasing subsequences have a start and end point*
        - However, let’s focus on the end index of an increasing subsequence
    - Identify a subproblem as: **LIS[k] = LIS ending at index k**
        - An example of an LIS[3] → LIS ending at index 3
        
        ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/7f972654-5caf-4f5f-b73b-64dfd24de587/Untitled.png)
        
        - LIS[3] = paths: 3 → 8 or 1→ 8 or 1 → 2
        - LIS[3] = Longest Path in DAG + 1 = 1 + 1 = 2
        

## Step 3) Find Relationships Among Sub-Problems

- Helps asking yourself questions in this step
- For example, trying to find, LIS[4], longest increasing subsequence at index 4
    - What subproblems are needed to solve LIS[4]?
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/3b6044b0-15fe-4093-9dfc-79fcd12debab/Untitled.png)
    
    - It is clear from the visualization above what the sub problems are
    - We know that one path from index 4, needs to go through index 0
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/28d19fbd-2a1a-4984-b53a-a4d75fa77017/Untitled.png)
    
    - So we need to know LIS[0], LIS ending an index 0
        - LIS[0] = Longest Path in DAG + 1 = 0 + 1 = 1
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/cef6e99d-97c3-429c-96e3-4f48267c83f3/Untitled.png)
    
    - Then we need to know: LIS[1], LIS ending at index 1
        - LIS[1] = 0 + 1 = 1
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/16cad3b7-8fb4-4cff-a953-331831a648d0/Untitled.png)
    
    - The final possible path to index 4 is: LIS[3]
        - LIS[3] = 3 → 8 or 1 → 8 or 1 → 2 = 1 + 1 = 2
    - Now we know the relationship to index 4 here is:
        - LIS[4] = max{LIS[0], LIS[1], LIS[3]} + 1 = 2 + 1 = 3
        - The max of all previous subproblems leads to the length of index 4
    - Similarly, maybe finding index 3:
        - LIS[3] = max{LIS[0], LIS[1], LIS[2]} + 1 = max{1, 1, 2} + 1 = 2 + 1 = 3

## Step 4) Generalize the relationship

- Think about how we can solve LIS[5]
    - We can generalize the relationship with the equation:
    LIS[5] = 1 + max{k < 5, A[k] < A[5]}
        - We will only choose subproblems ending at index k, if k is less than 5 and the value at index k is less than the value at index 5
    - You can see below:
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/723f1ac9-f7dd-452a-a596-e620f2522c23/Untitled.png)
    
    - This applies for any nth index:
    LIS[n] = 1 + max{k < n, A[k] < A[n]}

## Step 5) Implement by solving subproblems in order

```python
def lis(A):
	# Initialize an array length of array A, all to 1 
	# since every increasing subsequence will have at least 1 element
	# e.g. len(A) = 3, [1, 1, 1]
	L = [1] * len(A) 
	for i in range(1, len(L):
		# First find the necessary sub problems
		subproblems = [L[k] for k in range(i) if A[k] < A[i]]
		# Update the length according to the generalizaiton we specified
		L[i] = 1 + max(subproblems, default = 0)
	return max(L, default = 0)
	
```

# Example 2: Min Cost Climbing Stairs

## Step 1) Visualize Examples

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/31c526eb-11a0-4489-8c4e-107d0b0b7d0a/Untitled.png)

- We created a DAG above to get to the end of the cost array.
- We can either take 1 or 2 steps.
- The minimum cost per step depends on the steps we took previously.

## Step 2) Find an appropriate sub-problem

- ***A sub problem is a simpler version of the overall problem***
    - The overall problem is to find the minimum cost to reach the top of the stairs.
    - The simpler version is to find the minimum cost based on index k
        - So the paths we need to pass through to reach the top of the stairs
    - We know that:
        - There is a start and end index
        - The steps we take contribute to the overall goal of minimizing the cost to the top of the stairs.
    - So lets begin with some sub problems:
        - Sub-problem 1: What is the min cost to reach step 0?
            - There is only one step to take so min cost is 10.
            - This becomes a base case. Since we have no choice as the top of the stairs is step 0.
        - Sub-problem 2: What is the min cost to reach step 1?
            - We can take 1 or 2 steps, so the min cost depends on the min between step 0 or step 1.
            - So we can either:
                1. Directly go to step 0
                2. Directly go to step 1
            - This also becomes a base case.
        - Sub-problem 3: What is the min cost to reach step 2?
            - Similarly to sub problem 2, we can either:
                1. Come from step 0
                2. Or come from step 1
            - We would choose what the previous min costs was between step 0 or step 1.

## Step 3) Find relationships among sub-problems

- What are the relationships amongst the sub-problems?
    - Sub-problem 1 is sort of independent since there is only 1 step to take, step 0.
        - Direct calculation
    - Sub-problem 2 is also independent as we can directly step on step 1.
        - Direct calculation
    - Sub-problem 3 has a difference since we need to know the cumulative steps that have been taken already between step 0 or 1.
        - If we add more steps, it would create sub-problem 4, and sub-problem 4 would be the same as sub-problem 3.
    - **In sub-problem 4, it becomes a recurrence relation because the choice we make for each step is based on outcomes of previous steps.**
- So for step 2:
    - If we know the outcomes of step 0 and step 1, it lets us know what the min **total** cost would be for step 2
    - This is due to the fact that we accumulate the total costs per each step
    - And the previous steps has already accumulated through the different step selections

 

## Step 4) Generalize the relationship

- Now we know based on our additional sub-problem 4 which adds further steps to see the recurrence relation.
- We can generalize the relationship between sub-problem 3 and sub-problem 4.
- Instead of a direct calculation (which are base cases)
- We have more of a cumulative approach to get the min cost for step 2 or step 3 (new step)
- Example, lets say its now [10, 15, 21, 20]
    - For step 2:
        - MCCS[2] = cost[2] + min(step 0 min cost, step 1 min cost) = 21 + 10 = 31
    - For step 3:
        - MCCS[3] = cost [3] + min(step 1 min cost, step 2 min cost) = 20 + 15 = 35
- Now we can generalize the relationship as:
    - **MCCS[k] = cost[k] + min(MCCS[k-1], MCCS[k-2]**

## Step 5) Implement the solution

- We can now choose between top down or bottom up approach
    - Top down is recursive
    - Bottom up is tabulation
- Our base cases as we know is to take either step 0 or step 1 since we can **directly** step on one of the first 2 steps.

# Solutions:

## **LOOK INTO THE FUTURE, TO GET THE FORMULA OF THE PAST**

- **Memoization** is typically used in the context of a **top-down approach**. In this approach, you start solving the problem by breaking it down into smaller subproblems recursively and storing the results of these subproblems in a cache (often a dictionary or array) to avoid redundant calculations. Memoization is a technique where you "remember" the results of expensive function calls and return the cached result when the same inputs occur again.
- **Bottom-up approach**, also known as **tabulation**, involves solving the problem by starting with the smallest subproblems and iteratively building up the solution to the larger problem. In this approach, you typically use an array or table to store the results of subproblems (this can also be seen as a form of caching), but the process is iterative, not recursive. The solution to the entire problem is built iteratively by filling up this table based on the solutions to smaller subproblems.
- **A sub problem is a simpler version of the overall problem**

## What a redditor said to turn top down to bottom up:

```python
No, it won’t be ok if they’re expecting an optimal solution. Sorry if that’s not what you want to hear.

The good news is the recursive solution is the hardest part. Once you’ve done that converting it to a dp solution is fairly process oriented and you just need to make sure you don’t miss edge cases. Dm me if you want a better explanation of that process. I tried typing out an example in this comment but the scope creep happened fast.

Edit: Screw it my flights delayed and I’m dying of boredom.

Let’s take the minimum edit distance problem. You can find it here. https://www.geeksforgeeks.org/edit-distance-dp-5/

I’m going to start from front of string to give you a different look than answer I linked

Recursive cases include :

If m>=len(a)

If n >=len(b)

If(a[m]==b[n]) call(a,b,m+1,n+1)// same char

If(a[m]!=b[n]) 1+ min(call(a,b,m+1,n), call(a,b, m, n+1), call(a,b,m+1,n+1))

This last condition covers the deletion, insertion, and edit cases.

To change that to dp we see we’re incrementing m and n. That means we need go the other way to go bottom up.

We also have two things we’re keeping track of that are independent of each other, m and n.

That means a 2d vector to keep track of both, one will be down y axis and other will be x.

We see in the recursive case we depend on m+1 and n+1 for the current answer at each level. That means in bottoms up case we will depend on the other way(since were approaching it bottoms up).

That means if we have

abc

def

As a 2d array when we need to find what the val at e will be we need to do the min(vec[m-1][n-1],vec[m-1][n],vec[m][n-1]) +1

Or in orther words the min(a,b,d)+1

Notice this is THE SAME EXACT THING AS THE RECURSIVE CALL from the top down solution. This is all you have to do for each call. Convert the calls to memory accesses.

The answer will be at the very bottom right of the vector since it depends on things left, up or diagonally left of whichever subproblem we are at as I just showed.

So we now just need to turn it into 2 for loops and the code is literally an If conditional making sure they’re not equal(SAME AS RECURSIVE CALL) and if that’s the case we do the min call I wrote which equals the index we are currently at in the problem. Do this until we get to the bottom right and wala! You’ve converted.

Sorry, this is written on my phone as I sit like a prisoner in an airplane. If you need clarification let me know!
```