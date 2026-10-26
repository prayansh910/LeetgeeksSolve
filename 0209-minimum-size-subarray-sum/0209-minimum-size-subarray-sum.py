class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=r=current_sum=0
        minlength=float('inf')
        n=len(nums)
        while(r<n):
            current_sum+=nums[r]
            #if current_sum<target:
               # current_sum+=nums[r]

            while current_sum>=target:

                minlength=min(minlength,r-l+1)
                current_sum-=nums[l]
                l+=1
            r+=1
        if minlength==float('inf'):
            return 0
        else: return minlength

            


            