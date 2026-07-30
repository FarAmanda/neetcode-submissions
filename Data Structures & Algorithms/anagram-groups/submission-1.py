class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strDict = {}

        for word in strs:
            bucket = [0] * 26
            for lett in word:
                
                y = ord(lett) - ord('a')

                bucket[y]+=1

            print(bucket)

            if tuple(bucket) in strDict:
                strDict[tuple(bucket)].append(word)

            else:
                strDict[tuple(bucket)] = [word]

        return list(strDict.values())