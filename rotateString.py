class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        l=len(s)
        if(len(goal)!=len(s)):
            return False
        for i in range(0,len(s)):
            if(s[l-i:]+s[0:l-i]==goal):
                return True
        return False