class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1 and nums[0] == target:
            return 0
        
        print(f"=======Debugging=======")
        while l < r:
            
            mid = int(l + ((r-l)/ 2))
            print(f"l: {l}")
            print(f"r: {r}")
            print(f"mid: {mid}")
            print(f"nums[mid]: {nums[mid]}")

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if nums[l] == target:
            return l
        else:
            return -1