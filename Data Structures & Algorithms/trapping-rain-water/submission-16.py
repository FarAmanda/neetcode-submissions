# Understand: Across the entire diagram, trap water whenever there are borders 
# On the left & the right

# Edge cases to consider
# 1.    The bounds of the array (prior to 0, and after the last elemet)
#       Do not count as a border
# 2.    Water can not be contained past the minimum boundary 
# 3.    If there is an increase in height on the minimum side, 
#       We don't add anything

# Plan
# 1.    Using two pointers, first we traverse until we encounter
#       a boundary, 
# 2.    We store the minimum of the two bounds
# 3.    We traverse the minimum bound pointer until we find a new maximum
# 4.    As we traverse, take into account how much "water is being stored"
#       As we go
# 5.

class Solution:
    def trap(self, height: List[int]) -> int:
        # Setting our bounds
        left, right = 0, len(height) - 1
        
        # Setting left & right at appropriate indexes
        while left < len(height) and height[left] == 0:
            left += 1
            
        while right > left and height[right] == 0:
            right -= 1

        # Determining our minimum height,
        # might not be necessary?
        if not left < right:
            return 0     
        res = 0

        minimumHeight = min(height[left], height[right])
        
        while left < len(height) - 1 and left < right:

            # Traversing Left

            if height[left] < height[right]:
                left += 1
                if minimumHeight < height[left]:
                    minimumHeight = min(height[left], height[right])
                res += max(0, minimumHeight - height[left])

            else:
                right -= 1
                if minimumHeight < height[right]:
                    minimumHeight = min(height[left], height[right])

                res += max(0, minimumHeight - height[right])


        return res   
















