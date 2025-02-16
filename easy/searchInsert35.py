class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target in nums):
            return nums.index(target)
        if(nums[len(nums)-1]<target):
             return len(nums)
    
        for i in range(0,len(nums)):
                if(nums[i]>target):
                    return i
       
       
        
print(Solution().searchInsert([1,2,3,4,6],7))