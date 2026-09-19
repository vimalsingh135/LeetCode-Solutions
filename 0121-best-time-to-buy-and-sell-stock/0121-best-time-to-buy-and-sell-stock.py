class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        profit=0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]          # cheapest day to buy so far
            elif prices[i] - min_price > profit:
                profit = prices[i] - min_price  # best sell if we sold today
        return profit
        