1class Solution(object):
2    def twoSum(self, nums, target):
3        num_map = {}
4        for i, num in enumerate(nums):
5            complement = target - num
6            if complement in num_map:
7                return [num_map[complement], i]
8            num_map[num] = i