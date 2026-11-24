class Solution:
    def countPrimes(self, n: int) -> int:
        # Primes must be strictly less than n, so n < 3 has no primes except
        # possibly 2, which is excluded when n = 2.
        if n < 3:
            return 0

        # is_prime[k] is True while k is still a prime candidate
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        i = 2
        # Only need i up to sqrt(n): any composite < n has a prime factor <= sqrt(n)
        while i * i < n:
            if is_prime[i]:
                # Start at i*i: smaller multiples were already crossed out
                # by smaller primes. Slice assignment is much faster than a loop.
                is_prime[i * i : n : i] = [False] * len(range(i * i, n, i))
            i += 1

        # True entries are the primes
        return sum(is_prime)


# Time:  O(n log log n)  - each prime p crosses out ~n/p entries
# Space: O(n)            - the boolean sieve array
