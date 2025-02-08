class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        al=len(a)-1
        bl=len(b)-1
        i,j=al,bl
        carry="0"
        result=""
        while i>-1 and j>-1:
            if(a[i]=="1" and b[j]=="1"):
                result+=carry
                carry="1"
            elif(a[i]=="0" and b[j]=="0"):
                result+=carry
                carry="0"
            else:
                result+=carry+"1"
                carry="0"
            i-=1
            j-=1
        print(result)
        if carry=="0":
            remain=a[0:i]+b[0:j]
            result=remain+result[::-1] 
        return result
print(Solution().addBinary("1100","11"))