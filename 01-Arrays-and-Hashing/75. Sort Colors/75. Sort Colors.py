1class Solution:
2    def sortColors(self, nums: list[int]) -> None:
3        # Time:  O(n) - every iteration either moves i forward or moves high
4        #        backward, so the unchecked region [i..high] shrinks each step
5        # Space: O(1) - only three index variables, sorting happens in-place
6        
7        # low  -> next slot for a 0   (everything before it is 0)
8        # i    -> element being inspected
9        # high -> next slot for a 2   (everything after it is 2)
10        low, i, high = 0, 0, len(nums) - 1
11
12        # <= (not <) because nums[high] is still unchecked when i == high
13        while i <= high:
14            if nums[i] == 0:
15                nums[i], nums[low] = nums[low], nums[i]
16                low += 1
17                # Safe to advance i: the value that came from `low` was
18                # already inspected (it's a 1, or it's i itself)
19                i += 1
20            elif nums[i] == 1:
21                # 1s belong in the middle, so leaving it here is correct
22                i += 1
23            else:
24                nums[i], nums[high] = nums[high], nums[i]
25                high -= 1
26                # Do NOT advance i: the value swapped in from `high` has
27                # never been checked and could be 0, 1, or 2