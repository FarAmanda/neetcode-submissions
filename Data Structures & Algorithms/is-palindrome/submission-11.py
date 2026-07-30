# Understand: Taking in any string input
# Check to see if it is a palindrome
# Input may have spaces or punctuation
# Must be removed / skipped in order to check if a

# Plan: Have 2 pointers checking the first and 
# Last character

class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s) -1
        start = 0
        palin = s.lower()
        while start < end:
            if not (palin[end].isalpha() or palin[end].isnumeric()):
                end -= 1
                continue
            if  not (palin[start].isalpha() or palin[start].isnumeric()):
                start += 1
                continue
            
            print(palin[start], palin[end])
            print(start, end)
            print()
            if palin[start] != palin[end]:
                return False
            end -= 1
            start += 1

        return True
        