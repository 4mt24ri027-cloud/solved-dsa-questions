class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)
        for c in citations:
            bucket[min(c, n)] += 1
        total = 0
        for h in range(n, -1, -1):
            total += bucket[h]
            if total >= h:
                return h
        return 0
