from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Time: O(n) -- one pass over adjacent pairs
        # Space: O(1) -- three integer variables only
        increasing_run = 1  # length of strictly increasing run ending here
        decreasing_run = 1  # length of strictly decreasing run ending here
        longest = 1  # a single element is always a valid subarray

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                increasing_run += 1
                decreasing_run = 1  # an upward step kills any downward run
            elif nums[i] > nums[i + 1]:
                decreasing_run += 1
                increasing_run = 1  # a downward step kills any upward run
            else:
                increasing_run = 1  # equal values break both runs
                decreasing_run = 1

            longest = max(longest, increasing_run, decreasing_run)

        return longest
