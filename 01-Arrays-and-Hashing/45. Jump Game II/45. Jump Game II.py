class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        farthest = 0
        current_reach = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_reach:
                jumps += 1
                current_reach = farthest
                if current_reach >= n - 1:
                    break
        return jumps
