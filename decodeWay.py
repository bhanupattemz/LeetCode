class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=1
        def check(string):
            if len(string)>1:
                nonlocal num
                if int(string[0:2])<=26:
                    num+=1
                    check(string[2:])
                    
                else:
                    check(string[1:])
        for i in range(len(s)):
            if i<len(s)-1 and int(s[i:i+2])<=26:
                num+=1
                check(s[i+2:])
                check(s[0:i])
        return num
print(Solution().numDecodings("121124"))
        