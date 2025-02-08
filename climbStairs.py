class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def climb(step,num,sol):
            step=step+num
            if(step==n):
                return sol+1
            sol=climb(step,1,0)
            if step+2<=n:
                sol=climb(step,2,0)
            return sol
        sol=climb(0,1,0)
        sol+=climb(0,2,0)
        return sol
print(Solution().climbStairs(3))