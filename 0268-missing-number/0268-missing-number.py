class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        xor1=xor2=0
        for i,value in enumerate(nums):
            xor1^=(i+1)
            xor2^=value
        return xor1^xor2


