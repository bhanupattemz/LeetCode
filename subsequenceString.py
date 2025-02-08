class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(not s):
            return True
        i=0
        for letter in t: 
            if i<len(s) and letter==s[i] :
                i+=1
        return True if i==len(s) else False
print(Solution().isSubsequence("b","abc"))