# Understand Can you reach the end of the index using the values inbetween?

# If we are at 0, we can't progress,
# if we are at an index of any n value, we can move to any value up to n,
##### Which does not stack btw.

# Plan, move backwards, the amount we can jump doesn't really matter
# Just can we reach the previous flag with the current number

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Obtain the our final index
        flag = len(nums) - 1

        # an error is that our final index is 0, which is fine.

        for i in range(len(nums)-1, -1, -1):
            ## If our flag has reached the start, we know we have a route
            
            # If our position i, + the amount of steps obtained
            # from our index >= flag, that means we have enough
            # so if we are at index 3, and index 3 has a 2, and 
            # we need to get a 4, we are guuci
            if i + nums[i] >= flag:
                flag = i

        return flag == 0
        


            
