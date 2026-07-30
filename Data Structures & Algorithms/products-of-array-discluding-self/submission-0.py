# Understand, 
# Produce a new array, in respect to the original one where
# Each indicie is the product of all the others, w/o the og


# Some things to take note, if there is a 0 that fucks us don't it hm
# the way prefix sum works is we 
# go from left to right
# and add the current to it's previous

# Some Constraints
# We can't simply find the product of all the indicies, and divide by current one that we're at
# 

# [1, 2, 4, 6]

# [1, 2, 8, 48]
# [6, 24, 48, 48]


# [48, 24, 12, 8]
# [8, 12, 24, 48]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, sufix = [], []

        prefix.append(1)
        sufix.append(1)

        product = 1
        # settin up prefix array
        for i in nums:
            product *= i
            prefix.append(product)

        product = 1
        for i in range(len(nums)-1, -1, -1):
            print(i)
            product *= nums[i]
            sufix.append(product)

        print(nums)
        print()
        print(prefix)
        print(sufix)
        res = []

        for i in range(len(nums)):
            end = len(sufix) - 2 - i
            print(end)
            res.append(prefix[i] * sufix[end])
            

        return res
            
            

        