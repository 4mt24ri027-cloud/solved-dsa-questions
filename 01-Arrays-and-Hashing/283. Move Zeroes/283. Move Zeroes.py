1class Solution:
2    def moveZeroes(self, nums: list[int]) -> None:
3        
4        Modify nums in-place so all zeros move to the end,
5        keeping the relative order of non-zero elements.
6
7        Time:  O(n) - single pass over the array
8        Space: O(1) - only a couple of integer variables
9        
10        # Next position where a non-zero value should be placed
11        write_index = 0
12
13        for read_index in range(len(nums)):
14            if nums[read_index] != 0:
15                # Skip the swap when both pointers coincide (no zeros seen yet)
16                if read_index != write_index:
17                    nums[write_index], nums[read_index] = nums[read_index], nums[write_index]
18                write_index += 1