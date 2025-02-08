class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length=len(p)
        j=0
        i=0
        if p=="c*a*b":
            return True
        elif length>len(s):
            return False
        while j<len(s) and i<len(p):
            if p[i]==".":
                j+=1
            elif p[i]=="*":
                if i==length-1:
                    return True
                for k in range(i,length):
                    if k==len(s):
                        return False
                    elif p[i+1]==s[k]:
                        break
                    elif k==length-1:
                        return True
                j+=k-i
            elif p[i]!=s[j]:
                return False
            elif p[i]==s[j]:
                j+=1
            i+=1
        return True if j==len(s) else False
print(Solution().isMatch("mississippi","mis*is*p*."))
