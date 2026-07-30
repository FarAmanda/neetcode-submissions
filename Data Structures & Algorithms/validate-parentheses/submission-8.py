class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parenDict = {')' : '(', ']' : '[', '}' : '{'}



        for i in s:
            if i in parenDict:
                if stack and parenDict[i] == stack.pop():
                    continue
                else: 
                    return False
            
            else:
                stack.append(i) 

        return len(stack) == 0
        # Try using dicts to make code cleaner