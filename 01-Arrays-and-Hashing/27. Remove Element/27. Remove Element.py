class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write_index = 0
        for value in nums:
            if value != val:
                nums[write_index] = value
                write_index += 1
        return write_index
