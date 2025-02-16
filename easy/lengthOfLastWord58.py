class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        if(not " " in s):
            return len(s)
        i=len(s)-1
        while True:
            if(s[i]==" "):
                return len(s[i+1:])
            i-=1
print(Solution().lengthOfLastWord("Hello World"))