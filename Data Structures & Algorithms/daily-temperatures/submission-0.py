class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                
                stackTemp, stackInd = stack.pop()
                print("Indicie:", i)
                print("Temperature:", t)
                print("stackTemp:", stackTemp)
                print("stackInd:", stackInd)
                print()
                res[stackInd] = i - stackInd
                print("res updated:", res)
            
            stack.append([t,i])

        return res

            


        