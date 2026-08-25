class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        elif not word2:
            return word1

        else:
            return word1[0] + self.mergeAlternately(word2, word1[1:])