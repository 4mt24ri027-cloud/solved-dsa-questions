1
2class Solution:
3    def longestCommonPrefix(self, strs: list[str]) -> str:
4
5        prefix = 
6
7        for i in range(len(strs[0])):
8
9            char = strs[0][i]
10
11            for word in strs[1:]:
12
13                if i >= len(word) or word[i] != char:
14                    return prefix
15
16            prefix += char
17
18        return prefix
19