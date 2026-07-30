class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print("While Loop End:\ni is", i, "\nj is", j)
            length = int(s[i:j])
            print("Length:", length)
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res




