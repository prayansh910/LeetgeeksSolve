class Solution(object):
    def singleNumber(self, nums):
        repeat=[]
        for num in nums:
            if num not in repeat:
                repeat.append(num)
            else:
                repeat.remove(num)
        return repeat[0]
                
        