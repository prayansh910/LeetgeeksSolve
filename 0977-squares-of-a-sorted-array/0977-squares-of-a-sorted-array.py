class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        res=[0]*n
        l=0
        r=n-1
        i=n-1
        for j in range(n):
            nums[j]**=2
        while l<=r:
            if nums[l]>nums[r]:
                res[i]=nums[l]
                l+=1
            else : 
                res[i]=nums[r]
                r-=1
            i-=1
        return res