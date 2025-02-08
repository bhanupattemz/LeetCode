
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def find(m,n):
            if m<=n:
                mid=m+(n-m)//2
                if mid*mid==num:
                    return True
                if mid*mid>num:
                    return find(m,mid-1)
                elif mid*mid<num:
                    return find(mid+1,n)
            return False
        return  find(0,num) 
        
print(Solution().isPerfectSquare(16))