class Solution(object):
    def twoSum(self, nums, target):
        arr=[]

        for i in range(len(nums)):
            arr.append((nums[i],i))
        
        arr.sort()

        l=0
        r=len(arr)-1
        while l<r:
            s=arr[l][0]+arr[r][0]

            if s==target:
                return arr[l][1],arr[r][1]
            elif s>target:
                r-=1
            else :
                l+=1
