class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            size = len(i)
            res+= str(size) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        lPtr = 0
        rPtr = 0
        res = []

        while rPtr < len(s):            
            print("\n------ Before Loop Test------")
            print("lptr")
            print(f"lptr value:{lPtr}")
            print(f"lptr index:{s[lPtr]}")
            print("\nrptr")
            print(f"rptr value:{rPtr}")
            print(f"rptr index:{s[rPtr]}")
            while s[rPtr] != "#":
                rPtr +=1
                print("\n------ Loop Test------")
                print("\nRPtr")
                print(f"rptr value:{rPtr}")
                print(f"rptr index:{s[rPtr]}")
            
            num = int(s[lPtr:rPtr])
            print("\n***********")
            print(num)
            print("***********")
            lPtr = rPtr + 1
            rPtr += num + 1


            word = s[lPtr:rPtr]
            res.append(word)

            lPtr = rPtr 
            rPtr = lPtr + 1

        return res

