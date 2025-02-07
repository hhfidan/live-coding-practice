class Solution(object):
    def climbStairs(self, n):
        """
        Given a number n, return the number of distinct ways to climb to the top of a staircase with n steps.
        
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev1 = 1  # Base case: the number of ways to reach the first step
        prev2 = 2  # Base case: the number of ways to reach the second step
        current = 0

        # Start from step 3 and calculate the number of ways to reach each subsequent step
        for i in range(3, n + 1):
            current = prev1 + prev2  # The number of ways to reach the current step is the sum of the previous two
            prev1 = prev2  # Update prev1 to be the previous step
            prev2 = current  # Update prev2 to be the current step

        return current
