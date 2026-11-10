1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        # One reusable buffer for all merges -> O(n) extra space
4        buffer = [0] * len(nums)
5
6        def merge_sort(lo: int, hi: int) -> None:
7            # Sorts nums[lo..hi] (inclusive) in place
8            if lo >= hi:                 # 0 or 1 element: already sorted
9                return
10
11            mid = (lo + hi) // 2
12            merge_sort(lo, mid)          # sort left half
13            merge_sort(mid + 1, hi)      # sort right half
14
15            # Merge the two sorted halves into buffer
16            left, right, write = lo, mid + 1, lo
17            while left <= mid and right <= hi:
18                if nums[left] <= nums[right]:    # <= keeps it stable
19                    buffer[write] = nums[left]
20                    left += 1
21                else:
22                    buffer[write] = nums[right]
23                    right += 1
24                write += 1
25
26            # Only one of these two loops will actually run
27            while left <= mid:           # leftovers from left half
28                buffer[write] = nums[left]
29                left += 1
30                write += 1
31            while right <= hi:           # leftovers from right half
32                buffer[write] = nums[right]
33                right += 1
34                write += 1
35
36            # Copy the merged result back into nums
37            nums[lo:hi + 1] = buffer[lo:hi + 1]
38
39        merge_sort(0, len(nums) - 1)
40        return nums
41
42# Time:  O(n log n) -> log n levels, O(n) merge work per level
43# Space: O(n) buffer + O(log n) recursion stack