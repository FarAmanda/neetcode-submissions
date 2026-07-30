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