class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # Move zeros to the end while preserving non-zero order.
        # Next position where a non-zero value should be placed
        write_index = 0

        for read_index in range(len(nums)):
            if nums[read_index] != 0:
                # Skip the swap when both pointers coincide (no zeros seen yet)
                if read_index != write_index:
                    nums[write_index], nums[read_index] = (
                        nums[read_index],
                        nums[write_index],
                    )
                write_index += 1
