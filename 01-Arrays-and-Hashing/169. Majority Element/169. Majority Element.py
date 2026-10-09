1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        candidate = None
4        count = 0 
5        for num in nums:
6            if count == 0:
7                candidate = num 
8            count += 1 if num == candidate else -1
9
10        return candidate 