1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        n=len(nums)
4        pre=0
5        curr=2
6        while curr<len(nums):
7            while curr<len(nums) and nums[curr-1]==nums[curr] and nums[curr-2]==nums[curr]:
8                nums.pop(curr)
9                pre+=1
10            curr+=1
11        while len(nums)<n:
12            nums.append(0)
13        return n-pre