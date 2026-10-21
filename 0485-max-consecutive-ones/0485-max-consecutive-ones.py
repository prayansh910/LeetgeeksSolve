class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=maxcount=0
        for i in nums:
            if i==1:
                count+=1
                maxcount=max(count,maxcount)
            else:
                count=0
        return maxcount