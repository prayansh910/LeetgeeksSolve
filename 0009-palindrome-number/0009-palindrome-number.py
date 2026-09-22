class Solution(object):
    def isPalindrome(self, x):
        INT_MAX=2**31-1
        num=x
        rev=0
        if x<0:
            return False
        while x>0:
            d=x%10
            x=x//10
            if rev>(INT_MAX-d)//10:
                return False
            rev=(rev*10)+d
        if rev==num:
            return True
        else:
            return False

        