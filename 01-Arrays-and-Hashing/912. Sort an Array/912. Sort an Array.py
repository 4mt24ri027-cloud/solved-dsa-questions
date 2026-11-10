1class Solution:
2    def sortArray(self, nums: list[int]) -> list[int]:
3         
4        temp = [0] * len(nums)
5
6        def merge_sort(lo,hi):
7
8            if lo >= hi :
9                return 
10            mid = (lo + hi) // 2 
11            merge_sort(lo ,mid)
12            merge_sort(mid+1,hi)
13
14            left,right,write = lo,mid+1,lo
15            while left <= mid and right <= hi:
16                if nums[left] <= nums[right]:
17                    temp[write] = nums[left]
18                    left += 1
19                
20                else:
21                    temp[write] = nums[right]
22                    right += 1
23                
24                write += 1
25
26            while left <= mid:
27                    temp[write] = nums[left]
28                    left += 1 
29                    write += 1
30
31            while right <= hi :
32                    temp[write] = nums[right]
33                    right += 1
34                    write += 1
35
36            nums[lo:hi + 1] = temp[lo : hi + 1]
37
38        merge_sort(0,len(nums) - 1)
39        return nums