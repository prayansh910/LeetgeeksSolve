class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n=[]
        n=nums1+nums2
        n.sort()
        l=len(n)
        if l%2==0:
            x=(n[l/2]+n[(l/2)-1])/2.0
            return x
        else:
            x=n[((l+1)/2)-1]
            return x

