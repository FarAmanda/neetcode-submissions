class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sB = [0] * 26
        tB = [0] * 26

        for i in range(len(s)):
            sLett = ord(s[i]) - ord('a')
            tLett = ord(t[i]) - ord('a')

            sB[sLett] += 1
            tB[tLett] += 1 




        return sB == tB
            