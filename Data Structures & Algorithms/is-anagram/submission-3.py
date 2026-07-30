class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sArr = [0] * 26
        tArr = [0] * 26

        for i in s:
            lett = ord(i) - ord('a')
            sArr[lett] += 1

        for k in t:
            lett = ord(k) - ord('a')
            tArr[lett] += 1


        return sArr == tArr
            

        