# can we do a weird binary search where instead of mid
# we check left and right respectievly?

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        # instead we would have an infinite loop if we did <= r I think
        print(f"=======Debugging========")
        while r - l > 1:
            mid = l + ((r-l) // 2)


            print(f"l: {l}")
            print(f"nums[l]: {nums[l]}")
            print(f"r: {r}")
            print(f"nums[r]: {nums[r]}")
            print(f"mid: {mid}")
            print(f"mid: {nums[mid]}")
            if nums[l] < nums[r]:
                print(f"Moving r to mid")
                r -=1

            else: 
                l += 1
                print(f"Moving l to mid")
            print()

        if l != r:
            return min(nums[l], nums[r])
        
        return nums[mid]
