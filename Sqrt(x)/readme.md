# Sqrt(x) Problem

## Problem Description:

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

### Example 1:
- **Input:** x = 4
- **Output:** 2
- **Explanation:** The square root of 4 is 2, so we return 2.

### Example 2:
- **Input:** x = 8
- **Output:** 2
- **Explanation:** The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
### Constraints:
- 0 <= x <= 231 - 1

## Problem Understanding:

My approach to problems starts with thinking like a human rather than immediately applying coding logic. 
I ask myself how I would solve the problem without any programming knowledge. This helps me develop a simpler technique. 
Sometimes, thinking in a programming language can make things more complicated.
Initially, I may come up with a complex solution, but at least I can optimize it later. However, if I dive straight into coding and things get too complicated, I might not even reach a solution.
For this problem, I approached it by identifying the range in which the square root of a number (e.g., 48) falls. This method helped me narrow down the possible answers before implementing the solution in code.

## Time and Space Complexity

The time complexity of the initial solution, where you're incrementing i one by one until i * i exceeds x, is indeed O(√x). This is because you're essentially searching for the square root by trying each integer value up to the square root of x.
The space complexity is O(1) since you're only using a constant amount of extra space (the variable i).
However, the time complexity can be improved by using a more efficient method ... (coming soon)

🌟Thinking in this way is also useful for live coding practice. Because you're often asked how else it could be written. 
The first solution is not always the most optimized, and we cannot always know that upfront. That's why we train ourselves to think in this way.

