class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif len(stack) != 0:
                if i == ")" and stack.pop() != "(":
                    return False 
                elif i == "]" and stack.pop() != "[":
                    return False 
                elif i == "}" and stack.pop() != "{":
                    return False 
            else:
                return False

        return len(stack) == 0