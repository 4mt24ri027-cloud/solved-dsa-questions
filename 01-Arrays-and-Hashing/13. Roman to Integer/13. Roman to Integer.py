1
2class Solution:
3    def romanToInt(self, s: str) -> int:
4        # Mapping of Roman numerals to their integer values
5        roman_to_num = {
6            'I': 1,
7            'V': 5,
8            'X': 10,
9            'L': 50,
10            'C': 100,
11            'D': 500,
12            'M': 1000
13        }
14
15        prev_value = 0
16        total = 0
17
18        # Traverse the Roman numeral string from right to left
19        for char in reversed(s):
20            curr_value = roman_to_num[char]
21
22            # Subtract if the current value is smaller than the previous value
23            # Otherwise, add it to the total
24            if curr_value < prev_value:
25                total -= curr_value
26            else:
27                total += curr_value
28
29            # Update the previous value for the next iteration
30            prev_value = curr_value
31
32        return total
33
34
35# Time Complexity: O(n)
36# - We traverse the string exactly once.
37
38# Space Complexity: O(1)
39# - The dictionary contains only 7 fixed Roman numeral mappings.
40# - Only a constant amount of extra space is used.
41