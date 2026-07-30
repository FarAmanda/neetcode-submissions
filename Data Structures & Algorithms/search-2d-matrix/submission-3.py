class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1
        # first identify the array that the target is in
        # how to calculate the mid point?

        print(f"======Debuggging: Find Row=======")
        while t <= b:

            midRow = int(t + ((b-t)/2))
            
            print(f"matrix[t]: {matrix[t]}")
            print(f"matrix[midRow]: {matrix[midRow]}")
            print(f"matrix[b]: {matrix[b]}")
            print()
            print(f"--------------")
            # should we check the first indicie?
            if matrix[midRow][0] == target:
                return True
            elif matrix[midRow][0] > target:
                b = midRow - 1
            elif matrix[midRow][0] < target:
                t = midRow + 1
        # Identify the specific index it exists in

        midRow = b
        arr = matrix[midRow]
        l = 0 
        r = len(arr) - 1

        print(f"======Debuggging: Find Index=======")
        print(f"t:{t}")
        print(f"b:{b}")
        print(f"midrow:{midRow}")
        print(f"arr: {arr}")
        print(f"======Loop Start=========")
        while l <= r:
            mid = int(l+ (r-l)/2)
            print(f"l:{l}")
            print(f"r:{r}")
            print(f"mid:{mid}")
            print(f"arr[mid]: {arr[mid]}")
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False