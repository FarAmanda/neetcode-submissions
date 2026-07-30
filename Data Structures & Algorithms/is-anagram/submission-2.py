class Solution:
# Understand
    # Determine whether two strings
    # Contain the same letters in the same amount

# Plan 
    # Inevitable to go through the entirety of both strings
    # Going through S we should collect each letter and tally
    # their amt.
    # Going through T similarly each letter should be tallied
    # One idea is setting up two dicts?
    # I wonder if it can be done with one dict
    # Currently the issue is, what if t has the same letters
    # as s, but less of them. It needs to be required for 

    def isAnagram(self, s: str, t: str) -> bool:
        thisdict = {}

        for x in s:
            if x in thisdict:
                thisdict[x] += 1
            else:
                thisdict[x] = 1

        for y in t:
            if y in thisdict:
                thisdict[y] -= 1
                if thisdict[y] == 0:
                    thisdict.pop(y)
            else:
                return False
        if (len(thisdict) == 0):
            return True
        else: 
            return False




