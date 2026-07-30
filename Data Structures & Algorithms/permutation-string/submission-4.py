class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            print("False Statement 1")
            return False
        
        bucket1 = [0] * 26
        bucket2 = [0] * 26

        for char in s1:
            lett = ord(char) - ord('a')

            bucket1[lett] += 1

        ## Setting up our sliding window:
        lPtr = 0
        rPtr = 0
        while rPtr < len(s1):
            char = s2[rPtr]
            lett = ord(char) - ord('a')
            bucket2[lett] += 1
            rPtr+= 1
        
        while rPtr < len(s2):
            # Debugging statements
            print(bucket1)
            print(bucket2)
            print('lPtr:', lPtr)
            print('rPtr:', rPtr)
            print('\n\n\n')


            if bucket1 == bucket2:
                return True

            else:
                
                rmLett = ord(s2[lPtr]) - ord('a')
                addLett = ord(s2[rPtr]) - ord('a')
                lPtr += 1

                bucket2[rmLett] -= 1
                bucket2[addLett] += 1
            rPtr += 1

        
        return bucket2 == bucket1