class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,k,j=0,0,m
        past=0
        for i in range(m,m+n) :
            nums1[i]=nums2[i-m]
        nums1.sort()
        print([1,2,3].pop([1,2,3].index(3)))
    
        return nums1
    
    
print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))