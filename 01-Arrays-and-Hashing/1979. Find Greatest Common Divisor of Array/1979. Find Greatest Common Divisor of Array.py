class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a, b = min(nums), max(nums)
        while b:
            # gcd(a, b) == gcd(b, a % b), so each step reduces the pair.
            a, b = b, a % b
        # The last nonzero remainder is the greatest common divisor.
        return a
