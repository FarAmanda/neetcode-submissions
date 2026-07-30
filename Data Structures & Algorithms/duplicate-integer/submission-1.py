class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        dicts = {}

        for x in nums:
            if x in dicts:
                return True
            else: 
                dicts[x] = 1

        return False
