class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Time: O(log n) - the search range halves every iteration
        # Space: O(1) - only a few integer variables
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            papers_from_mid = n - mid  # candidate h-index at this position

            if citations[mid] >= papers_from_mid:
                # mid is valid; a smaller index might be valid too
                right = mid - 1
            else:
                # mid is too weak; the answer lies to the right
                left = mid + 1

        # left = first valid index (n if none), so h = papers from there on
        return n - left
