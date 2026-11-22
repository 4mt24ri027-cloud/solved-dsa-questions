1class Solution:
2    def hIndex(self, citations: list[int]) -> int:
3        # Time: O(log n) - the search range halves every iteration
4        # Space: O(1) - only a few integer variables
5        n = len(citations)
6        left, right = 0, n - 1
7
8        while left <= right:
9            mid = (left + right) // 2
10            papers_from_mid = n - mid  # candidate h-index at this position
11
12            if citations[mid] >= papers_from_mid:
13                # mid is valid; a smaller index might be valid too
14                right = mid - 1
15            else:
16                # mid is too weak; the answer lies to the right
17                left = mid + 1
18
19        # left = first valid index (n if none), so h = papers from there on
20        return n - left