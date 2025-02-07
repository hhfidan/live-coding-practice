# Climbing Stairs Problem

## Problem Description:

You are climbing a staircase. It takes `n` steps to reach the top. 

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Example 1:
- **Input:** n = 2
- **Output:** 2
- **Explanation:** There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

### Example 2:
- **Input:** n = 3
- **Output:** 3
- **Explanation:** There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

### Constraints:
- 1 <= n <= 45

## Problem Understanding:

In problems like the Climbing Stairs problem, I begin by creating a few test cases to identify the pattern and relationship between the steps.
I often use paper and pencil for this, especially for small numbers (e.g., N=6), as it helps to visualize the problem.
Although understanding the problem may seem like a small task, it's important not to rush this phase, as a significant portion of the problem-solving process is spent here. 
Therefore, I recommend taking the time needed to fully understand the problem before proceeding.

## Climbing Stairs Problem - Case Breakdown

The Climbing Stairs problem can be solved by recognizing a pattern, as shown in the following cases:

- N=0 → 0  
- N=1 → 1  
- N=2 → 2  
- N=3 → 3  
- N=4 → 5  
- N=5 → 8  
- N=6 → 13  

At this point, I realized that the pattern was familiar—it’s based on the Fibonacci sequence. I initially attempted to solve the problem using the Fibonacci logic. However, this resulted in high time complexity (exponential), as we know Fibonacci has such a time complexity.

Given this, I shifted to an alternative solution with lower time complexity. A simpler way to think about the problem is that the result for `n` is the sum of the previous two values. This insight was the easiest part to implement in the code.

## Time and Space Complexity

The solution implemented in `live-coding-practice/Climbing_Stairs/Climbing_Stairs.py` has a time complexity of **O(n)**. This is due to the use of a single `for` loop within the code, which iterates through the steps.

The space complexity is **O(1)** because the amount of space used by the solution remains constant. Only a fixed amount of extra space is required, regardless of the input size.
