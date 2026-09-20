class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            sum1=numbers[i]+numbers[j]
            if sum1==target:
                return [i+1,j+1]
            elif sum1>target:
                j-=1
            else:
                i+=1
        