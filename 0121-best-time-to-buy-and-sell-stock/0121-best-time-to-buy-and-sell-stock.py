class Solution(object):
    def maxProfit(self, prices):
        minpric=float('inf')
        maxprof=0
        for i in range(len(prices)):
            if prices[i]<minpric:
                minpric=prices[i]
            if maxprof<prices[i]-minpric:
                maxprof=prices[i]-minpric
        return maxprof