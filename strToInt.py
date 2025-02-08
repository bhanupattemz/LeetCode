class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        length=len(s)
        if length==0:
            return 0
        elif s[0]=="-":
            flag=False
            i=1
        elif s[0]=="+":
            flag=True
            i=1
        elif s[0].isdecimal():
            flag=True
            i=0
        
        else:
            return 0
        start=i
        while i<length:
            if not s[i].isdecimal():
                break
            i+=1
        if start==i:
            return 0
        num=int(s[slice(start,i)])
        num =num if  flag else -num
        if num<-2147483648:
            return -2147483648
        elif num> 2147483647:
            return 2147483647
        
        return num

print(Solution().myAtoi(""))