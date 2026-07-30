class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            code += str(len(word)) + "#" + word

        return code

    def decode(self, s: str) -> List[str]:
        # Our return value list
        res = []
        
        # Our while loop to go through the string
        i = 0
        while i < len(s):
            # our second pointer
            j = i

            # We do this in the event our amt of 
            # letters is more than a single digit
            while s[j] != '#':
                j += 1

            # gets our distance between i & j
            length = int(s[i:j])

            i = j+1
            j = i + length

            word = s[i:j]
            res.append(word)
            i = j

        return res

            
