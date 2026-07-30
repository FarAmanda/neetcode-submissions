# Understand: Determine whether there are duplicate numbers
# in an array

# For this I'm thinking of solving it with a hashmap
# as soon as there is a value in the dictionary
# we return true

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}

        for i in nums:
            if i in res:
                return True
            else:
                res[i] = 1
        return False
        