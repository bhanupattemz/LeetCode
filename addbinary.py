class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result=[]
        i=len(a)-1
        j=len(b)-1
        carry=0
        while i>-1 and j>-1:
            sum=int(a[i])+int(b[j])+int(carry)
            if sum==2:
                carry=1
                result.append(0)
            else:
                carry=0
                result.append(1)
            i-=1
            j-=1
        return result
print(Solution().addBinary("11","1"))
            