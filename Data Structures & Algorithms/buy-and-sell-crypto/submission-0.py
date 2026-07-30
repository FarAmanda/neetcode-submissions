class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        res = 0
        minStock = prices[0]
        for i in prices:
            print("Highest Amt:", minStock, "\nCurrent Price:", i,
             "\nResult:", res)
            print()
            if i == minStock:
                continue
            
            if minStock < i:
                if i - minStock > res:
                    
                    res = i - minStock

            elif minStock > i:
                minStock = i

        return res
