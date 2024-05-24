# Assume that you're climbing a staircase. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

"""
The mathematical formula behind this problem can be derived from the concept of Fibonacci numbers.

Let f(n) represent the number of distinct ways to climb n stairs.

Now, let's consider the last step:

    If the last step is taken as a single step, then there are f(n−1) ways to climb the remaining n−1 stairs.
    If the last step is taken as a double step, then there are f(n−2) ways to climb the remaining n−2 stairs.

Therefore, the total number of distinct ways to climb n stairs is the sum of the distinct ways to climb n−1 stairs
and the distinct ways to climb n−2 stairs.

This can be represented by the recurrence relation:

f(n)=f(n−1)+f(n−2)

with base cases:

f(1)=1
f(2)=2

This recurrence relation is essentially the same as the Fibonacci sequence, where each term is 
the sum of the two preceding terms. Hence, the number of distinct ways to climb n stairs follows the Fibonacci sequence.
"""

class Solution:

    @staticmethod
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
    

def test_solution():
    return Solution.climbStairs(3) == 3 and Solution.climbStairs(4) == 5 and Solution.climbStairs(5) == 8

print(test_solution())


