class Solution(object):
    def isPalindrome(self, s):
        s="".join(char for char in s if char.isalnum()).strip().lower()
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            else :
                i+=1
                j-=1
        return True        