class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=0
        maxi=0
        for i in gain:
            alt+=i
            if alt>maxi:
                maxi=alt
        return maxi
print(Solution().largestAltitude([-5,1,5,0,-7]))