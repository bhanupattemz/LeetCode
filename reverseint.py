
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=0
        if x>0:
            flag=True
        else:
            flag=False
            x=-x
        while x>0:
            num=num*10+x%10
            x=x//10
        if x<-2147483648 or x> 2147483647:
            return 0
        return num if flag else -num
print(Solution().reverse(-123))