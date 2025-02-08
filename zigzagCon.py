class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s)<3:
            return s
        string=''
        length=len(s)
        n=numRows*2-2
        for i in range(numRows):
            if i==0 or i==numRows-1:
                string+=s[slice(i,length,n)]
                
            else:
                temp1=i
                temp2=n-i
                for j in range(i,length):
                    if j==temp1:
                        string+=s[j]
                        temp1=temp1+n
                    elif j==temp2:
                        string+=s[j]
                        temp2+=n
        
        return string

print(Solution().convert("PAYPALISHIRING",3))