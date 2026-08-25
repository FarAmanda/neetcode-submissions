# Two pointers
# One at the end, one at the start
# Once we encounter a wrong character, we move pointer both left and right
# and we check both at the same time

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:

            if s[l] != s[r]:
                shiftL = s[l+1: r+1]
                shiftR = s[l : r]

                return (shiftL == shiftL[::-1]
                or shiftR == shiftR[::-1])  

            l+=1
            r-=1 


        return True