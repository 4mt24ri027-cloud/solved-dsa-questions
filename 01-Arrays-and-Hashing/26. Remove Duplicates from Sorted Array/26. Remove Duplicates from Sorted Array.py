class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in nums:
            if i != nums[k - 1]:
                nums[k] = i
                k += 1
        return k
