# Understand
# Find a subarray with the largest sum and return the sum
# Need to find a set of undisrupted indicies that are
# Close together and their sum will be the max value

# Plan
# We will do a sliding window / Kadane's algorithm approach
# if at any point our section is negative. We can reset
# the sliding window.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The variables that will hold our current and max sum
        currSum, maxSum = nums[0], nums[0]

        i = 1
        while i in range(len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            maxSum = max(currSum, maxSum)

            i += 1

        return maxSum




        