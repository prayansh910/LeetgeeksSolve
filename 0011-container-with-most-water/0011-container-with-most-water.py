class Solution(object):
    def maxArea(self, height):
        MAX=0
        l=0
        r=len(height)-1
        
        
        while(l<r):
            if min(height[l],height[r])*(r-l) > MAX:
                MAX=min(height[l],height[r])*(r-l)
            elif height[r]>height[l]:
                l+=1
            else: r-=1
        
        return MAX
                