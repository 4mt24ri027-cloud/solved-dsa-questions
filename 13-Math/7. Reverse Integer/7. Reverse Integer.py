class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        sign = -1 if x < 0 else 1  # remember the sign
        x = abs(x)  # work with a non-negative number

        reversed_num = 0
        while x:
            last_digit = x % 10  # peel off the last digit
            reversed_num = reversed_num * 10 + last_digit  # append it
            x //= 10  # drop it from x

        reversed_num *= sign  # restore the sign

        # Out of 32-bit range -> return 0
        if INT_MIN <= reversed_num <= INT_MAX:
            return reversed_num
        return 0


# Time:  O(d), where d = number of digits in x (d <= 10 here, so effectively O(1))
# Space: O(1), only a few integer variables
