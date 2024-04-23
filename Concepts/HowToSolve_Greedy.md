# Introduction

Problem solving approach of making the locally optimal choice at each stage with the goal of finding a global optimum. There is no backtracking like in dynamic programming because we will never reconsider our choices. 

**Pros:** Simple, easy to implement, runs fast

**Cons:** Very often they don’t produce a globally optimal solution

## Key Characteristics

1. **Local optimum** - At each step, the algorithm picks the option that seems best at that moment.
    1. E.g. Pick largest or smallest value in the current step
2. **Never look back** - No backtracking, once a choice is made it is never reconsidered.
3. **Optimization goal** - Greedy algorithms aim to find the overall or global optimum by focusing on local optimum

# When to Use

When facing a new problem, analyze if the problem has a straightforward greedy solution by looking for signs of greedy choice property and feasibility of local optimums. If the problem is more complex and involves revisiting decisions or has overlapping subproblems, then it's likely a candidate for dynamic programming.

1. **Optimal Substructure in a Combinatorial Way**: If the problem requires you to choose the best option at each step without needing to reconsider these choices later, it’s a good candidate for a greedy approach. Greedy problems often involve decision-making that doesn't require revisiting or adjusting past decisions.
2. **Feasibility of Local Optimum**: If a locally optimal choice leads directly to a global solution without the need for further verification or adaptation, the problem might be suitable for a greedy solution.
3. **Problem Simplification**: In many greedy problems, once a decision is made, the problem simplifies. For example, in the activity selection problem, once you select an activity, you discard all overlapping activities and solve the problem for the remaining part.
4. **Sorting or Ordering**: Many greedy algorithms start with sorting or rearranging elements (like costs, profits, deadlines, etc.) because an optimal solution involves processing elements in a specific sequence.
5. **Greedy Choice Property**: The problem allows a choice to be made from the current options that seems best and fits the problem constraints, without worrying about future consequences.

- Differences with Dynamic Programming
    1. **Overlapping Subproblems**: DP is suitable for problems where the same subproblems arise repeatedly, and solutions can be reused. This is a hallmark of DP problems—memoization or tabulation is used to store results of subproblems to avoid redundant work.
    2. **Optimal Substructure in a Sequential/Recursive Way**: A problem has optimal substructure suitable for DP if an optimal solution to the problem contains within it optimal solutions to subproblems. Unlike greedy, where the local choice is final, DP may require revisiting and revising these choices based on future computations.
    3. **Need for Revisiting Decisions**: If the problem requires reassessing earlier decisions as new information or calculations become available, it likely needs a DP approach. For instance, in the knapsack problem, decisions made about including an item may need reconsideration based on the total capacity and remaining items.
    4. **Decision Dependency**: The decision at each step might depend on various possible scenarios or states achieved from previous decisions, indicative of the need for dynamic programming.
    5. **Counting or Minimizing/Maximizing Exact Outcomes**: Problems that require counting the number of ways to achieve something, or precisely minimizing or maximizing certain criteria where the impact of each decision affects subsequent decisions, typically use DP.

# How to Approach

1. **Analyze the Problem**: Understand the problem and decide if a greedy strategy can be applied. A problem suitable for a greedy algorithm typically has "optimal substructure," meaning an optimal solution to the problem contains optimal solutions to its sub-problems.
2. **Choose a Criterion**: Determine what constitutes the "best" choice at each step. This could be the smallest, largest, highest value, lowest cost, etc., depending on the problem.
3. **Build a Solution**: Construct the solution step by step, choosing the best option at each step without reconsidering past decisions.
4. **Prove Correctness**: It’s crucial to argue why following the greedy criterion will result in an optimal solution. This often involves proving that making a locally optimal choice leads to a global optimum.
5. **Implement and Test**: Write the code and test it with different cases to ensure it handles all possible scenarios.

# Examples

## Not finding the global optimum

### Example 1: Find largest root leaves sum

We want to find the largest root leaves sum, so our local optimal choice for each step is to go to the nodes with largest value.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/6f444c62-5a75-4515-ad26-00381bdc8c3c/Untitled.png)

After selecting the most optimal choice which is the largest value node, we end up with a greedy answer: 3 + 7 + 11 = 21

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/b8424ee0-5db3-4ad4-9a49-bfbb8c015261/Untitled.png)

However, the most optimal choice is actually: 3 + 4 + 20 = 27

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/56ec8ded-70c5-46a5-b639-988a6638cc10/Untitled.png)

### Example 2: Dijkstra’s Algorithm

[Problem with greedy algorithms](https://www.notion.so/Problem-with-greedy-algorithms-c06c30cfe2504a1fb50cdc47f1820d25?pvs=21) 

# Common Template

1. **Problem Understanding and Analysis**:
    - Clearly understand the problem and the constraints.
    - Identify if the problem can be broken down into components where local optimal choices lead to a global optimal solution.
2. **Initialization**:
    - Define necessary variables to keep track of the current state (like current result, maximum/minimum, counters).
    - Optionally, sort the input if the problem involves comparing elements or requires a specific order for processing.
3. **Iteration over Input**:
    - Iterate over the sorted or original input based on problem requirements.
    - Make a greedy choice during each iteration, updating the state based on local optima.
4. **Greedy Choice**:
    - Apply the greedy decision rule that aligns with moving toward the desired outcome.
    - Update any auxiliary data structures or variables that monitor the progress or state of the solution.
5. **Post-Processing** (if needed):
    - Sometimes after iterating, you might need to adjust or finalize the result based on additional constraints or final checks.
6. **Return the Result**:
    - Output the final result which could be the accumulated value, a constructed array, or any other structure depending on the problem.

```python
def solve(input):
    # Step 1: Sort the input if necessary
    input.sort(key=lambda x: x[1])  # Example sort by second element

    # Step 2: Initialize necessary variables
    result = 0
    current_state = None

    # Step 3: Iterate through the sorted input
    for element in input:
        if should_take(element, current_state):
            # Step 4: Make the greedy choice
            result += element[0]  # Update result based on problem requirement
            current_state = update_state(current_state, element)

    # Step 5: Final adjustments (if necessary)
    final_result = finalize_result(result, input)

    # Step 6: Return the final result
    return final_result
```