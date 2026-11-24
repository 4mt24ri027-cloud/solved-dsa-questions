class Solution:
    def reverseString(self, s: list[str]) -> None:
        # ---------- Approach 1: Two pointers (optimal) ----------
        # Time: O(n) - about n/2 swaps, each element visited once
        # Space: O(1) - only two index variables, list is modified in place
        left, right = 0, len(s) - 1

        while left < right:
            # Tuple assignment swaps without a temp variable
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # ---------- Approach 2: Slice assignment ----------
        # s[:] = s[::-1]
        #
        # Time: O(n) - building the reversed copy and copying it back are both linear
        # Space: O(n) - s[::-1] creates a temporary reversed list of n elements
        #
        # s[:] = ... changes the contents of the caller's list, so it is valid
        # in place for LeetCode. Plain `s = s[::-1]` would NOT work, because it
        # only rebinds the local name s and leaves the caller's list unchanged.
