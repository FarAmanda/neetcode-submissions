## Understand
# Given:
# nums1 = [x1,...,x2]
# nums2 = [y1,...,y2]
# m = number of VALID ELEMENTS in nums1
# n = number of ELEMENTS in nums2
#
#

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        placeHolder = nums2 + nums1[0:m]
        print(placeHolder)
        nums1[:] = placeHolder
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
        