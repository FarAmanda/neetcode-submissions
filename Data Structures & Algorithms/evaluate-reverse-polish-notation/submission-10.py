class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arith = []

        for i in tokens:

            # Adding
            if i == "+":
                num1 = arith.pop()
                num2 = arith.pop()
                print(num1, i, num2)
                arith.append(num2 + num1)


            # Subtracting
            elif i == "-":
                num1 = arith.pop()
                num2 = arith.pop()
                print(num1, i, num2)
                arith.append(num2 - num1)
        
            # Multiplying
            elif i == "*":
                num1 = arith.pop()
                num2 = arith.pop()
                print(num1, i, num2)
                arith.append(num2 * num1)

            # dividing
            elif i == "/":
                num1 = arith.pop()
                num2 = arith.pop()
                print(num1, i, num2)
                arith.append(int(num2 / num1))

            else:
                arith.append(int(i))

        return arith[0]