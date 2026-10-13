1class Solution:
2    def jump(self, nums: list[int]) -> int:
3        n= len(nums)
4        jumps = 0
5        farthest = 0
6        current_reach = 0 
7        for  i in range(n-1):
8            farthest = max(farthest,i+nums[i])
9            if i == current_reach:
10                jumps += 1
11                current_reach = farthest
12                if current_reach >= n-1 :
13                    break
14        return jumps
15