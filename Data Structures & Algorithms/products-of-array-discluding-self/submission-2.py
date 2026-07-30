class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        print(nums)
        res = []
        for k in range(len(nums)):
            i = 0
            print("...")
            print(k)
            print(i)
            print("...")
            product = 1

            while i < len(nums):
                if i == k:
                    i += 1 
                    continue

                else:
                    product *= nums[i]

                i += 1

            res.append(product)

        return res