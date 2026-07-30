class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl = {}
        for i in nums:
            if i in dupl:
                return True
            else: 
                dupl[i] = i
        return False