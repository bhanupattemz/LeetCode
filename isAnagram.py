class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=len(s)
        if l!=len(s):
            return False
        s=list(s)
        t=list(t)
        i=l-1
        while i>=0 :
            print(s,t)
            if s[i] not in t:
                return False
            t.remove(s.pop())
            i-=1
        return True
print(Solution().isAnagram("anagram","nagaram"))
            