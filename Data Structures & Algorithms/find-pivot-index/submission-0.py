# Understand
# In an array, there is a digit where the opposing sides are equal to one another.
# We want to return the index of that number

# Plan
# ultimately the plan is to make a prefix sum, but how do we calculate everything prior? 

# An Idea, create the prefix sum array
# hold the very last value for reference
# iterate through prefix sum one more time to determine when we get that final value - everything prior



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        rightSum = 0


        for i in nums:
            total += i
            prefix.append(total)

        rightSum = prefix[-1]


        for i in range(len(prefix)):
            if i == 0 and prefix[-1] - prefix[i] == 0:
                return 0
            if prefix[-1] - prefix[i] == prefix[i-1]:
                return i

        return -1