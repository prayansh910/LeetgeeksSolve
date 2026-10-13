class Solution(object):
    def maxScore(self, cardPoints, k):
        n=len(cardPoints)
        lsum=rsum=maxsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum=lsum
        rindex=n-1
        for j in range(k,0,-1):
            lsum-=cardPoints[j-1]
            rsum+=cardPoints[rindex]
            rindex-=1
            maxsum=max(maxsum,lsum+rsum)
        return maxsum
