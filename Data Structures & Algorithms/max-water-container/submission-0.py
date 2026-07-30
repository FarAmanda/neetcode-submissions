# Understand: Container with most water
# We are to return the maximum amt of water a container can store
# using the numbers in the input
# how is 7 & 7 returning 

# Okay this question is obscene with its wording
# We are to build a "metaphorical" container

# each indicie contains is a height
# the array indicie represents its place on the x axis
# Using 2 bars & the x intercept
# return the max amt. of water this metaphorical container can hold

# do we do two pointers?
# Yes I assume because we need an end, and we need a start
# But how do we calculate a solution
# Because it isn't sorted, I am unsure
# Of how to increment or decrement our pointers

# Things to keep in track
# lPointer and rPointers value (and the max between them)
# the distance between the two

# The max container we found
# This sounds like a sliding window solution
# but admittedly I suck at processing this

# We can probably brute force a solution


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0
        while left < right:
            width = right - left
            area = width * min(heights[left], heights[right])
            print("Width:", width, "Left:", left, "Right:", right)
            print(heights[left], heights[right])
            print(maxArea, area)
            maxArea = max(maxArea, area)
            right -= 1
            if right == left:
                left += 1
                right = len(heights) - 1

        return maxArea
        