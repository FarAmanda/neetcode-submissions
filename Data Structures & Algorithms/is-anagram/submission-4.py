class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ## Create a bucket for each string
        sBucket = [0] * 26
        tBucket = [0] * 26

        for i in range(len(s)):
            sLett = ord(s[i]) - ord('a')
            tLett = ord(t[i]) - ord('a')

            sBucket[sLett] += 1
            tBucket[tLett] += 1

        return sBucket == tBucket