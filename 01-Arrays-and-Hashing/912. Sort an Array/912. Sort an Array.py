import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Merge sort

        # One reusable buffer for all merges -> O(n) extra space
        buffer = [0] * len(nums)

        def merge_sort(lo: int, hi: int) -> None:
            # Sorts nums[lo..hi] (inclusive) in place
            if lo >= hi:  # 0 or 1 element: already sorted
                return

            mid = (lo + hi) // 2
            merge_sort(lo, mid)  # sort left half
            merge_sort(mid + 1, hi)  # sort right half

            # Merge the two sorted halves into buffer
            left, right, write = lo, mid + 1, lo
            while left <= mid and right <= hi:
                if nums[left] <= nums[right]:  # <= keeps it stable
                    buffer[write] = nums[left]
                    left += 1
                else:
                    buffer[write] = nums[right]
                    right += 1
                write += 1

            # Only one of these two loops will actually run
            while left <= mid:  # leftovers from left half
                buffer[write] = nums[left]
                left += 1
                write += 1
            while right <= hi:  # leftovers from right half
                buffer[write] = nums[right]
                right += 1
                write += 1

            # Copy the merged result back into nums
            nums[lo : hi + 1] = buffer[lo : hi + 1]

        # Time:  O(n log n) -> log n levels, O(n) merge work per level
        # Space: O(n) buffer + O(log n) recursion

        # Quick sort
        def quick_sort(lo: int, hi: int) -> None:

            # Sorts nums[lo..hi] (inclusive) in place
            if lo >= hi:  # 0 or 1 element, or an empty range
                return

            pivot = nums[random.randint(lo, hi)]  # random pivot VALUE
            lt, i, gt = lo, lo, hi

            while i <= gt:
                if nums[i] < pivot:  # smaller: send to the left block
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:  # bigger: send to the right block
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1  # i stays: swapped-in value is unchecked
                else:  # equal: leave in the middle
                    i += 1

            # Now nums[lt..gt] all equal pivot and are in final position
            quick_sort(lo, lt - 1)  # smaller block
            quick_sort(gt + 1, hi)  # bigger block

        quick_sort(0, len(nums) - 1)
        return nums


# Time:  O(n log n) average, O(n^2) worst case (very unlikely with a random pivot)
# Space: O(log n) expected recursion stack, no extra buffer
