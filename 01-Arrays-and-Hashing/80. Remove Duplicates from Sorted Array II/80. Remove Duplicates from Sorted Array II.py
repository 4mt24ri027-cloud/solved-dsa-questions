1class Solution:
2    def removeDuplicates(self, nums: list[int]) -> int:
3        current_index = 0 
4        for num in nums:
5           if current_index < 2 or num != nums[current_index-2] :
6              nums[current_index] =  num
7              current_index += 1
8              
9              
10        return current_index
11        
12        
13        
14        
15        
16        
17        
18        
19        
20        
21        
22        
23        
24        
25        
26        
27        
28        
29        
30        
31        
32        
33        
34        
35        
36        
37        
38        
39        
40        
41        
42        
43        
44        
45        
46        
47        
48        
49        
50        
51        
52        
53        
54        
55        
56        
57        
58        
59        
60        
61        
62        
63        
64        
65        
66        
67        
68        
69        
70        
71        
72        
73        
74        
75        
76        
77        
78        
79        
80        
81        
82        
83        
84        