class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            data=nums[i]
            nums.pop(i)
            if data not in nums:
                return data
            nums.insert(i,data)
print(Solution().singleNumber([2,2,1]))
            
        