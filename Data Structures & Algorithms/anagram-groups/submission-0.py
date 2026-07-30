# Plan, we do bucket sort all the strings
# whatever has the same bucket, we append onto the dict



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucketDict = defaultdict(list)

        for word in strs:
            bucket = [0] * 26
            
            for lett in word:
                bucket[ord(lett) - ord('a')] += 1

            bucketDict[tuple(bucket)].append(word)

        return list(bucketDict.values())