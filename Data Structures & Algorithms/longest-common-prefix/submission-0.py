class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # We can't get a prefix longer than the shortest word
        word = min(strs)
        print(word)
        index = 0
        prefix = ""

        
        for i in range(len(word)):
            lett = word[index]
            for x in strs:
                if x[index] != lett:
                    return prefix
            index += 1
            prefix += lett

        return prefix

            

