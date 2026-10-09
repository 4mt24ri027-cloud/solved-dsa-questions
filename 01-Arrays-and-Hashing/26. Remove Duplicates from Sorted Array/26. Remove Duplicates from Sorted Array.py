1class Solution:
2    def removeDuplicates(self, nums: list[int]) -> int:
3        k = 1
4        for i in nums:
5            if i != nums[k-1]:
6               nums[k] = i
7               k += 1
8        return k
9