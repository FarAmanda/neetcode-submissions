class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        amt = len(nums)
        check = set(nums)

        return not (amt == len(check))
        