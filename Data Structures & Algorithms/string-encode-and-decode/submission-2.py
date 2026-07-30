class Solution:
    ## Need to join string to a single string
    ## then separate it
    ## combining a string is fairly simple
    ## but knowing when & where to separate is the difficult part
    ## perhaps between each word we add 3 character combinations
    # $%^
    # as our indicatory to split them

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            for char in word:
                code += char
            code+= "!2)"

        return code




    def decode(self, s: str) -> List[str]:
        # Make our result array
        res = []
        # Make our variable that will hold our code
        code = ""
        # string that indicates our separator
        seperator = "!2)"
        # Count variable to indicate how much of separator we've encountered
        count = 0

        # for every letter in our code
        for i in s:
            # append the current letter
            code += i
            # check if letter is apart of count 
            if i == seperator[count]:
                ## i it is, increment
                count+=1

                # if count is also = 3,
                if count == 3:
                    # pop the 3 most recent letters
                    code = code[:-3]
                    # append the full code to res
                    res.append(code)
                    # flush out our string
                    code = ""
                    count = 0
            ## otherwise, set it to 0 if need be
            else:
                count = 0
        return res

            
