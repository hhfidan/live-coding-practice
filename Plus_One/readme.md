# Plus One Problem

## Problem Description:

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return _the resulting array of digits_.

### Example 1:

- **Input:** digits = [1,2,3]
- **Output:** [1,2,4]
- **Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

### Example 2:
- **Input:** digits = [4,3,2,1]
- **Output:** [4,3,2,2]
- **Explanation:** The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

### Example 3:

- **Input:** digits = [9]
- **Output:** [1,0]
- **Explanation:** The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

### Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- `digits` does not contain any leading `0`'s.

## Problem Understanding:

For problems involving addition like this, I usually start by **reversing the number**. This is because addition is performed from right to left, but when coding, it's often easier to handle it from left to right.

Looking at the first two examples, the solution is straightforward:
  - Treat the array as a number(integer),
  - Reverse it,
  - Add `1` to the first digit,
  - Reverse it back to get the final result.

However, the third example introduces a **carry-over** situation when the sum exceeds `9`.
  - In this case, we need to **check for carry-over** and handle it properly in the code.
  - This follows the **besic addition logic** we learned in elementary school-when a digit reaches `10`, we carry over `1` to the next position.

Thinking simply often leads to faster solutions 😊

## Plus One Problem - Case Breakdown

Let's try with `[1,5,6,9]`

- reverse it -> `9651`
- Add the carry to firs digit -> `9 + 1 = 10`
- Check for carry-over ->Since 10 creates a carry `(10 == 10)`, we continue propagating it.
- If it is carry over we need to continue carry over when we come end of the integer we can just add the 1 to end of integer
- Then dont forget the reverse result, thats it!

## Time and Space Complexity

1. Reversing the list (digits.reverse()) -> O(n)
2. Iterating through the list once -> O(n)
3. Appending a carry if needed -> O(1)
4. Reversing the list again -> O(n)

Since the dominant term is **O(n) + O (n) + O(n) = O(n)**, the overall time complexity is **O(n)**.

- The solution modifies the input list in place, using only a constant extra space **(O(1))**, except in the worst case, where we append one extra digit.
- In the worst case, the space complexity is **O(n)** if we consider the additional digit.
- As a result, the space complexity is **O(1)** in most cases, but **O(n)** in the worst case when extra space is needed.
