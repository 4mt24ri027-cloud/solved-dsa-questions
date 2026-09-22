1class Solution:
2    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
3        
4        Do not return anything, modify nums1 in-place instead.
5        
6        k = m+n-1
7        m = m -1
8        n = n -1 
9        while(m >= 0 and n >= 0):
10            if nums1[m] > nums2[n]:
11                nums1[k] = nums1[m]
12                m-= 1
13            else:
14                nums1[k] = nums2[n]
15                n-= 1
16            k-= 1
17
18        while n >= 0 :
19            nums1[k] = nums2[n]
20            n -= 1
21            k -= 1
22            