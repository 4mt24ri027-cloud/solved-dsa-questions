class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # Modify nums in place.
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
