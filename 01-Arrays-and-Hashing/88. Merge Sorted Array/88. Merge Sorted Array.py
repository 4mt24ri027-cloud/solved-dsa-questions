class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        k = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m -= 1
            else:
                nums1[k] = nums2[n]
                n -= 1
            k -= 1

        while n >= 0:
            nums1[k] = nums2[n]
            n -= 1
            k -= 1
