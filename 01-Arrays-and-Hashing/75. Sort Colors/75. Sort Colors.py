class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # Time:  O(n) - every iteration either moves i forward or moves high
        #        backward, so the unchecked region [i..high] shrinks each step
        # Space: O(1) - only three index variables, sorting happens in-place

        # low  -> next slot for a 0   (everything before it is 0)
        # i    -> element being inspected
        # high -> next slot for a 2   (everything after it is 2)
        low, i, high = 0, 0, len(nums) - 1

        # <= (not <) because nums[high] is still unchecked when i == high
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
                # Safe to advance i: the value that came from `low` was
                # already inspected (it's a 1, or it's i itself)
                i += 1
            elif nums[i] == 1:
                # 1s belong in the middle, so leaving it here is correct
                i += 1
            else:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
                # Do NOT advance i: the value swapped in from `high` has
                # never been checked and could be 0, 1, or 2
