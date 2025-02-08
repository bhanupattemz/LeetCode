class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels={"a","e","i","o","u","A","E","I","O","U"}
        index=-1
        result=[]
        for i in range(len(s)):
            if s[i] in vowels:
                if not index==-1:
                    result.append(result[index])
                    result[index]=s[i]
                else:
                    result.append(s[i])
                index=i
            else:
                result.append(s[i])
        return "".join(result)
print(Solution().reverseVowels("hello"))