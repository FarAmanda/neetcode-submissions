class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        index = 0


        for i in nums:
            difference = target - i
            if difference not in myDict:
                myDict[i] = index
            else:
                return [myDict[difference], index]

            index += 1
