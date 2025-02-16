import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(n):
            if(n<2):
                return x
            if(n%2==0):
                a=power(int(n/2))
                return a*a
            else:
                a=power(int((n-1)/2))
                return x*a*a
        result=power(n)
        return result if n>0 else 1/result
        # return math.pow(x,n)

print(Solution().myPow(0.00001,2147483647))