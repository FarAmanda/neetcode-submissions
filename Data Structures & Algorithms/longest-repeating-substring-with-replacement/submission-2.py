# Understand
# We need to implement a sliding window taking into account
# How many "K's" we have in reserve
# We can have an l_pointer and r_pointer, r_pointer moves as long as we have
# k's in reserve
# L moves when we dont

# Plan
# 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Set our pointers to 0, dictionary, and value for res
        left, right = 0, 0
        chars = {}
        res = 0

        while right < len(s):
            
            chars[s[right]] = chars.get(s[right], 0) + 1

            while sum(chars.values()) - max(chars.values()) > k:
                chars[s[left]] -= 1
                left += 1    

            res = max(res, right - left + 1) 
            right += 1


        return res



