
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        a={}
        b={}
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        for c1,c2 in zip(pattern,s):
            if (c1 in a and a[c1] !=c2) or (c2 in b and b[c2]!=c1):
                return False
            if c1 not in a:
                a[c1]=c2
                b[c2]=c1
        return True
print(Solution().wordPattern("abc","b c a"))