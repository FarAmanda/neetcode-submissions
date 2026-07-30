# Understand
# Similar to the last problem, 
# Return the maximum area of water that can be 
# trapped between ALL bars

# Would we need to do two pointers at the far end(s)

# I don't believe multiplication would be super necessary
# 

# An Idea I have is similar to having a left and right pointer
# r_pointer starts at left_pointer + 1 and it keeps moving until it finds a 
# ridge that is higher than l_pointer, once it does we add the "sum" of the empty blocks
# to the result
# l_pointer now moves to r_pointer, r_pointer moves to r_pointer - 1
# this keeps going until r_pointer trails off. 

# only issue is, r_pointer doesnt NEED to be taller than l_pointer, there just 
# needs to be a dip of some capacity, 

# there might be a scenario of
#
#   #
# # #

# which would hold 1 

# but there can also be. 
#       #
#   #   #
# # # # #

# We don't know where our min or max edge is. 
# That is the tricky part

# which would now hold 5.
# when do we know to "cap" the water?


# An idea I have is similar to the last problem
# Where we keep moving adding the min height - the amt thats in the index
# until we get to a height thats larger than our minimum height? 

# Also

class Solution:
    def trap(self, height: List[int]) -> int:
        # Setting our pointers
        res = 0
        l, r = 0, len(height) - 1
        
        # Make sure starting out that l_pointer & r_pointer are at an appropriate place
        while l < len(height) - 1 and height[l] == 0:
            l += 1

        while r > 0 and height[r] == 0:
            r -= 1

        minimumHeight = min(height[l], height[r])
        sumWater = 0
        
        while l < r:
            
            # Traversing Left Side
            if height[l] < height[r] : 
                if height[l] > minimumHeight:
                    minimumHeight = min(height[l], height[r])
                    continue
                # Might be a way to make this cleaner / coalesce this in the above
                l += 1 
                sumWater += max(0, minimumHeight - height[l]) 

            # Traversing right side
            else:               
                if height[r] > minimumHeight:
                    minimumHeight = min(height[l], height[r])
                    continue
                # Might be a way to make this cleaner / coalesce this in the above
                r -= 1 
                sumWater += max(0, minimumHeight - height[r]) 

            res += sumWater
            sumWater = 0

        return res



