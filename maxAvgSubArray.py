# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """
#         maxi=sum(nums[:k])
#         for i in range(1,len(nums)-k+1):
#             s=sum(nums[i:i+k])
#             if maxi<s:
#                 maxi= s
#         return maxi/float(k)
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s=sum(nums[:k])
        maxi=s
        for i in range(k,len(nums)):
            s+=nums[i]-nums[i-k]
            print(s)
            maxi=max(maxi,s)
        return maxi/float(k)
print(Solution().findMaxAverage([4,0,4,3,3],5))
            