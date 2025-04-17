class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            
            maxProfit = max(maxProfit, prices[r] - prices[l])

            if prices[r] < prices[l]:
                l = r #buying at a new low, your l pointer should ideally find the lowest point in time to buy. and you're preventing buying and selling on the sane day because in the problem it says you must choose a different day.

            r += 1
        return maxProfit