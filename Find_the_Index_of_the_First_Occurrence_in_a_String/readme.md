# Find the Index of the First Occurrence in a String Problem

## Problem Description:

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

### Example 1:
- **Input:** haystack = "sadbutsad", needle = "sad"
- **Output:** 0
- **Explanation:** "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.
- 
### Example 2:
- **Input:** haystack = "leetcode", needle = "leeto"
- **Output:** -1
- **Explanation:** "leeto" did not occur in "leetcode", so we return -1.
- 
### Constraints:
- `1 <= haystack.length, needle.length <= 104`
- haystack and needle consist of only lowercase English characters.

## Problem Understanding:

### ⭐️ Solution 1 ⭐️

#### Approach:

- Iterate through each character of the haystack.

- For each character, check if the substring starting at that position matches the needle character by character.

- If a match is found, return the starting index; otherwise, continue until the end of the haystack.

#### Pros:

- Simple logic that is easy to understand.

- Works well for short strings.

#### Cons:

- Less readable due to nested loops.

- Inefficient for large strings.

### Time Complexity:

- Worst-case: O(N * M), where N is the length of the haystack and M is the length of the needle.

- This occurs when each character of the haystack is checked against every character of the needle.

### Space Complexity:

- O(1) since no additional space is used except a few variables.

### ⭐️ Solution 2 ⭐️

#### Approach:

- Use slicing to extract substrings from the haystack.

- Compare each substring of the same length as the needle with the needle itself.

- If a match is found, return the starting index.

#### Pros:

- Improved readability and cleaner code.

- Easier to maintain and debug.

#### Cons:

- Slight overhead due to creating substrings.

### Time Complexity:

- Worst-case: O(N * M), where N is the length of the haystack and M is the length of the needle.

- Similar to Solution 1, but the slicing operation can introduce additional overhead.

### Space Complexity:

- O(M) since each slicing operation creates a substring of length M.

### Conclusion
Both solutions have the same time complexity. However, Solution 2 is more readable and maintainable due to its clean slicing approach. 
The slight space overhead is usually acceptable for most applications. Therefore, Solution 2 is recommended for real-world usage, unless memory constraints are critical. 
So i choose the solution 2. 

