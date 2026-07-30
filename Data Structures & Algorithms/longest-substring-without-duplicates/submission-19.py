# Understand, we want to see how long we can go through a string w/o duplicating a letter
# EG fsevcds, longest would be fsevcd
# or drcsrstui longest would be rstui


# Plan: 
# I think this can be solved with 2 pointers, and perhaps a dictionary? 
# Or rather an array that we can append / push / pop, with a queue (FIFO)
#  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # In case where array does not exist
        if not s:
            return 0 

        # Proceed with program
        dicts = {}
        res = []
        res.append(s[0])
        dicts[s[0]] = 1
        maxSub, currentSub = 1, 1

        # Will we run into an error if there isn't a 1 index?
        # Seems like thats a no
        for i in s[1:]:

            # We find encounter a letter already in the substring
            if i in dicts:
                # We update maxSub before any popping 
                # or incrementing of currentSub occurs
                maxSub = max(currentSub, maxSub)

                # We go through the array (and dict) removing letters until we come upon
                # The duplicated letter
                while currentSub > 0 and res[0] != i:
                    dicts.pop(res[0])
                    res.pop(0)
                    currentSub -= 1
                # can we make this less redundant?
                # These two lines of code are here to properly pop the duplicate element
                if res:
                    dicts.pop(res[0])
                    res.pop(0)
                    currentSub -= 1

            # Add the letter to the dict (if it hasn't been already added 
            # + has been previously removed)
            dicts[i] = 1
            res.append(i)
            currentSub += 1
            maxSub = max(currentSub, maxSub)   

        # In the event we did not update maxSub in that last run
        return maxSub