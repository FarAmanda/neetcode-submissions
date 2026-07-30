# Understand: We will have a list that will contain a balance of operators and numbers

# ATM it seems from the two example cases there will always be two numbers
# and then an operator

# Plan
# Implement a stack
# Push the two numbers on the stack
# encounter an operator
# pop the numbers to respective variables and 
# do the operation


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for i in tokens:
            if i == "+":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num1 + num2)

            elif i == "-":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(num1 - num2)

            elif i == "/":
                num2 = nums.pop()
                num1 = nums.pop()
                nums.append(int(num1 / num2))

            elif i == "*":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(num1 * num2)

            else:
                nums.append(int(i))

        return nums[0]