class Solution(object):
    def maxProfit(self, prices):
        min_price= float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price= prices[i]
            if prices[i]-min_price > max_profit:
                max_profit= prices[i]-min_price
        
        return max_profit