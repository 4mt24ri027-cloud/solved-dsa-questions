class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        pre = 0
        curr = 2
        while curr < len(nums):
            while (
                curr < len(nums)
                and nums[curr - 1] == nums[curr]
                and nums[curr - 2] == nums[curr]
            ):
                nums.pop(curr)
                pre += 1
            curr += 1
        while len(nums) < n:
            nums.append(0)
        return n - pre
