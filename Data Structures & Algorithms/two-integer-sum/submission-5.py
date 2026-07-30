class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if nums[i] in res:
                return [res[nums[i]], i]

            else: 
                res[difference] = i

        