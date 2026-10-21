class Solution(object):
    def reverseVowels(self, s):
        listed_str=list(s)
        n=len(listed_str)
        l=0
        r=n-1
        vowels={'a', 'e', 'i', 'o','u','A','E','I','O','U'}
        while(l<r):
            if listed_str[l] not in vowels:
                l+=1
            elif listed_str[r] not in vowels:
                r-=1
            else:
                listed_str[l],listed_str[r]=listed_str[r],listed_str[l]
                l+=1
                r-=1
               
        s="".join(listed_str)  
        return s    
