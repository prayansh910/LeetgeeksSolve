class Solution(object):
    def missingNumber(self, nums):
        allnums= [i for i in range(0,len(nums)+1)]
        n= [item for item in allnums if item not in nums]
        return n[0]