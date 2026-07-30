class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if num not in sumDict:
                sumDict[diff] = i

            else:
                return [sumDict[num], i] 