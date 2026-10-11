1class Solution:
2    def canJump(self, nums: list[int]) -> bool:
3        furthest = 0
4        for i in range(len(nums)):
5            if i > furthest:
6                return False
7            furthest = max(furthest,i+nums[i])
8            if furthest >= len(nums) - 1:
9               return True 
10
11