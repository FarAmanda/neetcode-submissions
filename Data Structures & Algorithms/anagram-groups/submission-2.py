class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect = defaultdict(list)

        for word in strs:
            bucket = [0] * 26
            for lett in word:
                index = ord(lett) - ord('a')
                bucket[index] += 1

            collect[tuple(bucket)].append(word)
        
        return list(collect.values())