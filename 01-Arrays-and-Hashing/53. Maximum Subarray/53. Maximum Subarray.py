class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Time: O(n) -> single pass over the array
        # Space: O(1) -> only two integer variables

        # Both start at the first element so all-negative arrays work
        # (an empty subarray is not allowed, so 0 is not a valid start).
        current_sum = nums[0]  # best sum of a subarray ending at current index
        max_sum = nums[0]  # best sum seen anywhere so far

        for num in nums[1:]:
            # Extend the previous subarray, or restart at `num`
            # (restart wins when current_sum is negative).
            if current_sum < 0:
                current_sum = num
            else:
                current_sum += num
            # Keep the best answer seen at any index.
            max_sum = max_sum if max_sum > current_sum else current_sum

        return max_sum
