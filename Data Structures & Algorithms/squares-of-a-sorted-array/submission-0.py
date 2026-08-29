class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, 0

        while r < len(nums):
            nums[r] *= nums[r]
            r+= 1

        return sorted(nums)