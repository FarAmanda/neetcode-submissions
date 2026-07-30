# Understand (Encode), given an array, using whatever means, combine the indicies or the variables
# into a singular string

# Understand (Decode), given a string, be able to decipher where the string starts and ends 
# and separate it into it's own list indicie

# Plan (encode): as we combine each string, we'll add the number of letters and a hash to signify the 
# begining and end of a string

# Plan (decode): as we separate each string, we will refer to the number of letters in the following
# string that we placed earlier
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            num = len(i)
            res += str(num) + "#" + i

        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 1

        res = []

        while r < len(s):
            while s[r] != "#":
                r += 1

            # we are slicing between l and r, 
            # slicing is not inclusive, so we should stop
            # just before the hash 
            # But my expectation is, we return the full number
            # between the start of l, to r-1
            lettLen = int(s[l:r])
            
            # move r to the start of the word
            r += 1
            word = s[r : r + lettLen]
            res.append(word)

            l = r + lettLen
            r = l + 1

        return res


            

