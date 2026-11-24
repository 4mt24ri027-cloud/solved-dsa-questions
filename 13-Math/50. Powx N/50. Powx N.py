class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Time: O(log |n|) -- n is halved every iteration
        # Space: O(1) -- only a few scalar variables
        is_negative_power = n < 0
        exponent = abs(n)  # safe in Python: ints never overflow
        result = 1.0
        base = x

        # Walk through the binary digits of the exponent, lowest bit first
        while exponent > 0:
            if exponent % 2 == 1:  # current bit is 1: include this power of x
                result *= base
            base *= base  # x, x^2, x^4, x^8, ...
            exponent //= 2  # move to the next bit

        # Apply the reciprocal once, at the end, to keep rounding error small:
        # x^(-n) == 1 / x^n
        return 1 / result if is_negative_power else result
