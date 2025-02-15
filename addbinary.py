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
            carry = sum // 2
            result.append(str(sum % 2))
            i-=1
            j-=1
        while i>=0:
            if(carry==1):
                sum=carry+int(a[i])
                carry=sum//2
                result.append(str(sum % 2))
            else:
                result.append(a[i])
            i-=1
        while j>=0:
            if(carry==1):
                sum=carry+int(b[j])
                carry=sum//2
                result.append(str(sum % 2))
            else:
                result.append(b[j])
            j-=1
        if(carry==1):
           result.append("1")
        return "".join(result[::-1])
    
print(Solution().addBinary("100","110010"))
            