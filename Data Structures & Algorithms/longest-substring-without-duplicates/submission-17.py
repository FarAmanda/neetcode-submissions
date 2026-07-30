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
            print()
            print("MaxSub:", maxSub)
            print("currentSub:", currentSub)
            print()

            if i in dicts:
                maxSub = max(currentSub, maxSub)
                print("Currently searching for:", i)
                print("Dictionary items:", dicts.keys())
                while currentSub > 0 and res[0] != i:
                    dicts.pop(res[0])
                    print(res.pop(0))
                    currentSub -= 1
                # can we make this less redundant?
                # These two lines of code are here to properly pop the duplicate element
                if res:
                    dicts.pop(res[0])
                    res.pop(0)
                    currentSub -= 1
                print()
                print("->Updated MaxSub:", maxSub)
                print("->Updated currentSub:", currentSub)
                print()

            dicts[i] = 1
            res.append(i)
            currentSub += 1   


        return max(currentSub, maxSub)