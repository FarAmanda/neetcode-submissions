# Understand given an array,
# Update it so that all k instances of 
# a value are not present in the first len(array) - k indicies
# We are not returning a new array with only the not k values
# we are changing the array to overwrite the k instances
# with new other values that exist in the array


# plan, we only need to go as far as "n" being the len of nums
# but if we remove a k, we can update it with 'n'
# and subtract 1 from n
# almost like a 2 ptr approach
# we return where our last ptr is

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            
            else:
                l += 1

        return l