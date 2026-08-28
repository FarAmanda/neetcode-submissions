# Understand: Given an array that contains duplicates,
# Remove said duplicates in place
# The array will be sorted in non-decreasing order
# 
# an easy way to do it was to make it into a set and return the size. OKAY THAT WONT WORK
# we will do 2 ptrs
# l will be the most recent non(?) dupe element
# r will be the one going through array

# I am a bit confused of the logic that I want to do
# do I swap as soon as nums[l] ! = nums[r]? I don't think I do that
# [0, 1] is good, we shouldnt do anything but continue searching with r
# I think the logic is
# if nums[l] != nums[r] we increment l
# we do this in a while loop?
# and if nums[l] == nums[r] we increment r UNTIL r trails off or finds a new value
# and as soon as it finds a new value THEN we move?
# but I see so many errors with this

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 1

        while r < len(nums):
            # [0, 0, 2, 2, 3, 4]
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]

            r += 1

        return l+1

