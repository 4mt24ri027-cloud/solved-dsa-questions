1class Solution:
2    def reverseString(self, s: list[str]) -> None:
3        # ---------- Approach 1: Two pointers (optimal) ----------
4        # Time: O(n) - about n/2 swaps, each element visited once
5        # Space: O(1) - only two index variables, list is modified in place
6        left, right = 0, len(s) - 1
7
8        while left < right:
9            # Tuple assignment swaps without a temp variable
10            s[left], s[right] = s[right], s[left]
11            left += 1
12            right -= 1
13
14        # ---------- Approach 2: Slice assignment ----------
15        # s[:] = s[::-1]
16        #
17        # Time: O(n) - building the reversed copy and copying it back are both linear
18        # Space: O(n) - s[::-1] creates a temporary reversed list of n elements
19        #
20        # s[:] = ... changes the contents of the caller's list, so it is valid
21        # in place for LeetCode. Plain `s = s[::-1]` would NOT work, because it
22        # only rebinds the local name s and leaves the caller's list unchanged.