class Solution(object):
    def sortColors(self, nums):
        n= len(nums)
        p=q=r=0
        for i in nums:
            if i ==0:
                p+=1
            elif i== 1:
                q+=1
            else: r+=1
        for i in range(p):
            nums[i]=0
        for i in range(p,p+q):
            nums[i]=1
        for i in range(q+p,p+q+r):
            nums[i]=2
            


            
        