1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        # Time: O(n) -> single pass over the array
4        # Space: O(1) -> only two integer variables
5
6        # Both start at the first element so all-negative arrays work
7        # (an empty subarray is not allowed, so 0 is not a valid start).
8        current_sum = nums[0]  # best sum of a subarray ending at current index
9        max_sum = nums[0]      # best sum seen anywhere so far
10
11        for num in nums[1:]:
12            # Extend the previous subarray, or restart at `num`
13            # (restart wins when current_sum is negative).
14            current_sum = num if num > current_sum + num else current_sum +num
15
16            # Keep the best answer seen at any index.
17            max_sum = max_sum if max_sum > current_sum else current_sum
18
19
20        return max_sum