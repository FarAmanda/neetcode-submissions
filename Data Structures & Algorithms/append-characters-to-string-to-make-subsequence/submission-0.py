# two strings, s & t
# we want to append t in such a way to s that there will be a subsequence
# it recommends to answer this with arrays but I think we can solve this with ptrs
# two pointers, one at start of s, one at t
# if sptr shares a character with where t ptr currently is, increment both
# otherwise move sptr and maintain tptr
# return len(t) - tptr

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        r, l = 0, 0

        while r < len(s) and l < len(t):
            if s[r] == t[l]:
                l += 1
            r += 1


        return len(t) - l

