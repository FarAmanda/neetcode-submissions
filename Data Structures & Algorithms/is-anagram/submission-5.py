# I'm thinking of solving this with a bucket array
# We have two arrays of size 26
# that we use to count how many letters exist
# 

# Conditions
# Letters have to be of the same equal length
# 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sArr = [0] * 26
        tArr = [0] * 26


        for i in range(len(s)):
            lettS = ord(s[i]) - ord('a')
            lettT = ord(t[i]) - ord('a')

            sArr[lettS] += 1
            tArr[lettT] += 1

        return sArr == tArr

