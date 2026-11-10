1
2class Solution:
3    import random 
4    
5    def sortArray(self, nums: List[int]) -> List[int]:
6        # Merge sort
7
8        # One reusable buffer for all merges -> O(n) extra space
9        buffer = [0] * len(nums)
10
11        def merge_sort(lo: int, hi: int) -> None:
12            # Sorts nums[lo..hi] (inclusive) in place
13            if lo >= hi:                 # 0 or 1 element: already sorted
14                return
15
16            mid = (lo + hi) // 2
17            merge_sort(lo, mid)          # sort left half
18            merge_sort(mid + 1, hi)      # sort right half
19
20            # Merge the two sorted halves into buffer
21            left, right, write = lo, mid + 1, lo
22            while left <= mid and right <= hi:
23                if nums[left] <= nums[right]:    # <= keeps it stable
24                    buffer[write] = nums[left]
25                    left += 1
26                else:
27                    buffer[write] = nums[right]
28                    right += 1
29                write += 1
30
31            # Only one of these two loops will actually run
32            while left <= mid:           # leftovers from left half
33                buffer[write] = nums[left]
34                left += 1
35                write += 1
36            while right <= hi:           # leftovers from right half
37                buffer[write] = nums[right]
38                right += 1
39                write += 1
40
41            # Copy the merged result back into nums
42            nums[lo:hi + 1] = buffer[lo:hi + 1]
43
44        
45
46# Time:  O(n log n) -> log n levels, O(n) merge work per level
47# Space: O(n) buffer + O(log n) recursion   
48
49
50        # Quick sort
51        def quick_sort(lo: int, hi: int) -> None:
52            
53            # Sorts nums[lo..hi] (inclusive) in place
54            if lo >= hi:                      # 0 or 1 element, or an empty range
55                return
56
57            pivot = nums[random.randint(lo, hi)]   # random pivot VALUE
58            lt, i, gt = lo, lo, hi
59
60            while i <= gt:
61                if nums[i] < pivot:           # smaller: send to the left block
62                    nums[lt], nums[i] = nums[i], nums[lt]
63                    lt += 1
64                    i += 1
65                elif nums[i] > pivot:         # bigger: send to the right block
66                    nums[i], nums[gt] = nums[gt], nums[i]
67                    gt -= 1                   # i stays: swapped-in value is unchecked
68                else:                         # equal: leave in the middle
69                    i += 1
70
71            # Now nums[lt..gt] all equal pivot and are in final position
72            quick_sort(lo, lt - 1)            # smaller block
73            quick_sort(gt + 1, hi)            # bigger block
74
75        quick_sort(0, len(nums) - 1)
76        return nums
77
78# Time:  O(n log n) average, O(n^2) worst case (very unlikely with a random pivot)
79# Space: O(log n) expected recursion stack, no extra buffer