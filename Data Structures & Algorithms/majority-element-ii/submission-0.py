class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        d = {}

        m = int(len(nums) / 3) + 1
        for i in nums:
            d[i] = d.get(i, 0) + 1

            if d[i] == m:
                res.append(i)


        return res
