# A plan: 
# We have 2 ptrs
# if rptr is smaller than lptr, we move it immediately
# otherwise we calculate the max sum between them
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSum = 0
        lPtr = 0
        rPtr = 1
        
        while rPtr < len(prices):
            if prices[lPtr] > prices[rPtr]:
                lPtr = rPtr
            elif prices[lPtr] < prices[rPtr]: 
                maxSum = max(maxSum, prices[rPtr] - prices[lPtr])

            rPtr+= 1

        return maxSum