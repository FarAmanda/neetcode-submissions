# Understand: Given an array of "asteroids"
# Determine which asteroids will remain

# Asteroids remaining is in relation to the absolute value of each asteroid
# Only those with opposing signs are destroyed

# I assume this means only asteroids of the same sign can remain
# meaning we can't have a [-3, 9] output
    # We need a way to determine if the number is negative or not


# Trick is, take into account the direction asteroids are going
# the negative asteroids will always move left
# and the pos asteroids will always move right

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for i in asteroids:
            # If res is empty we auto append
            if not res:
                res.append(i)

            # if i is positive, we can just append
            elif (i < 0 and res[-1] < 0) or i >= 0:
                res.append(i)

            # if top of res is pos, and incoming asteroid is negative
            elif (res[-1] >= 0 and i < 0):
                while res:
                    # top of res is smaller, blow up
                    if abs(res[-1]) < abs(i):
                        res.pop()
                        # Append if we exhaust list


                    # if top value is equal to incoming value
                    # blow up both and break out of loop
                    elif abs(res[-1]) == abs(i):
                        res.pop()
                        break

                    # if top value is greater than incoming
                    # blow up incoming
                    elif abs(res[-1]) > abs(i):
                        break

                    if not res or (res[-1] < 0 and i < 0):
                        res.append(i)
                        break

        return res
                    



             