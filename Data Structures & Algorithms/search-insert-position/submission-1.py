# Understand: We are given a sorted array
# We need to find a value target in o(log n) time
# if we find it, return that index

# if not, we return where it should be.

# Edge cases
# list is empty, should be placed in 0 position
# If we look at the constraints, we don't have to worry about that
# It might appear outside the list, such as in the len(nums) position
# or just before the 0 index --> I assume in this case we just place it in
# the 0 index

# Plan Set up binary search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 
        
        print("======Debug======")
        while l <= r:

            mid = l + int((r-l)/2)
            print(f"l: {l}")
            print(f"r: {r}")
            print(f"mid: {mid}")
            print(f"nums[mid]: {nums[mid]}")
            print()
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid - 1

            elif nums[mid] < target:
                l = mid + 1
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid
        