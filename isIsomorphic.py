class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        obj={}
        for i in range(len(s)):
            vals=list(obj.values())
            if (t[i] in vals and s[i] not in obj) or (s[i] in obj and t[i] not in vals) :
                return False
            if s[i] not in obj:
                obj[s[i]]=t[i]
        return True
print(Solution().isIsomorphic("bbbaaaba","baba"))