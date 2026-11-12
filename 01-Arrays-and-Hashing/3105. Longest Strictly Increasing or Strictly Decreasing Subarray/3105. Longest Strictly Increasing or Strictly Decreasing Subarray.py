1from typing import List
2
3
4class Solution:
5    def longestMonotonicSubarray(self, nums: List[int]) -> int:
6        # Time: O(n) -- one pass over adjacent pairs
7        # Space: O(1) -- three integer variables only
8        increasing_run = 1   # length of strictly increasing run ending here
9        decreasing_run = 1   # length of strictly decreasing run ending here
10        longest = 1          # a single element is always a valid subarray
11
12        for i in range(len(nums) - 1):
13            if nums[i] < nums[i + 1]:
14                increasing_run += 1
15                decreasing_run = 1       # an upward step kills any downward run
16            elif nums[i] > nums[i + 1]:
17                decreasing_run += 1
18                increasing_run = 1       # a downward step kills any upward run
19            else:
20                increasing_run = 1       # equal values break both runs
21                decreasing_run = 1
22
23            longest = max(longest, increasing_run, decreasing_run)
24
25        return longest