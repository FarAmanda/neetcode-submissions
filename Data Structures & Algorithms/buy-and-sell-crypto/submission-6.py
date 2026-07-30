# Ultimately we need to keep track of the lowest value & the highest value next to it
# if at any point our right pointer gets a new min, we move it there
# If at any point we get a new high, we update the max profit (when possible)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        if not prices:
            return 0
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

            else: 
                l = r
            r+=1

        return maxP