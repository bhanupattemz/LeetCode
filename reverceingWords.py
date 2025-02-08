class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([data for data in s.strip().split(" ") if not (data==" " or data=="")][-1::-1])
        
print(Solution().reverseWords("a good   example"))