class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        paren = {'{' : '}', '[' : ']', '(' : ')'}


        for i in s:
            if i in paren:
                res.append(i)

            else:
                if res and paren[res[-1]] == i:
                    res.pop()

                else: 
                    return False

        return len(res) == 0

