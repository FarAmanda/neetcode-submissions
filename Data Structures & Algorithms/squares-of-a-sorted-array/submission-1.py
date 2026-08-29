class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)
        ptr = len(nums) - 1

        while ptr >= 0:
            if (nums[l] * nums[l] >= nums[r] * nums[r]):
                res[ptr] = nums[l] * nums[l]
                l+= 1
            else:
                res[ptr] = nums[r] * nums[r]
                r-= 1

            ptr -= 1

        return res


# [-4,-1,0,3,10]