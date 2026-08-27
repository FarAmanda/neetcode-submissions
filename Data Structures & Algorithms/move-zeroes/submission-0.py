# Understand: Given an array with at least 1 value
# that may or may not have 0s, move all the 0s to the right
# While maintaining the order of the array
# We could do a bubble sort approach
# I am trying to think of how to do this with two pointers
# but in a way that doesn't swap values
# If we start at the end 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, len(nums) -1

        while l < r:
            if nums[l] == 0:
                m = l
                while m < r:
                    nums[m] = nums[m+1]
                    m+= 1
                nums[m] = 0
                r-= 1
            else:
                l+=1

            

        
        """
        Do not return anything, modify nums in-place instead.
        """
        