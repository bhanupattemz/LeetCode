class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle in haystack :
            return -1
        if haystack==needle:
            return 0
        for i in range(0,len(haystack)):
            if(i+len(needle)<=len(haystack) and haystack[i:i+len(needle)]==needle):
                return i
        return i

print(Solution().strStr("mississippi","pi"))