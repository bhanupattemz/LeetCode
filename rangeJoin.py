class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n=nums[0]
        list=[]
        for i in range(1,len(nums)):
            if nums[i]==n+1:
                continue
            list.append([n,i])
        return list
print(Solution().summaryRanges([0,1,2,4,5,7]))