class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        ptr = 0
        l, r = 0, len(nums) -1
        

        while l <= r:

            if nums[ptr] % 2 == 0:
                res[l] = nums[ptr]
                ptr+= 1
                l+= 1
            else:
                res[r] = nums[ptr]
                ptr += 1
                r -= 1
        return res
