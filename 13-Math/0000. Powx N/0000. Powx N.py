1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        # Time: O(log |n|) -- n is halved every iteration
4        # Space: O(1) -- only a few scalar variables
5        is_negative_power = n < 0
6        exponent = abs(n)          # safe in Python: ints never overflow
7        result = 1.0
8        base = x
9
10        # Walk through the binary digits of the exponent, lowest bit first
11        while exponent > 0:
12            if exponent % 2 == 1:  # current bit is 1: include this power of x
13                result *= base
14            base *= base           # x, x^2, x^4, x^8, ...
15            exponent //= 2         # move to the next bit
16
17        # Apply the reciprocal once, at the end, to keep rounding error small:
18        # x^(-n) == 1 / x^n
19        return 1 / result if is_negative_power else result