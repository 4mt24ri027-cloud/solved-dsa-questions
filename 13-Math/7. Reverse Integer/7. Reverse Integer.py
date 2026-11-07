1class Solution:
2    def reverse(self, x: int) -> int:
3        INT_MIN, INT_MAX = -2**31, 2**31 - 1
4
5        sign = -1 if x < 0 else 1   # remember the sign
6        x = abs(x)                  # work with a non-negative number
7
8        reversed_num = 0
9        while x:
10            last_digit = x % 10                          # peel off the last digit
11            reversed_num = reversed_num * 10 + last_digit  # append it
12            x //= 10                                     # drop it from x
13
14        reversed_num *= sign        # restore the sign
15
16        # Out of 32-bit range -> return 0
17        if INT_MIN <= reversed_num <= INT_MAX:
18            return reversed_num
19        return 0
20
21# Time:  O(d), where d = number of digits in x (d <= 10 here, so effectively O(1))
22# Space: O(1), only a few integer variables