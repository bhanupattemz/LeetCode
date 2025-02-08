class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            n=-n
        def check(mini,maxi):
            if mini<maxi:
                mid=(mini+maxi)//2
                num=2**mid
                if num==n or num==-n:
                    return True
                elif num>n :
                    return check(mini,mid)
                elif num<n:
                    return check(mid+1,maxi)
            return False
        return check(0,31)
print(Solution().isPowerOfTwo(-15))