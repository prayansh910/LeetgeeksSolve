class Solution(object):
    def longestMountain(self, arr):
        mountain=up=down=0
        i=1
        n=len(arr)
        while(i<n):
            
            up=down=0
            while(i<n and arr[i]>arr[i-1]):
                up+=1
                i+=1
            while(i<n and arr[i]<arr[i-1]):
                down+=1
                i+=1
            if up>0 and down>0:
                mountain=max(mountain,up+down+1)
            if up==0 and down==0:
                i+=1
        return mountain

        