#A classic example is proving the formula for the sum of the first n natural numbers. The code below uses recursion (an approach you’d prove correct via induction) to compute the sum and then compares it with the closed form.
def sum_n(n):
    """Return the sum of the first n natural numbers using recursion."""
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)