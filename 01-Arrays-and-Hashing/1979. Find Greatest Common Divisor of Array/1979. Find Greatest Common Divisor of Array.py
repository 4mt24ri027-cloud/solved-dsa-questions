class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a, b = min(nums), max(nums)
        while b:
            a, b = b, a % b
        return a
