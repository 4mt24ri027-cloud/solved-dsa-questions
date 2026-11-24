class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers can never be palindromes (the '-' sign breaks symmetry)
        if x < 0:
            return False

        original = x  # keep a copy, since the loop consumes x
        reversed_num = 0

        while x > 0:
            last_digit = x % 10  # peel off the last digit
            reversed_num = (
                reversed_num * 10 + last_digit
            )  # append it to the reversed number
            x //= 10  # drop the last digit (integer division)

        # A palindrome equals its own reversal
        return reversed_num == original


# Time:  O(d), where d = number of digits (about log10(x))
# Space: O(1), only a few integer variables
