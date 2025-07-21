#A classic recursive example is the Fibonacci sequence, which is defined by a recurrence relation.
#This implementation directly models the recurrence F(n) = F(n-1) + F(n-2), though its exponential time complexity also motivates the need for optimization (see dynamic programming example below).
def fibonacci_recursive(n):
    """Compute the nth Fibonacci number using simple recursion."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Display the first 10 Fibonacci numbers
print("Fibonacci numbers (recursive):")
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")