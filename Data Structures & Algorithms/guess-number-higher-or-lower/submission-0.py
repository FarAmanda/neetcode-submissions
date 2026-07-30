# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n

        print("====Debugging====")
        while l < r:

            mid = l + ((r-l)//2)
            print(f"l: {l}")
            print(f"mid: {mid}")
            print(f"r: {r}")
            res = guess(mid)
            print(f"res: {res}")
            print()
            
            if res == 0:
                return mid

            elif res == -1:
                r = mid - 1

            else:
                l = mid + 1

        
        return l if guess(l) == 0 else r
