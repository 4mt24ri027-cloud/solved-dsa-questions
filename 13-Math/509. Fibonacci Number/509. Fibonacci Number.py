1class Solution:
2    def fib(self, n: int) -> int:
3        # Time: O(n) - one pass from 2 to n
4        # Space: O(1) - only two integers are stored
5
6        # Base cases: F(0) = 0, F(1) = 1
7        if n < 2:
8            return n
9
10        # prev = F(i-2), curr = F(i-1) at the start of each iteration
11        prev, curr = 0, 1
12
13        for _ in range(2, n + 1):
14            # Tuple assignment evaluates the right side first,
15            # so no temporary variable is needed to shift the window
16            prev, curr = curr, prev + curr
17
18        # After the last iteration, curr holds F(n)
19        return curr