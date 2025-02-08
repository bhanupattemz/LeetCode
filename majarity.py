class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        obj={}
        maxi=[0,0]
        for num in nums:
            if num in obj:
                obj[num]+=1
            else:
                obj[num]=1
        for key,val in obj.items():
            if val>maxi[1]:
                maxi[0]=key
                maxi[1]=val
        return maxi[0]
print(Solution().majorityElement([3,2,3,4,5]))