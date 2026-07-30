class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store a dictionary
        # Key = difference
        # Value = index
        numDict = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in numDict:
                return [numDict[num],i]

            else:
                numDict[target - num] = i

        
