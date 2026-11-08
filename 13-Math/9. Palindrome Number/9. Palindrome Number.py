1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        # Negative numbers can never be palindromes (the '-' sign breaks symmetry)
4        if x < 0:
5            return False
6
7        original = x       # keep a copy, since the loop consumes x
8        reversed_num = 0
9
10        while x > 0:
11            last_digit = x % 10                          # peel off the last digit
12            reversed_num = reversed_num * 10 + last_digit  # append it to the reversed number
13            x //= 10                                     # drop the last digit (integer division)
14
15        # A palindrome equals its own reversal
16        return reversed_num == original
17
18# Time:  O(d), where d = number of digits (about log10(x))
19# Space: O(1), only a few integer variables