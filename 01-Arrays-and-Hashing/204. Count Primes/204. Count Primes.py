1class Solution:
2    def countPrimes(self, n: int) -> int:
3        # Primes must be strictly less than n, so n < 3 has no primes except
4        # possibly 2, which is excluded when n = 2.
5        if n < 3:
6            return 0
7
8        # is_prime[k] is True while k is still a prime candidate
9        is_prime = [True] * n
10        is_prime[0] = is_prime[1] = False
11
12        i = 2
13        # Only need i up to sqrt(n): any composite < n has a prime factor <= sqrt(n)
14        while i * i < n:
15            if is_prime[i]:
16                # Start at i*i: smaller multiples were already crossed out
17                # by smaller primes. Slice assignment is much faster than a loop.
18                is_prime[i * i : n : i] = [False] * len(range(i * i, n, i))
19            i += 1
20
21        # True entries are the primes
22        return sum(is_prime)
23
24# Time:  O(n log log n)  - each prime p crosses out ~n/p entries
25# Space: O(n)            - the boolean sieve array