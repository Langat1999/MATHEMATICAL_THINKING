#Memoization optimizes recursion by storing previous results. Here’s the Fibonacci sequence computed with a dynamic programming approach
#This approach reduces the exponential runtime of the naive recursive method to linear time by caching results, showcasing an effective use of dynamic programming
#Memoization optimizes recursion by storing previous results. Here’s the Fibonacci sequence computed with a dynamic programming approach
#This approach reduces the exponential runtime of the naive recursive method to linear time by caching results, showcasing an effective use of dynamic programming
def fibonacci_memo(n, memo=None):
    """Compute the nth Fibonacci number using memoization."""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)