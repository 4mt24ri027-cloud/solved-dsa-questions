1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        freq = {}
4        for i in nums:
5            if i in freq:
6                freq[i] +=1
7            else:
8                freq[i] = 1
9
10        max = 0 
11        for num,count in freq.items():
12           if  max < count:
13                max = count 
14                max_num = num 
15
16        return max_num