class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i 

        return res

    def decode(self, s: str) -> List[str]:
        lPtr = 0
        rPtr = 1

        res = []
        while rPtr < len(s):
            while s[rPtr]!= "#":
                rPtr += 1

            lN = int(s[lPtr:rPtr])

            lPtr = rPtr + 1
            rPtr += lN + 1
            res.append(s[lPtr:rPtr])


            lPtr = rPtr

        return res
