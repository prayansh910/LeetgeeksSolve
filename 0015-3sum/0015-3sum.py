class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        new=[]

        for i in range(len(nums)-2):
            if nums[i]==nums[i-1] and i>0:
                continue

            j=i+1
            k=len(nums)-1
            while(j<k):
                
                if nums[i]+nums[j]+nums[k]==0:

                    new.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
        return new


                
