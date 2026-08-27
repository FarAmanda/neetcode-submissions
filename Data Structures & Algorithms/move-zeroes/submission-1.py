# Understand: Given an array with at least 1 value
# that may or may not have 0s, move all the 0s to the right
# While maintaining the order of the array
# We could do a bubble sort approach
# I am trying to think of how to do this with two pointers
# but in a way that doesn't swap values
# If we start at the end 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0

        while r < len(nums):
            if nums[r] == 0:
                r+= 1

            elif nums[r] != 0 and r != l:
                nums[l] = nums[r]
                nums[r] = 0
                r += 1
                l+= 1

            else:
                l+= 1
                r+= 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        