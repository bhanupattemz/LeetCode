class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        i=0
        for item in nums[l-k:]+nums[0:l-k]:
            nums[i]=item
            i+=1
        return 
print(Solution().rotate([1,2,3,4,5,6,7],3))