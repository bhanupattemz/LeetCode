import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        subs=""
        subs=re.sub(r'[^a-z0-9]','',s)
        for i in range(int(len(subs)/2)):
            if not subs[i]==subs[len(subs)-i-1]:
                return False
        return True
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))