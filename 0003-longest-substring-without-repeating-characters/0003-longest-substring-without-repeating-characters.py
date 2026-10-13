class Solution(object):
    def lengthOfLongestSubstring(self, s):
        repeated={}
        l=r=maxlen=0
        n=len(s)
        while(r<n):
            char=s[r]
            if char in repeated and repeated[char]>=l:
                l=repeated[char]+1
            maxlen=max(maxlen,r-l+1)
            repeated[char]=r
            r+=1
        return maxlen
                

        