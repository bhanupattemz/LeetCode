class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result=[]
        maxi=max(candies)
        for item in candies:
            result.append(item+extraCandies>=maxi)
        return result
            
print(Solution().kidsWithCandies([2,3,5,1,3],3))