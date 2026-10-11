1class Solution:
2    def rotate(self, nums: list[int], k: int) -> None:
3        
4        Do not return anything, modify nums in-place instead.
5        
6        n = len(nums)
7        k %= n 
8
9        def reverse(left,right):
10            while left < right:
11                nums[left],nums[right] = nums[right],nums[left]
12                right -= 1
13                left += 1
14      
15        reverse(0,n-1)
16        reverse(0,k-1)
17        reverse(k,n-1)