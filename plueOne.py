class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(k) for k in str(int("".join(str(i) for i in digits))+1)]
print(Solution().plusOne([1,2,3,4]))