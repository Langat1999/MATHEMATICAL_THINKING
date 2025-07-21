#The Sieve of Eratosthenes is an efficient method for finding all prime numbers up to a given limit.
#Explanation: This code populates a boolean sieve to mark non-prime numbers efficiently, illustrating basic yet powerful number theory concepts used in areas like cryptography and hashing
def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n (inclusive)."""
    if n < 2:
        return []

    # Initialize sieve: True means "assume prime"
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    # Eliminate non-primes
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Collect all prime indices
    return [i for i, is_prime in enumerate(sieve) if is_prime]

# Example usage
primes_up_to_50 = sieve_of_eratosthenes(50)
print("Primes up to 50:", primes_up_to_50)