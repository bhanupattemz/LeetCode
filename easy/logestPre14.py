class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre=""
        for i in range(len(strs[0])):
            letter=strs[0][i]
            for j in range(len(strs)):
                if len(strs[j])==i or letter!=strs[j][i] :
                    return pre
            pre+=letter
        return pre

print(Solution().longestCommonPrefix(["ab", "a"]))